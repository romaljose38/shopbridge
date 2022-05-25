# shopbridge

The project is built using django.
Includes endpoints to perform ***CRUD operations*** on products.
Additionally ***reviews*** can be added to each product and products can be ***searched*** using their name.

The endpoints and request structures are as given below.
To perform CRUD operations on products
```/api/products/``` can be used
The structure for post to create product is
``` {
  "name":"product_name",
  "price":"price",
  "description":"description"
 ```
 ```GET``` request to the said endpoint lists all the products.
 ```/api/products/<id>/``` where id is the <id> of a product gives one product.
  
 To edit a product a patch request with the same body as the post request along with the product is used.
 for eg. To edit a product with id, 1.
  ```
    "id":1,
    "name":"Brush",
    "price":34,
    "description":"description"
  ```
  
