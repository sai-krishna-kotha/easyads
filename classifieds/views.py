from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, CreateView, UpdateView, View,DeleteView,DetailView)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Ad, Seller, Category, City, Customer
from accounts.models import User
from .forms import AdForm, SellerForm, ContactForm
from django.views import View
from django.db.models import Q

class SellerRegistrationView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        current_user = self.request.user.user_type
        return current_user == 'seller' or current_user == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("You are not authorized to access this page.")
    
    def get(self, request):
        form = SellerForm()
        return render(request, 'classifieds/seller_registration.html', {'form': form})

    def post(self, request):
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.verified = True
            seller.save()
            return redirect('classifieds:seller_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('classifieds:seller_dashboard')
    


class SellerDashboardView(LoginRequiredMixin,  ListView):
    model = Ad
    template_name = 'classifieds/seller_dashboard.html'
    context_object_name = 'ads'

    def get_queryset(self):
        self.seller = Seller.objects.filter(user=self.request.user).first()
        if self.seller:
            return Ad.objects.filter(seller=self.seller).order_by('-created_at')
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seller'] = getattr(self, 'seller', None)
        if not self.seller:
            context['form'] = SellerForm()
        return context


class AdCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'classifieds/create_ad.html'
    success_url = reverse_lazy('classifieds:seller_dashboard')

    def test_func(self):
        current_user = self.request.user.user_type
        return current_user == 'seller' or current_user == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("You are not authorized to access this page.")
    
    def form_valid(self, form):
        seller = get_object_or_404(Seller, user=self.request.user)
        form.instance.seller = seller
        form.instance.status = 'PENDING'
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'classifieds/edit_ad.html'
    success_url = reverse_lazy('classifieds:seller_dashboard')

    def test_func(self):
        ad = self.get_object()
        current_user = self.request.user
        return ad.seller.user == current_user or current_user.user_type == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("You are not authorized to access this page.")
    
    def get_queryset(self):
        seller = get_object_or_404(Seller, user=self.request.user)
        return Ad.objects.filter(seller=seller)  # Ensures seller can only edit their own ads

class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    template_name = 'classifieds/delete_ad_confirm.html'  # You'll create this
    success_url = reverse_lazy('classifieds:seller_dashboard')

    def test_func(self):
        # Only allow the admin and seller who owns the ad to delete it
        ad = self.get_object()
        current_user = self.request.user
        return ad.seller.user == current_user or current_user.user_type == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("You are not authorized to access this page.")

class AdDetailView(DetailView):
    model = Ad
    template_name = 'classifieds/ad_detail.html'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()

        in_wishlist = False
        user = self.request.user

        if user.is_authenticated and hasattr(user, 'customer'):
            in_wishlist = ad in user.customer.wishlist.all()

        context['in_wishlist'] = in_wishlist
        return context

class HomePageView(View):
    def get(self, request):
        sort_option = request.GET.get('sort', 'newest')
        category_slug = request.GET.get('category')
        city_slug = request.GET.get('city')
        query = request.GET.get('q', '')

        ads = Ad.objects.filter(status="Approved")
        
        if category_slug:
            ads = ads.filter(category__slug=category_slug)

        if city_slug:
            ads = ads.filter(city__slug=city_slug)

        if query:
            ads = ads.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        if sort_option == 'newest':
            ads = ads.order_by('-created_at')
        elif sort_option == 'oldest':
            ads = ads.order_by('created_at')
        elif sort_option == 'price-low':
            ads = ads.order_by('price')
        elif sort_option == 'price-high':
            ads = ads.order_by('-price')

        categories = Category.objects.all()
        cities = City.objects.all()

        return render(request, 'home.html', {
            'ads': ads,
            'sort_option': sort_option,
            'categories': categories,
            'cities': cities,
            'selected_category': category_slug,
            'selected_city': city_slug,
            'search_query': query
        })


class SellerProfileView(LoginRequiredMixin, DetailView):
    model = Seller
    template_name = 'classifieds/seller_profile.html'
    context_object_name = 'seller'

    def get_queryset(self):
        # Restrict sellers only to those who are verified if needed
        return Seller.objects.filter(verified=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seller = self.get_object()
        # Attach ads for display
        context['all_ads'] = seller.ads.all()
        context['ads'] = seller.ads.filter(status='Approved')  # only active ads
        for ad in context['ads']:
            print(ad.title)
            print(ad.seller.user)
        print(context['ads'])
        return context
class CustomerDashboardView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'classifieds/customer_dashboard.html'
    context_object_name = 'ads'

    def get_queryset(self):
        self.customer = Customer.objects.filter(user=self.request.user).first()
        if self.customer:
            return self.customer.wishlist.all()
        return []
    
class CustomerProfileView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'classifieds/customer_profile.html'
    context_object_name = 'customer'

    def get_object(self, queryset=None):
        return self.request.user.customer  # gets customer linked to current user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        context['wishlist'] = customer.wishlist.all()
        print(context['wishlist'])
        return context


class AddToWishlist(LoginRequiredMixin, View):
    def get(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        if request.user.user_type == 'customer':
            request.user.customer.wishlist.add(ad)
        elif request.user.user_type == 'seller':
            request.user.seller.wishlist.add(ad)

        return redirect(request.META.get('HTTP_REFERER', '/'))
class RemoveFromWishlist(LoginRequiredMixin, View):
    def get(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        if request.user.user_type == 'customer':
            request.user.customer.wishlist.remove(ad)
        elif request.user.user_type == 'seller':
            request.user.seller.wishlist.remove(ad)

        return redirect(request.META.get('HTTP_REFERER', '/'))

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: Save to DB or send email
            messages.success(request, "Thanks! Your message has been sent.")
            return redirect('contact')
        return render(request, 'contact.html', {'form': form})