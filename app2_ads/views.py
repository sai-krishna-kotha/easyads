from django.shortcuts import render, redirect, HttpResponse
from .models import Ad, Seller
from .forms import AdForm, SellerForm  # You’ll create this next
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # for error messages

# Create your views here.
from django.contrib import messages

@login_required
def seller_registration(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            
            seller = form.save(commit=False)
            seller.user = request.user
            seller.verified = True # approved to post ads   
            # print("I am valid\n\n\n")

            # Save seller
            seller.save()

            # Store verification result in session or messages
            request.session['isRegistered'] = True

            return redirect('seller_dashboard')
        else:
            print(form.errors.items())
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field},{error}")
            return redirect('seller_dashboard')
        
@login_required
def seller_dashboard(request):
    try:
        seller = Seller.objects.get(user_id=request.user)
        verification = {
            "isRegistered": True,
        }
        return render(request, 'app2_ads/seller_dashboard.html', {
            'verification': verification
        })

    except Seller.DoesNotExist:
        verification = {
            "isRegistered": False,
        }
        form = SellerForm()
        return render(request, 'app2_ads/seller_dashboard.html', {
            'verification': verification,
            'form': form
        })
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
