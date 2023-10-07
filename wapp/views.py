from django.shortcuts import render
from django.http import JsonResponse 
import requests
# Create your views here.
def get_weatherdata(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        city=request.POST.get('city')
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR API KEY"
        response=requests.get(url)
        data=dict(response.json())
        weather_data={
            'city':city,
            'temp': round(data['main']['temp']- 273.15,2),
            'main':data['weather'][0]['main'],
        }
        return JsonResponse(weather_data) 
        # return render(request,"index.html",weather_data)

    return render(request,"index.html")
        