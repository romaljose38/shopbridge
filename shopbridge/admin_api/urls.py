from django.urls import include,path
from rest_framework import routers
from .import views


product_router = routers.DefaultRouter()
product_router.register(r'products',views.ProductViewSet)


urlpatterns = [
    path('',include(product_router.urls),name='product_crud'),
    path('product_review',views.product_review_handler,name='product_review'),
    path('product_detail/<int:product_id>',views.product_detail_view,name='product_detail'),
    path('product_search',views.product_search_view, name='product_search')
]
