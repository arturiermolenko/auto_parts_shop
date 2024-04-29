## Auto Parts Shop

This is an auto parts shop web application developed using Django. It is a one-stop-shop solution for purchasing auto parts online, allowing users to browse through a extensive collection of auto parts, add them to a shopping cart, and make payments securely.

### Features
 - User Authentication: Implemented Django's built-in authentication for user registration, login, and logout functionality.
 - Product Browsing: Users can browse through a varied assortment of auto parts.
 - Search Functionality: Implemented a search feature allowing users to look for specific items.
 - Shopping Cart Feature: Allows users to add items to a virtual shopping cart, view the items in their cart, and change quantities or remove items.
 - Secure Payments: Integrated a secure payment gateway for processing payments.

### Installation and Setup
 - Before you start, make sure you have Python 3.10 installed.
 - In order to set up and run this project locally, follow these steps:
 - Clone or download this repository to your local machine. git clone https://github.com/your_username/autoshop.git cd autoshop
 - Inside the project directory, create a virtual environment: python3 -m venv venv
 - Activate the virtual environment: Linux or Mac: source venv/bin/activate Windows: .\venv\Scripts\activate
 - Install the required packages from requirements.txt: pip install -r requirements.txt
 - Run the migrations: python manage.py makemigrations python manage.py migrate
 - Begin the development server: python manage.py runserver
 - Now, go to your web browser and enter http://127.0.0.1:8000 in the address bar to view and interact with the auto parts shop web application.

### Technologies Used
 - Django
 - Python
 - SQLite (default Django database)
 - HTML/CSS/Javascript
 - Bootstrap (for responsive design)

### Contributing
Feel free to fork this project, make changes in your own branch, and then issue a pull request. Although this project is small, we encourage you to submit bug reports or requests for future features.

### License MIT
Author Artur Iermolenko - Initial work

### This README file is a guide to the basic setup and principles of the project. It doesn't cover all the points that a README might typically contain, such as an extensive guide for contribution, the project's history, and acknowledgment section. Feel free to add those sections as the project develops.