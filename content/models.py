from django.db import models


# Create your models here.
class Feed(models.Model):
    content = models.TextField()  # 글내용 #textfield : 필드에 어떤 데이터가 들어가나 명시해줌
    image = models.TextField()  # 피드 이미지
    profile_image = models.TextField()  # 프로필 이미지 주소를 넣어주고 이를 클라이언트가 내려 받으면 이미지를 보여주는 형태
    user_id = models.TextField()  # 글쓴이
    like_count = models.IntegerField()  # 좋아요 수(숫자)
