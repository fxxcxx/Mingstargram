import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Mingstargram.settings import MEDIA_ROOT
from user.models import User
from .models import Feed


# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # feed에 있는 모든 데이터를 가져오겠다(select * from content_feed)

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        # 유저 정보 하드코딩 없이 처리 가능
        return render(request, "Mingstargram/main.html", context=dict(feeds=feed_list, user=user))  # 사전형식


class UploadFeed(APIView):
    def post(self, request):
        # 파일을 불러온다
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일 읽고 저장하는 부분, 경로를 적고 for문에 파일 변수 선언
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        asdf = uuid_name
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=asdf, content=content, user_id=user_id, profile_image=profile_image, like_count=0)

        return Response(status=200)


class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")
        return render(request, 'content/profile.html', context=dict(user=user))
