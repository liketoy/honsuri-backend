from rest_framework import serializers # serializer import
from .models import Post, Comment, Like # 선언한 모델 import
from drf_yasg import openapi

# ModelSerializer 클래스를 사용하면 Model에 정의한 필드에 해당하는 값을 Serializer 에서 사용할 수 있음
class PostSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Post  # 모델 설정
        fields = '__all__'  # 필드 설정
        extra_kwargs = {'likeproduct': {'required': False}}
    # message = EmailMessageField()