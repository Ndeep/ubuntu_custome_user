from rest_framework import serializers
from account.models import Client,Account,User
from rest_framework.validators import UniqueValidator


class AccountSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=Account
        fields=(
            'id',
            'name',
            'client',
        )
        read_only_fields=('client',)

class ClientSerializer(serializers.ModelSerializer):
    accounts=AccountSerializer(many=True)
    class Meta:
        model=Client
        fields=(
            'id',
            'name',
            'accounts'
        )

    def create(self, validated_data):
        accounts=validated_data.pop('accounts')
        client=Client.objects.create(**validated_data)
        for account in accounts:
            Account.objects.create(**account,client=client)
        return client

    def update(self, instance, validated_data):
        accounts=validated_data.pop('accounts')
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        keep_accounts=[]
        existing=[c.id for c in instance.accounts]
        for account in accounts:
            if "id" in account.keys():
                if Account.objects.filter(id=account['id']).exists():
                    a=Account.objects.get(id=account['id'])
                    a.name=account.get('name',a.name)
                    a.save()
                    keep_accounts.append(a.id)
                else:
                    continue
            else:
                a=Account.objects.create(**account,client=instance)
                keep_accounts.append(a.id)

        return instance







class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,
                                 validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())])

    password=serializers.CharField(min_length=8)

    def create(self, validated_data):
        user=User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user

    class Meta:
        model=User
        fields=('id','username','email','password')
        read_only_fields=('account',)
