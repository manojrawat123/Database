from django.contrib import admin
from usertracker.models import UserTracer

@admin.register(UserTracer)
class UserTracerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'ip_adress', 'date_of_birth', 'desc')
    list_filter = ('user_id', 'date_of_birth')
    search_fields = ('user_id__username', 'ip_adress')