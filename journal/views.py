from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'journal/index.html')

def foodAddition(request): #add a new food to the database by user entry
    response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=2VmCq7QyQkHLv67MnptJmF75p1AWv3MOkA0OumKJ')
