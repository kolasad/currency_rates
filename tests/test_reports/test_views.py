from datetime import date

import pytest
from decimal import Decimal
from django.test import Client
from django.urls import reverse

from reports.models import CurrencyRate


@pytest.mark.django_db
def test_reports(currency_rate):
    client = Client()
    response = client.get(reverse('reports-list'))
    assert len(response.data) == 1
    assert response.status_code == 200

    response = client.get(reverse('reports-detail', args=(currency_rate.pk, )))
    assert Decimal(response.data['exchange_rate']) == currency_rate.exchange_rate
    assert response.data['currency'] == currency_rate.currency
    assert response.data['date'] == str(currency_rate.date)
    assert response.status_code == 200


@pytest.mark.django_db
def test_reports_filters(currency_rate):
    from_date = date(year=2019, month=5, day=2)
    name = 'ABC'
    CurrencyRate.objects.create(
        currency=name,
        date=from_date,
        exchange_rate=Decimal('1.1')
    )
    client = Client()
    response = client.get(reverse('reports-list'))
    assert len(response.data) == 2
    assert response.status_code == 200

    response = client.get("{}?date={}".format(reverse('reports-list'), from_date))
    assert len(response.data) == 1
    assert response.status_code == 200

    response = client.get("{}?currency={}".format(reverse('reports-list'), name))
    assert len(response.data) == 1
    assert response.status_code == 200
