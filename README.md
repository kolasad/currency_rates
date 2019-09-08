# Currency Rates

App to currency Euro exchange rates.
Data fetched from European Central Bank.

### Get the app running
Python 3.5.2
Set up virtualenv and install packages with:
pip install -r requirements.txt
Migrate and run:
python manage.py migrate
python manage.py runserver
To run test enter the command:
pytest

Local API usage:
http://127.0.0.1:8000/api/report/
You can use post /api/report/scrap to scrap page and create CurrencyRate objects.
It takes some time to scrap pages.
It can be updated with celery tasks to scrap page asynchronously after post request.

### Deplyment
I would use https://github.com/joke2k/django-environ package to create .env file and prepare production settings.

### Preview
CurrencyRate objects have unique date and currency, based on received from ECB data (daily rates).
Tests are placed in tests directory with all the configuration files.
I found that sometimes is better to have all the pytest fixtures and apps tests in other directory than app directories, so I tried this setup and it looks pretty good.
I also added simple api to view currency rates, scrap page and added some models to admin.
