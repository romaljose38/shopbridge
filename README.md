# shopbridge

The project is built using django.
Includes endpoints to perform ***CRUD operations*** on products.
Additionally ***reviews*** can be added to each product and products can be ***searched*** using their name.

The endpoints and request structures are as given below.
To perform CRUD operations on products
```/api/products/``` can be used
#### Create

The structure for post to create product is
``` {
  "name":"product_name",
  "price":"price",
  "description":"description"
 ```
 
 #### Retrieve
 ```GET``` request to the said endpoint lists all the products.
 ```/api/products/<id>/``` where id is the ```<id>``` of a product returns one product.
 
  #### Update
 To edit a product a ```PATCH``` request with the same body as the post request along with the product id is used.
 for eg. To edit a product with id, 1. A ```PATCH``` request is sent to ```/api/products/1``` with body
  ```
    "id":1,
    "name":"Brush",
    "price":34,
    "description":"description"
  ```
  
  #### Delete
  To delete a product a ```DELETE``` request to ```/api/products/<id>``` is used where <id> is replaced by the id of the product to be deleted.
  
  ### Product Review
  The endpoint to post reviews for a product is ```/api/product_review```
  The structure of the request body should be
  ```
    "product":"the id of the product reviewing",
    "author":"authors name",
    "review": "review"
  ```
  A ```GET``` request to the said endpoint with product id as a parameter can be used to get all the reviews of that product
  For eg. a ```GET``` request to ```/api/product_review?id=1``` gives all the reviews of the product having id, 1.
  
  ### Product Detail
  The endpoint to get detailed view of a product is ```/api/product_detail/<product_id>``` where ```<product_id>``` is the id of the required product.
  It returns basic details of the product along with its reviews.
  
  ### Product Search
  To search among products a ```GET``` request to ```/api/product_search``` can be used.
  For eg. To get all products having "br" in their product name
  We would send a ```GET``` request to ```/api/product_search?name=br```.
  
  ### Code Coverage
  Tests are written using the unittest module from the Python Standard Library.
  All the endpoints are checked necessarily.
  The tests are located in ```shopbridge/admin_api/tests.py```
  
  
 ### Instructions to run the server
  A lightweight ```sqllite``` database is used for the project. Integration with other databases is also seamless.
  After installing the required modules mentioned in the `requirements.txt`
  The server can be started using 
  ```python manage.py runserver```
  Also to run tests
  ```python manage.py test```
  
  
  
  
