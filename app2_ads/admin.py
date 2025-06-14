from django.contrib import admin
from .models import Ad, Category, Seller

# Register your models here.

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'status', 'created_at']
    list_filter = ['status', 'category']
    actions = ['approve_ads', 'reject_ads']

    def approve_ads(self, request, queryset):
        queryset.update(status='APPROVED', reviewed_by=request.user)
    approve_ads.short_description = "Approve selected Ads"

    def reject_ads(self, request, queryset):
        queryset.update(status='REJECTED', reviewed_by=request.user)
    reject_ads.short_description = "Reject selected Ads"

admin.site.register(Category)
admin.site.register(Seller)
