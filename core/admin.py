from django.contrib import admin
from .models import Resumemodel
# Register your models here.
@admin.register(Resumemodel)
class Resumadmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']