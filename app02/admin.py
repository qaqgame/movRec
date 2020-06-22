from django.contrib import admin
from app02.models import Book, Publish, Author, AuthorDetail
# Register your models here.


class BookInline(admin.TabularInline):
    model = Book


class AuthorInline(admin.TabularInline):
    model = Author


class BookAdmin(admin.TabularInline):

    list_display = ['title', 'price', 'pub_date', 'publish', 'authors']


class PublishAdmin(admin.ModelAdmin):
    inlines = [BookInline]


# class AuthorDetailInline(admin.TabularInline):
#     model = AuthorDetail
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [AuthorDetailInline]

admin.site.register([Book])

admin.site.register(Publish, PublishAdmin)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register([AuthorDetail])
# admin.site.register(Author, AuthorAdmin)