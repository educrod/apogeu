from __future__ import absolute_import, unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address, RegexValidator
from django.utils.html import format_html

class Customer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    dns_infix = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=100)
    vcenter_url = models.URLField(max_length=256,blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    def vcenter(self):
        if self.vcenter_url != None:
            return format_html('<a href="{}" target="_blank">Vcenter URL: {}</a>', self.vcenter_url,self.vcenter_url)
        else:
            return '-'
    def __str__(self):
        return self.name

class Nic(models.Model):
    name = models.CharField(max_length=10)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='nics')
    mac = models.CharField(unique=True, blank=True, null=True, max_length=17, validators=[RegexValidator(regex='^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', message='invalid MAC')])
    
    def save(self, *args, **kwargs):
        if self.mac == '':
            self.mac = None
        super(Nic, self).save( *args, **kwargs)
    
    def __str__(self):
        return self.name

class IP(models.Model):
    nic = models.ForeignKey(Nic, blank=True, null=True, on_delete=models.CASCADE, related_name='ips')
    address = models.CharField(unique=True, max_length=20, validators=[validate_ipv4_address])

    def __str__(self):
        return self.address
