# Neufville-Williams-BSEM1201-Assignment-1-

Overview

This project demonstrates a simple library system using API design concepts and asynchronous programming in Python. It includes both API endpoint specifications and a simulation of how multiple users interact with a shared library system.

The goal is to model real-world library operations such as logging in, borrowing, returning, updating, and deleting records while handling concurrent requests.

Features
1. API Endpoints Design

The system defines several RESTful endpoints:

POST /auth/login
Authenticates users and returns a token.
GET /books/{id}
Retrieves details of a specific book.
PUT /users/{id}
Updates user information.
DELETE /books/{id}
Removes a book from the system.
2. Asynchronous Library Simulation

The Python script simulates real-time library interactions using asyncio:

Users can borrow books
Users can return books
Multiple users interact simultaneously
Handles resource conflicts (e.g., two users trying to borrow the same book)
How It Works
A shared dictionary acts as a mock database storing book availability.
asyncio is used to simulate delays and concurrent access.
asyncio.gather() runs multiple user actions at the same time.
The system demonstrates how conflicts occur when multiple users access the same resource.


Technologies Used

Python 3
Asyncio (for concurrency simulation)
REST API design principles
JSON (for request/response structure)


How to Run
Make sure you have Python 3 installed
Run the script:
python main.py
Observe how multiple users interact with the system in the console


If you want, I can also make this into a more “student-style” README (simpler language) or a more “professional GitHub” version with badges and formatting.
