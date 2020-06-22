from django.http import HttpResponse
from django.shortcuts import render
from app01.models import Sites


def add_book(request):
    # book = Sites(title="GOd", price=300, publish="DoG", pub_date="2008-8-8")
    book = Sites.objects.create(title="GOd", price=300, publish="DoG",
                                pub_date="2008-8-8")
    print(book, type(book))
    book.save()
    return HttpResponse("<p>数据添加成功</p>")


def show_book(request):
    books = Sites.objects.all()
    print(books, type(books))
    for i in books:
        print(i.title)
    return HttpResponse("<p>查找成功</p>")