# Rental Connects – Backend API

Backend application for a housing rental platform.
This project demonstrates real-world backend architecture including REST API design, authentication, booking logic, and AI-powered recommendations.

---

##  Main Features

###  Users & Roles

* User registration and authentication
* JWT authentication (access / refresh tokens)
* Role-based access:

  -Landlord — can create and manage advertisements
  -Tenant — can browse advertisements and create bookings

---

###  Advertisements

* CRUD API for rental listings
* Nested address support
* Filtering:

  -by price range
  -by city
  -by number of rooms
* Sorting:

  -by price
  -by creation date

---

###  Bookings

* Create bookings for selected dates
* Prevent overlapping bookings (validation logic)
* View personal bookings
* View busy dates for an advertisement

---

###  Comments & Ratings

* Add comments to advertisements
* Rating system with aggregation
* Automatic average rating calculation

---

###  AI-powered Recommendations

* Endpoint:
  `GET /api/rental/advertisements/<id>/similar/`

* Functionality:

  -Builds semantic representation of listings (title, description, address, etc.)
  -Uses Sentence -Transformers- to generate embeddings
  -Computes similarity via cosine similarity
  -Returns top similar advertisements with `similarity_score`

* Purpose:

  -Improves user experience
  -Demonstrates ML integration in backend services

---

##  Technologies

* -Python 3.12+-
* -Django-
* -Django REST Framework-
* -MySQL-
* -JWT (SimpleJWT)-
* -Docker & Docker Compose-
* -Sentence Transformers (NLP / AI)-

---


