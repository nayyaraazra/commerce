from django.contrib import admin

from .models import AuctionList, User, Category, Bid, Comment
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_diplay = ("name")

class ListingsAdmin(admin.ModelAdmin):
    list_diplay = ("title", "image", "owner", "starting bid", "is_active", "category", "created at")
    list_filter = ("is_active", "category")
    search_fields = ("title", "description")

class BidsAdmin(admin.ModelAdmin):
    list_display = ("current_bid", "winner", "final_price")
    list_filter = ("listing",)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("commenter", "text", "listing")
    search_fields = ("content",)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")

admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionList)
admin.site.register(Bid)
admin.site.register(Comment)