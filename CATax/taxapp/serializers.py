from rest_framework import serializers
from taxapp.models import Tax,TaxDetail


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tax
        fields = '__all__'

class TaxDetailSerializer(serializers.ModelSerializer):
    effectivefromdate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f%z")
    effectivetodate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f%z")
    class Meta:
        model = TaxDetail
        fields = ('tax','effectivefromdate','effectivetodate')