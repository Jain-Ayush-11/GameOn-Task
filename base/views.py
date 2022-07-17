from rest_framework import generics, status
from rest_framework.response import Response
from .models import Bid, User, Auction
from .serializers import AuctionSerializer, BidSerializer
from rest_framework.permissions import AllowAny
from django.utils import timezone

# Create your views here.
class AuctionView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class BidView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        amount = request.data['amount']
        auction = Auction.objects.get(id=self.kwargs['pk'])
        current = timezone.now()
        if(auction.end_time>current):
            if amount >= (auction.start_price):
                request.data['auction'] = auction.id
                request.data['user'] = user.id
                try:
                    bid = Bid.objects.get(auction=auction.id, user=user)
                    print(bid.amount, amount)
                    if bid.amount >= amount:
                        return Response({'message':'Plsease Bid Higher. Amount Already Bid'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    else:
                        bid.amount = amount
                        bid.save()
                except:
                    bid = super().post(request, *args, **kwargs)
                if auction.winner is None:
                    auction.bid = amount
                    auction.winner = user
                    auction.save()
                else:
                    if int(amount) > auction.bid:
                        auction.bid = amount
                        auction.winner = user
                        auction.save()
                serializer = AuctionSerializer(instance=auction)
                return Response(serializer.data)
            return Response({'message':'Please Bid Higher'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({'message':'Auction Already Over'}, status=status.HTTP_406_NOT_ACCEPTABLE)

class BiddedView(generics.ListAPIView):
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(user=self.request.user)
