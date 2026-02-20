# Project 2: Commerce

## Overview
**Commerce** is an eBay-like e-commerce auction site. It allows users to post auction listings, place bids, comment on listings, and manage a "watchlist". This application is built using the **Django** web framework.

---

## Features
The application fulfills the following core requirements:

* **Models**: The site includes at least three models in addition to the User model: **Auction Listings**, **Bids**, and **Comments**.
* **Create Listing**: Users can visit a dedicated page to create new listings. They specify a title, text-based description, and starting bid. Optional fields include an image URL and a category (e.g., Fashion, Toys, etc.).
* **Active Listings Page**: The default route displays all currently active auction listings. Each listing shows the title, description, current price, and photo if available.
* **Listing Page**: 
    * **Details**: Shows all listing details, including the current price.
    * **Watchlist**: Signed-in users can add or remove the item from their "Watchlist".
    * **Bidding**: Signed-in users can place bids that are at least as large as the starting bid and greater than any previous bids.
    * **Closing**: The listing creator can "close" the auction, making the highest bidder the winner. 
    * **Winning**: If a signed-in user wins a closed auction, the page displays a winner notification.
    * **Comments**: Signed-in users can add comments, and the page displays all existing comments for that listing.
* **Watchlist Page**: Displays all listings a signed-in user has added to their watchlist, with links to the individual listing pages.
* **Categories**: A page that lists all categories. Clicking a category displays

# [cite_start]Project 2: Commerce [cite: 14]

## Overview
[cite_start]**Commerce** is an eBay-like e-commerce auction site[cite: 17]. [cite_start]It allows users to post auction listings, place bids, comment on listings, and manage a "watchlist"[cite: 17]. [cite_start]This application is built using the **Django** web framework[cite: 66, 76].

---

## Features
The application fulfills the following core requirements:

* [cite_start]**Models**: The site includes at least three models in addition to the User model: **Auction Listings**, **Bids**, and **Comments**[cite: 92].
* [cite_start]**Create Listing**: Users can visit a dedicated page to create new listings[cite: 95]. [cite_start]They specify a title, text-based description, and starting bid[cite: 96]. [cite_start]Optional fields include an image URL and a category (e.g., Fashion, Toys, etc.)[cite: 97].
* [cite_start]**Active Listings Page**: The default route displays all currently active auction listings[cite: 98]. [cite_start]Each listing shows the title, description, current price, and photo if available[cite: 99].
* **Listing Page**: 
    * [cite_start]**Details**: Shows all listing details, including the current price[cite: 101].
    * [cite_start]**Watchlist**: Signed-in users can add or remove the item from their "Watchlist"[cite: 102, 103].
    * [cite_start]**Bidding**: Signed-in users can place bids that are at least as large as the starting bid and greater than any previous bids[cite: 104, 105].
    * [cite_start]**Closing**: The listing creator can "close" the auction, making the highest bidder the winner[cite: 107]. 
    * [cite_start]**Winning**: If a signed-in user wins a closed auction, the page displays a winner notification[cite: 108].
    * [cite_start]**Comments**: Signed-in users can add comments, and the page displays all existing comments for that listing[cite: 109, 110].
* [cite_start]**Watchlist Page**: Displays all listings a signed-in user has added to their watchlist, with links to the individual listing pages[cite: 111, 112].
* [cite_start]**Categories**: A page that lists all categories[cite: 117]. [cite_start]Clicking a category displays all active listings within that specific group[cite: 118].
* [cite_start]**Django Admin Interface**: Site administrators can view, add, edit, and delete any listings, comments, and bids[cite: 119].

---

## Getting Started

### Installation & Setup
1.  [cite_start]**Download the distribution code** and unzip the project files[cite: 59, 61].
2.  [cite_start]**Navigate** to the `commerce` directory in your terminal[cite: 62].
3.  **Initialize the Database**:
    * [cite_start]Run `python manage.py makemigrations auctions` to create migrations for the app[cite: 63].
    * [cite_start]Run `python manage.py migrate` to apply migrations to the database[cite: 64].
4.  [cite_start]**Create an Admin Account**: Run `python manage.py createsuperuser` to access the admin interface[cite: 121].
5.  [cite_start]**Start the Server**: Run `python manage.py runserver` and visit the site at `http://127.0.0.1:8000`[cite: 76].

### Project Structure
* [cite_start]`auctions/`: The main application directory[cite: 144].
* [cite_start]`auctions/models.py`: Contains data models for listings, bids, and comments[cite: 81, 88].
* [cite_start]`auctions/views.py`: Contains the logic for the different routes (index, login, etc.)[cite: 69, 70].
* [cite_start]`auctions/urls.py`: Defines the URL configuration for the application[cite: 67].
* [cite_start]`auctions/templates/`: Contains HTML templates, including the shared layout[cite: 78].

---

## Submission Screencast
[cite_start]A video demonstration of this project's functionality (not exceeding 5 minutes) is required for submission[cite: 150]. [cite_start]The video demonstrates all seven elements of the specification with corresponding timestamps in the description[cite: 151, 154].

> [cite_start]**Note**: This project was developed as part of CS50's Web Programming with Python and JavaScript[cite: 2].
