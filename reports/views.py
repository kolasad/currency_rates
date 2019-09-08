from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reports.models import CurrencyRate
from reports.scraper import ECBScraper
from reports.serializers import CurrencyRateSerializer


class ReportApiView(viewsets.ReadOnlyModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'currency']

    @action(detail=False, methods=['post'])
    def scrap(self, request):
        ECBScraper().scrap()
        return Response('success', status.HTTP_200_OK)
