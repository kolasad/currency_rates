from rest_framework.serializers import ModelSerializer

from reports.models import CurrencyRate


class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ['currency', 'exchange_rate', 'date']
