from django.contrib import admin
from .models import Order
from django.utils.html import format_html
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('fcuser', 'product', 'styled_status')

    def styled_status(self,obj):
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == '결제완료':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return format_html(f'<b>{obj.status}</b>')

    styled_status.short_description = '상태'
    
admin.site.register(Order, OrderAdmin)
