from rest_framework import serializers
from catapp.models import Client,Account


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('client_name',)

class AccountSerializer(serializers.ModelSerializer):
    client=ClientSerializer(many=True,read_only=True)
    class Meta:
        model=Account
        fields=('account_name','client',)

    def create(self, validated_data):
        client=validated_data.pop('client')
        if Client.objects.get(pk=client['client_id']).exists():
            pass
