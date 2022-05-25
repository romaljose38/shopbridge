from rest_framework import serializers
from .models import Product,ProductReview



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','description','date_created','price']


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = ['id','author','review','date_created','product']

 
    
class ProductReviewField(serializers.RelatedField):

    def to_representation(self,instance):
      
        return {'id':instance.id,
                'author':instance.author,
                'review':instance.review,
                'date':str(instance.date_created)
                }

    def get_queryset(self):
        return ProductReview.objects.all()



class ProductDetailSerializer(serializers.ModelSerializer):
        productreview_set = ProductReviewField(many=True)

        class Meta:
            model = Product
            fields = ['id','name','description','date_created','price','productreview_set']
