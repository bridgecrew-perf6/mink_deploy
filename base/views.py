from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from board.models import Board, Article


def index(request: HttpRequest):
    board = Board.objects.all()
    page = request.GET.get('page', '1')  # 페이지

    notice_index = Article.objects.filter(board=1).order_by('-id')
    paginator = Paginator(notice_index, 10)  # 페이지당 10개씩 보여주기
    notice_index_page_obj = paginator.get_page(page)

    mink_index = Article.objects.filter(board=2).order_by('-id')
    paginator = Paginator(mink_index, 10)  # 페이지당 10개씩 보여주기
    mink_index_page_obj = paginator.get_page(page)

    context = {'notice_index': notice_index_page_obj,
               'mink_index': mink_index_page_obj,
               'board': board,
               }
    return render(request, "home/main.html", context)

