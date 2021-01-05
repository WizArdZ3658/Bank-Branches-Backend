from rest_framework import serializers


class BankSerializer(serializers.Serializer):
    ifsc = serializers.CharField(max_length=11)
    bank_id = serializers.IntegerField()
    branch = serializers.CharField(max_length=74)
    address = serializers.CharField(max_length=195)
    city = serializers.CharField(max_length=50)
    district = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=26)

    class Meta:
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state')
