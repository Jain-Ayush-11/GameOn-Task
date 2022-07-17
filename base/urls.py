from django.urls import path
from . import views

urlpatterns = [
    path('auction/', views.AuctionView.as_view()),
    path('bid/<int:pk>/', views.BidView.as_view()),
    path('user-bids/', views.BiddedView.as_view())
]