Post/auth/login # User login endpoint allows the user to login to the library system if they have an account.

#Inputs 
{
    "username": "john_doe",
    "password": "2004123"
}

#Output/Response

200 #ok
{token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"}
                                             
Get/books/1 # Get book details endpoint allows the user to retrieve details of a specific book by its ID.

#inputs
URL #parameter: id (integer)


#Output/Response
{
    "id": 1,
    "title": "The diary of the wimpy kid",  
    "author": "Jeff Kinney",
    "published_date": "2007-04-01",
    "isbn": "978-1416524793",
    "pages": 224,
    "cover": "https://jsonplaceholder.typicode.com/users/3",
    "language": "English"
}

Put/users/2  # Update user details endpoint allows the user to update the details of a specific user by its ID.

#Inputs

{
  "name": "David",
  "age": 22
}

#Output/Response

201 #success
{
  "id": 2,
  "name": "David",
  "age": 22
}


Delete/books/3 # Delete book endpoint allows the user to delete a specific book by its ID.

#Inputs
URL #parameter: id (integer)

Output/Response
{204 #No Content:
("No response body")
}