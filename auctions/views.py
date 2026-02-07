from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, AuctionList, Bid, Comment, Category
from decimal import Decimal
# show active listing
# def index(request):
#     return render(request, "auctions/index.html", {
#         "listings": AuctionList.objects.filter(is_active=True) #marked
#     })
def index(request):
    listings = AuctionList.objects.filter(is_active=True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        # Ensure password matches confirmation
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# def auction_listing(request, item_id):
#     listing = AuctionList.get(pk=item_id)
#     bids = listing.bids.order_by("-amount")
#     comments = listing.comments.order_by("-timestamp")
#     return render(request, "auctions/layout.html", {
#         "auctions": auction,
#         "items": auction.item
#     })

def listing_detail(request, listing_id):
    # 1. Get the listing safely, get listing_id from url
    listing = get_object_or_404(AuctionList, pk=listing_id)
    # listing = AuctionList.objects.get(id=listing_id)
    # 2. Get related data
    bids = listing.bids.order_by("-amount")
    comments = listing.comments.order_by("-timestamp")

    # 3. Determine current price
    highest_bid = bids.first()
    if highest_bid:
        current_price = highest_bid.amount
    else:
        current_price = listing.starting_bid

    # 4. User-related flags (default values)
    is_owner = False
    is_watching = False
    is_winner = False

    if request.user.is_authenticated:
        is_owner = request.user == listing.owner
        is_watching = listing.watchlist.filter(id=request.user.id).exists()
        is_winner = (
            not listing.is_active
            and listing.winner == request.user
        )

    # 5. Handle POST actions
    error_message = None

    if request.method == "POST" and request.user.is_authenticated:

        # A. Place bid
        if "bid" in request.POST:
            bid_amount = (request.POST.get("bid_amount"))

            try:
                bid_amount = float(bid_amount)
            except (TypeError, ValueError):
                error_message = "Invalid bid amount."
            else:
                if not listing.is_active:
                    error_message = "This auction is closed."
                elif bid_amount <= current_price:
                    error_message = "Bid must be higher than current price."
                else:
                    Bid.objects.create(
                        bidder=request.user,
                        listing=listing,
                        amount=bid_amount
                    )
                    return HttpResponseRedirect(
                        reverse("listing_detail", args=[listing.id])
                    )

        # B. Toggle watchlist
        elif "watchlist" in request.POST:
            if request.user.is_authenticated and request.user != listing.owner:
                if request.user in listing.watchlist.all():
                    listing.watchlist.remove(request.user)
                else:
                    listing.watchlist.add(request.user)

            return HttpResponseRedirect(
                reverse("listing_detail", args=[listing.id])
            )

        # C. Add comment
        elif "comment" in request.POST:
            if request.user.is_authenticated:
                content = request.POST.get("content")

                if content:
                    Comment.objects.create(
                        author=request.user,
                        listing=listing,
                        # content=content`
                        content = request.POST["comment"]
                    )

            return HttpResponseRedirect(
                reverse("listing_detail", args=[listing.id])
            )

        # D. Close auction (owner only) - marked
        elif "close" in request.POST and is_owner:
            listing.is_active = False
            
            if highest_bid:
                listing.winner = highest_bid.bidder
            listing.save()

            return HttpResponseRedirect(
                reverse("listing_detail", args=[listing.id])
            )

    # 6. Render page
    return render(request, "auctions/listing_detail.html", {
        "listing": listing,
        "current_price": current_price,
        "bids": bids,
         "highest_bid": highest_bid,
        "comments": comments,
        "is_owner": is_owner,
        "is_watching": is_watching,
        "is_winner": is_winner,
        "error": error_message,
    })

@login_required
def create_listing(request):

    if request.method == "GET": # user opens page
        return render(request, "auctions/create.html", {
            "categories": Category.objects.all()
        })
    
    if request.method == "POST": # user submit form
        title = request.POST.get("title")
        description = request.POST.get("description")
        starting_bid = request.POST.get("starting_bid")
        image = request.FILES.get("image")
        category_id =request.POST.get("category")
        new_category = request.POST.get("new_category")

        category = None
        if new_category:
            category, created = Category.objects.get_or_create(
                name=new_category.strip()
            )
        elif category_id:
            category = Category.objects.get(id=category_id)
        
        listing = AuctionList.objects.create(
            owner = request.user,
            title = title,
            description=description,
            starting_bid=starting_bid,
            image=image,
            category=category
            )
        return redirect("index") # bkn return ke index.html

@login_required
def watchlist(request):
    listings = request.user.watchlist.all()

    for listing in listings:
        highest_bid = listing.bids.order_by("-amount").first()
        listing.current_price = (
            highest_bid.amount if highest_bid else listing.starting_bid
        )
        
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

@login_required
def toggle_watchlist(request, listing_id):
    print("WATCHLIST VIEW HIT")
    listing = get_object_or_404(AuctionList, id = listing_id)
    if request.method == "POST":
        if request.user in listing.watchlist.all():
            listing.watchlist.remove(request.user)
        else:
            listing.watchlist.add(request.user)

    return redirect("listing_detail", listing_id=listing.id)