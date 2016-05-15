from django.contrib import admin

from .models import IsrImage, IsrPhase, IsrPlatform
# Register your models here.

admin.site.register(IsrImage)
admin.site.register(IsrPhase)
admin.site.register(IsrPlatform)
