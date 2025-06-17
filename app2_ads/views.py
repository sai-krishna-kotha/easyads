from django.shortcuts import render, redirect, HttpResponse
from .models import Ad, Seller
from .forms import AdForm  # You’ll create this next
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    if request.user.user_type == 'seller':
        return HttpResponse("I am in seller dashboard")
    elif request.user.user_type == 'customer':
        return HttpResponse("I am in customer dashboard")
@login_required
def create_ad(request):
    print("I am running")
    seller = Seller.objects.get(user=request.user)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = seller
            ad.status = 'PENDING'
            ad.save()
            return redirect('my_ads')  # Redirect to seller dashboard
    else:
        form = AdForm()
    return render(request, 'app2_ads/seller1.html', {'form': form})

def browse_ads(request):
    ads = Ad.objects.filter(status='APPROVED')
    return render(request, 'ads/browse_ads.html', {'ads': ads})
