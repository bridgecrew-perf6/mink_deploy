import re

from django.db import models
from django_summernote.models import AbstractAttachment, Attachment
from django.conf import settings
from accounts.models import User
from datetime import datetime, timedelta, timezone


# Create your models here.
class Board(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    name = models.CharField('상품명(내부용)', max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_article')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    subject = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    tag = models.CharField('태그', max_length=100)
    is_blind = models.BooleanField('공개 여부', default=False)
    voter = models.ManyToManyField(User, related_name='voter_article')
    writer = models.CharField('글쓴이', max_length=100)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.reg_date

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.reg_date.date()
            return str(time.days) + '일 전'
        else:
            return str(time.days) + '일 전'

    def count_voter_user(self):
        return self.voter.count()

    def __str__(self):
        return self.subject

    def extract_attachments(self) -> list[AbstractAttachment, ...]:
        img_urls = re.findall(r'src="(.*?)"', self.content)
        img_urls = [img_url.replace(settings.MEDIA_URL, '') for img_url in img_urls]

        img_attachment = Attachment.objects.filter(file__in=img_urls)

        return img_attachment

    def img_thumbnail(self):
        img_root = "/media/"
        icon_hidden = 'https://user-images.githubusercontent.com/85653591/157589936-bef76f01-c4eb-4378-8c42-f109d4169b9a.png'

        img = self.extract_attachments()
        img_url = img.first()
        if img_url is not None:
            return img_root + str(img_url.file)
        else:
            return icon_hidden


class Comment(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    content = models.TextField('내용')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    is_modify = models.BooleanField('수정 가능 여부', default=False)
    voter = models.ManyToManyField(User, related_name='voter_comment')

    def __str__(self):
        return self.content

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.reg_date

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.reg_date.date()
            return str(time.days) + '일 전'
        else:
            return False
