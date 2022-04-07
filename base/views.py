from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from board.models import Board, Article


def index(request: HttpRequest):

    article_list = Article.objects.filter(board=2).order_by('-id')[:10]

    context = {
        'article_list': article_list,

    }

    return render(request, "home/main.html", context)
