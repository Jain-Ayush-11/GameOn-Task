from rest_framework.serializers import ModelSerializer
from .models import Bid, User, Auction
from datetime import datetime
from django.utils import timezone

class AuctionSerializer(ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        current = timezone.now()
        if(instance.end_time>current):
            response.pop('winner')
            response.pop('bid')
            # response.pop('users')
        return response

class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'