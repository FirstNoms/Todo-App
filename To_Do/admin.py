from django.contrib import admin
from .models import ToDoModel, UserModel
# Register your models here.

admin.site.register(ToDoModel)
admin.site.register(UserModel)
