from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Notice,ContactMessage

admin.site.register(Notice)
admin.site.register(ContactMessage)
