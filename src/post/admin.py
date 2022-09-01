from django.contrib import admin
from post import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Like)
admin.site.register(models.Coment)
admin.site.register(models.Vistas)