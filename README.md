Overview

Commerce is an eBay-like e-commerce auction site that allows users to post auction listings, place bids, comment on listings, and manage a personalized "watchlist". This application is built using the Django web framework.
+2

Features
The application fulfills the following core requirements:


Models: Includes at least three models in addition to the default User model: Auction Listings, Bids, and Comments.


Create Listing: Users can create new listings by specifying a title, description, and starting bid, with optional fields for an image URL and category.


Active Listings Page: The default route displays all currently active listings, including their title, description, current price, and photo.

Listing Page:

Users can view specific details and the current price of any listing.

Signed-in users can add/remove items from their Watchlist.

Signed-in users can place bids (which must be higher than the current price).

Listing creators can "close" an auction, declaring the highest bidder the winner.

Users can add and view comments on each listing.


Watchlist: A dedicated page for signed-in users to view all items they are currently watching.


Categories: A page listing all categories, which allows users to filter active listings by specific types (e.g., Fashion, Toys, Electronics).


Django Admin Interface: Site administrators can view, add, edit, and delete any site content directly through the admin portal.

Getting Started
Installation

Clone the repository and navigate into the commerce directory.

Install dependencies (ensure you have Python and Django installed).

Apply migrations:

Run python manage.py makemigrations auctions to prepare the database schema.

Run python manage.py migrate to apply the changes.


Create a Superuser: Run python manage.py createsuperuser to access the Django admin interface.


Run the Server: Execute python manage.py runserver and visit http://127.0.0.1:8000 in your browser.

File Structure
auctions/: The main application directory containing:


models.py: Database blueprints for Users, Listings, Bids, and Comments.
+1


views.py: Logic for rendering pages and handling user requests.


urls.py: Routing configuration.


templates/auctions/: HTML layouts and page-specific templates.

Specification Screencast
