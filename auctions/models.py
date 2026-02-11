from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(
        max_length=64, unique=True
    )

    def __str__(self):
        return self.name
    
class AuctionList(models.Model):
    owner = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name="listings"
    )

    title = models.CharField(max_length=120)
    description = models.TextField()

    starting_bid = models.DecimalField(
        max_digits=10, decimal_places=2
    )

    image = models.ImageField(    # or URL field
       upload_to ="images/", blank = True, null = True 
    )

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="listings",  blank = True, null = True 
    )

    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    winner = models.ForeignKey(
        User, on_delete = models.SET_NULL,  blank = True, null = True, related_name ="won_auction"
    )

    watchlist = models.ManyToManyField(
        User, blank = True, related_name = "watchlist"
    )

    def __str__(self):
        return f"{self.title} (Active: {self.is_active})"

class Bid(models.Model):
    bidder = models.ForeignKey(
        User, on_delete= models.CASCADE, related_name = "bids"
    )

    listing = models.ForeignKey(
        AuctionList, on_delete=models.CASCADE, related_name="bids"
    )

    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder} bid {self.bid_amount} on {self.listing}"
    
class Comment(models.Model):
    commenter = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name="comments"
    )

    listing = models.ForeignKey(
        AuctionList, on_delete = models.CASCADE, related_name="comments"
    )

    comment_text = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment posted by {self.commenter} on {self.listing}"
    
