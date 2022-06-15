from django.shortcuts import render
from rest_framework.views import APIView

from .models import Feed


# Create your views here.


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()  # feed에 있는 모든 데이터를 가져오겠다(select * from content_feed)

        for feed in feed_list:
            print(feed.content)

        return render(request, "Mingstargram/main.html", context=dict(feeds=feed_list))  # 사전형식
