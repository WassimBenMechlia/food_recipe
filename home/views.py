import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .cuisine import cuisine_map

# Create your views here.

class CombinedApiView(APIView):
    def get(self, request):
        # Make requests
        
        meals_response = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=')
        meals = meals_response.json()['meals']
        
        countries_origin={}
        for meal in meals:
            print(meal['strArea'])
            for k , v in cuisine_map.items():
                if meal['strArea'] == k :
                    countries_origin.update({k:v})
           
        print(countries_origin)
        
   

        return Response(countries_origin)