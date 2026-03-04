# Rental Connects – Backend API

Backend application for a housing rental system.
This project was developed as a study project and demonstrates backend logic for advertisements, bookings, user roles, and JWT authentication.


## Main Features 

Users & Roles
User registration and authentication
JWT authentication (access / refresh tokens)
User roles:
Landlord — can create and manage advertisements
Tenant — can browse advertisements and create bookings
Advertisements
Create advertisements (Landlord only)
Update and delete advertisements
View list of advertisements
View advertisement details
Filtering:
by price range
by city
by number of rooms
Sorting by price and creation date
Bookings
Create bookings for selected dates
Date overlap validation (prevents double booking)
View own bookings
View busy dates for an advertisement
Comments
Add comments to advertisements
View comments for advertisements


## Technologies

Python 3.13
Django
Django REST Framework
MySQL
JWT (SimpleJWT)
Docker & Docker Compose


## How to run the project

1. Clone the repository

git clone https://github.com/Ruslan797/project_rental.git

2. Go to the project directory

cd project_rental

3. Create virtual environment

python -m venv venv

4. Activate virtual environment

Windows:
venv\Scripts\activate

Linux / Mac:
source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

6. Run migrations

python manage.py migrate

7. Start the server

python manage.py runserver


