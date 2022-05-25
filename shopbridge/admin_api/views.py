from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Product, ProductReview
from .serializers import (ProductDetailSerializer, ProductReviewSerializer,
                          ProductSerializer)

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



@api_view(['GET','POST'])
def product_review_handler(request): 
    if request.method == "POST":
        serialized = ProductReviewSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=201)
        else:
            return Response(status=400,data=serialized.errors)
        
    elif request.method == "GET":
        try:
            product_id = request.query_params['id']

            try:
                product = Product.objects.get(id=product_id)            
            except:
                product = None
            
            if product is not None:
                reviews = product.productreview_set.all()
                serialized = ProductReviewSerializer(reviews, many=True)
                return Response(status=200,data=serialized.data)
            else:
                return Response(status=400,data={"details":"product not found"})
        
        except:
            return Response(status=200, data={"details":"product id not given."})



# View to get detail information of products

@api_view(['GET'])
def product_detail_view(request,product_id):
    try:
        product = Product.objects.get(id=product_id)            
    except:
        product = None
    
    if product is not None:
        serialized = ProductDetailSerializer(product)
        return Response(status=200, data=serialized.data)
    else:
        return Response(status=400, data={"details:product does not exist"})
    
       


# View to handle the product search

@api_view(['GET'])
def product_search_view(request):
    try:
        name = request.query_params['name']  

        qs = Product.objects.filter(Q(name__icontains=name))
        serialized = ProductSerializer(qs,many=True)
      
        return Response(status=200, data=serialized.data)

    except Exception as e:
        return Response(status=400)
