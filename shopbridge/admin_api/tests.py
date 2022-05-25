import json
from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
from .models import Product,ProductReview
from .serializers import ProductSerializer,ProductDetailSerializer

client = Client()

class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            name='Casper', price=23, description='Casper description')
        Product.objects.create(
            name='Muffin', price=345, description='Muffin description')
        

    def test_get_all_products(self):
        # get API response
        response = client.get('/api/products/')
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateProductTest(TestCase):
    """ To ensure that we can create a product """


    def test_create_product(self):
        # get API response
        product_info = {
            'name':'Brush',
            'description':'Brush you teeth',
            'price':234,
        }
        response = client.post('/api/products/',product_info,format='json')
        # get data from db
        products = Product.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(products.count(),1)


class EditProductTest(TestCase):
    """ To edit an existing product """

    def setUp(self):
        Product.objects.create(name="Brush",description="test",price=234)


    def test_edit_product(self):
        # get API response
        product_info = {
            'id':1,
            'name':'Paint',
            'description':'Brush your teeth',
            'price':275,
        }
        response = client.patch('/api/products/1/',product_info,content_type='application/json')
        # get data from db
        product = Product.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product.name,'Paint')
        self.assertEqual(product.description,'Brush your teeth')
        self.assertEqual(product.price, 275)


class DeleteProductTest(TestCase):
    """ To delete a product """

    def setUp(self):
        Product.objects.create(name="Brush",description="test",price=234)


    def test_delete_product(self):

        response = client.delete('/api/products/1/')
        # get data from db
        products = Product.objects.all()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(products.count(),0)

class ProductReviewAddTest(TestCase):
    """ To add a product review """

    def setUp(self):
        Product.objects.create(name="Brush",description="test",price=234)


    def test_product_review_add(self):
        review_info = {
            'author':'anna',
            'review':'good',
            'product':1
        }

        response = client.post('/api/product_review',review_info,format='json')
        # get data from db
        product = Product.objects.get(id=1)
        reviews = product.productreview_set.all()
        review = reviews.first()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(reviews.count(),1)
        self.assertEqual(review.author,'anna')
        self.assertEqual(review.review,'good')



class ProductReviewGetAllTest(TestCase):
    """ To add a product review """

    def setUp(self):
        product = Product.objects.create(name="Brush",description="test",price=234)
        product.save()
        ProductReview.objects.create(product=product,author="anna",review="good")
        ProductReview.objects.create(product=product,author="amrutha",review="good")
        ProductReview.objects.create(product=product,author="deepika",review="good")
        


    def test_product_review_get_all(self):
        
        response = client.get('/api/product_review?id=1')
        # get data from db
        product = Product.objects.get(id=1)
        reviews = product.productreview_set.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(reviews.count(),3)


class ProductDetailViewTest(TestCase):

    def setUp(self):
        product = Product.objects.create(name="Brush",description="test",price=234)
        product.save()
        ProductReview.objects.create(product=product,author="anna",review="good")
        ProductReview.objects.create(product=product,author="amrutha",review="good")
        ProductReview.objects.create(product=product,author="deepika",review="good")
    
    def test_product_detail(self):
        
        response = client.get('/api/product_detail/1')
        # get data from db
        product = Product.objects.get(id=1)
        reviews = product.productreview_set.all()

        serialized = ProductDetailSerializer(product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serialized.data)
    
