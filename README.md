# Currency Rates

App to currency Euro exchange rates.<br>
Data fetched from European Central Bank.

### Get the app running
Python 3.5.2<br>
Set up virtualenv and install packages with:<br>
pip install -r requirements.txt<br>
Migrate and run:<br>
python manage.py migrate<br>
python manage.py runserver<br>
To run test enter the command:<br>
pytest<br>
<br>
Local API usage:<br>
http://127.0.0.1:8000/api/report/<br>
You can use post /api/report/scrap to scrap page and create CurrencyRate objects.<br>
It takes some time to scrap pages.<br>
It can be updated with celery tasks to scrap page asynchronously after post request.<br>

### Deplyment
I would use https://github.com/joke2k/django-environ package to create .env file and prepare production settings.

### Preview
CurrencyRate objects have unique date and currency, based on received from ECB data (daily rates).<br>
Tests are placed in tests directory with all the configuration files.<br>
I found that sometimes is better to have all the pytest fixtures and apps tests in other directory than app directories, so I tried this setup and it looks pretty good.<br>
I also added simple api to view currency rates, scrap page and added some models to admin.
