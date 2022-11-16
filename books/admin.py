from django.contrib import admin
from .models import Books, Comments, Authors

admin.site.register(Books)
admin.site.register(Comments)
admin.site.register(Authors)
# Register your models here.
