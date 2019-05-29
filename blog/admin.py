from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Opinion)
admin.site.register(Comment)