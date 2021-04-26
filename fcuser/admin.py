from django.contrib import admin
from .models import Fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Fcuser, FcuserAdmin)
admin.site.site_header = '관리자 페이지'
admin.site.index_title = '관리자 페이지'
admin.site.site_title = '관리자 페이지'