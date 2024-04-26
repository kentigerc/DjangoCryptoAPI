from django.shortcuts import render
import requests

def index(request):
  
  
  
  
  r2 = requests.get('https://www.boredapi.com/api/activity')
  data = r2.json()
  activity  = data['activity']

  r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  res = r.json()
  price = res['bpi']['USD']['rate']
  
  return render(request, 'templates/index.html', {'price': price})