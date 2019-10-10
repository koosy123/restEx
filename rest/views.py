from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
import requests
import json

#CBV
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#kakao api
url = "https://kapi.kakao.com/v1/translation/translate"
queryString = {"query":"나는 사과를 좋아합니다", "src_lang":"kr", "target_lang":"en"}
header = {"Authorization":"KakaoAK 774bd135eaa26e7a550af7fe1519cfd6"}
r = requests.get(url, params= queryString, headers=header)
print(json.loads(r.text))
