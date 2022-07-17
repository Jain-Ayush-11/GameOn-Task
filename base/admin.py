from django.contrib import admin
from . import models

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'winner')

class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'auction', 'amount')

# Register your models here.
admin.site.register(models.Auction, AuctionAdmin)
admin.site.register(models.Bid, BidAdmin)
