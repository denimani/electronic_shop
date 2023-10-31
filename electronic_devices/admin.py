from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from electronic_devices.models import NetworkNode, Product, Supplier


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'debt', 'level', 'created_at', 'supplier_link')
    list_filter = ('city',)
    search_fields = ('name', 'email', 'country')
    actions = ['debt_zero']

    def supplier_link(self, obj):
        """
        Данная функция возвращает ссылку на поставщика.
        """

        url = reverse('admin:%s_%s_change' % (obj.supplier._meta.app_label, obj.supplier._meta.model_name),
                      args=[obj.supplier.id])
        return mark_safe('<a href="{}">{}</a>'.format(url, obj.supplier.name))

    supplier_link.short_description = 'Поставщик'

    def debt_zero(self, request, queryset):
        queryset.update(debt=0)

    debt_zero.short_description = 'Обнулить долг'


admin.site.register(Product)
admin.site.register(Supplier)
