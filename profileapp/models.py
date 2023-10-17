from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    #  on_delete=models.CASCADE의미 user가삭제될때 profile도 삭제
    #  related_name = profile객체를 찾지않더라도 user와 연결시켜주는것 ex) request.user.profile.nickname 과같은 명령어로 바로찾을수 있게

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # upload_to= 이미지가 어디에 업로드 될것인지  즉 'profile/'로 하면media/profile/###  경로에 이미지가 저장
    # null = 꼭 이미지가 없어도 된다
    image = models.ImageField(upload_to= 'profile/', null=True)
    # unique = 닉네임이 유니크 해야한다
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
