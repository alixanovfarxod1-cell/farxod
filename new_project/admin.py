from django.contrib import admin
from .models import News,Category, Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Category)