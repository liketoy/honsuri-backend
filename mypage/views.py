from django.shortcuts import render
from rest_framework import status
from recipe.models import Recipe
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class MyFavoriteView(APIView): 
    '''
    내가 북마크한 레시피 api
    ---
    결과: 좋아요한 레시피(아이디,사진,이름,태그요소들) 반환
    '''
    def get(self, request):
      user_id = request.user.pk

      queryset = Recipe.objects.filter(bookmark__in=[user_id])
      serializer = MyFavoriteSerializer(queryset, many=True) 

      return Response(serializer.data)

class MyPageView(APIView): 
    '''
    나의 정보 api
    ---
    결과: 나의정보(이메일,이름,닉네임,연락처), 관심정보(주량,최애술,최애안주,최애콤비) 반환
    '''
    def get(self, request):
      user_id = request.user.pk
      queryset = User.objects.filter(id = user_id)
      serializer = UserSerializer(queryset, many=True) 

      return Response(serializer.data[0])


class UserDeleteView(APIView):
    '''
    유저 id 받아서 회원탈퇴 api
    ---
    '''
    def delete(self, request, pk):
      user_id = request.user.pk
      if User.objects.get(id=pk, user_id=user_id):
        User.objects.get(id=pk).delete()
        return Response({'message': 'DELETED'}, status=status.HTTP_200_OK)
      else:
        return Response({'message': 'FAILED'}, status.HTTP_400_BAD_REQUEST)