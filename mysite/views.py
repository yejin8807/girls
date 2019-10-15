from django.shortcuts import render
from django.utils import timezone
from .models import Post


from django.http import HttpResponse
Post.objects.filter(published_date__lte = timezone.now())# 출판일자가 지금보다 이전으로 들어있는 행만 검색
def homepage(request):
    return HttpResponse('여기는 홈 페이지')