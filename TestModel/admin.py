from django.contrib import admin
from TestModel.models import Test, Contact, Tag
# Register your models here.


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']  # 如何显示
    search_fields = ('name', )
    inlines = [TagInline]  # 让Tag内联进Contact
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])