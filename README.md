# omerdjango

## About Project
This is just a dummy project for coding task for 3IVIS.

Author: Omer Khan Jadoon


## How to run this Project
pyenv install 3.10.0
pyenv virtualenv 3.10.0 djangoproject

pyenv activate djangoproject

pip install cookiecutter

pip install -r requirements/local.txt

npm install

python manage.py makemigrations

python manage.py migrate


python manage.py runserver

## Add Dummy Data to Postgresql
python manage.py shell

In the shell, import the model and create some dummy data:
```
from omerdjango.users.models import Fruit

Fruit.objects.create(name="Apple", calories=52)
Fruit.objects.create(name="Apricot", calories=48)
Fruit.objects.create(name="Avocado", calories=160)
Fruit.objects.create(name="Banana", calories=94)

print("Dummy data added!")
```

Exit the shell by typing exit().


## Troubleshooting:
If you get tooltip related error. Please follow these steps
You need to edit these files by replacing 'chart.tooltipContent' with 'chart.tooltip.contentGenerator' on the corresponding line on the 'nvd3' module at the python site-packages.

1.) pythonx.x/site-packages/nvd3/templates/content.html at line '54' and '63'

2.) pythonx.x/site-packages/nvd3/templates/piechart.html at line '18'