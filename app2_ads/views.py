from django.shortcuts import render, redirect, HttpResponse
from .models import Ad, Seller
from .forms import AdForm, SellerForm  # You’ll create this next
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def seller_registration(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.verified = False
            print("I am valid\n\n\n")
            seller.save()
            return HttpResponse("You are verified....")
    elif request.method == 'GET':
        form = SellerForm()
        return render(request, 'app2_ads/seller_dashboard.html', {'form':form})
def seller_dashboard(request):
    try:
        seller = Seller.objects.get(user_id=request.user)
        return render(request, 'app2_ads/seller_dashboard.html', {'sellerVerified':True})
    except Seller.DoesNotExist:
        return render(request, 'app2_ads/seller_dashboard.html', {'sellerVerified':False})
    # if request.user.user_type == 'seller':
    #     return render(request, 'app2_ads/seller_dashboard.html')
    
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
