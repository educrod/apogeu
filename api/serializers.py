from backend.models import Machine, Nic, IP, Customer
from rest_framework import serializers
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','dns_infix']

class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IP
        fields = ['address']

class NicSerializer(serializers.ModelSerializer):
    ips = IPSerializer(many=True)
    class Meta:
        model = Nic
        fields = ['name','ips']

class MachineSerializer(serializers.ModelSerializer):
    nics = NicSerializer(required=False, many=True)
    customer = CustomerSerializer(many=False, read_only=True)
    class Meta:
        model = Machine
        fields = ['name', 'nics','vcenter_url','customer']

    def create(self, validated_data):
        nics = validated_data.pop('nics')
        print(nics)
        machine = Machine.objects.create(**validated_data)
        for nic in nics:
            ips = nic.pop('ips')
            new_nic = Nic.objects.create(machine=machine,**nic)
            for ip in ips:
                IP.objects.create(nic=new_nic,**ip)
        
        return machine
