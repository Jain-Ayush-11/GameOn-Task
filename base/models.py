from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auction(models.Model):
    # start time, end time, start price, item name
    start_time = models.DateTimeField()
    end_time=models.DateTimeField()
    start_price = models.IntegerField()
    name = models.CharField(max_length=255)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='winner', null=True, blank=True)
    bid = models.IntegerField(default=0)
    # users = models.ManyToManyField(User, related_name='participants', blank=True)

    def __str__(self) -> str:
        return self.name

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auction')
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bidder')

    def __str__(self) -> str:
        return f'{self.user.username} -- {self.auction.name} -- {self.amount}'