from django.contrib import admin
from .models import magang, user

@admin.register(magang)
class magangAdmin(admin.ModelAdmin):
    list_display = ['Judul', 'Jurusan']
    list_filter = ['Publish']
    search_fields = ['Judul']

admin.site.register(user)