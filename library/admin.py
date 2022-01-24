from django.contrib import admin
from . import models

admin.site.register(models.BookCategory)
admin.site.register(models.Book_libComent)
admin.site.register(models.Expert)
admin.site.register(models.ExpertRecomendation)
