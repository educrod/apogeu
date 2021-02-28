from django.contrib import admin
from backend.models import Machine, Nic, IP, Customer
import nested_admin

admin.site.site_header = 'Apogeu'

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    search_fields = ('name', 'dns_infix')
    list_display = ('name', 'dns_infix')


class IPAdmin(nested_admin.NestedStackedInline):
    model = IP
    classes = ['collapse',]
    extra = 0
    fieldsets = (
        (None,{
            'fields': ('address',)
        }),
    )

class NicAdmin(nested_admin.NestedTabularInline):
    model = Nic
    inlines = [IPAdmin]
    classes = ['collapse',]
    extra = 0
    fieldsets = (
        (None,{
            'fields': ('name','mac',)
        }),
    )

class MachineAdmin(nested_admin.NestedModelAdmin):
    save_as = True
    inlines  = [NicAdmin]
    list_filter = ('customer',)
    search_fields = ('name','nics__ips__address')
    save_as = True
    model = Machine
    list_display = ('name','vcenter','ip_display','customer')
    empty_value_display = ' - '
    fieldsets = (
        (None,{
            'fields': ('name','customer')
        }),
        ('More fields', {
            'classes': ('collapse',),
            'fields': ('vcenter_url',),
        }),
    )
    def ip_display(self, obj):
        return ", ".join([ip.address for ip in IP.objects.filter(nic__machine=obj)])

    ip_display.short_description = "IPS"

admin.site.register(Machine, MachineAdmin)
admin.site.register(Customer, CustomerAdmin)
