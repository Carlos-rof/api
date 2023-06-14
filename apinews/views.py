from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import GetArticlesSerializer
from .resources import request_apinews

def home(request):
    return render(request, "apinews/home.html")

def search_results(request):
    query = request.GET.get('q')
    data = request_apinews(query=query)
    return render(request, 'apinews/search_results.html', {'results': data["articles"], 'query': query})

api_view("GET")
def get_articles(request):
    query = request.GET.get("query")
    data = request_apinews(query=query)
    data = [x for x in data["articles"] if x["author"]]
    serializer = GetArticlesSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=True)
    return HttpResponse(serializer.data)
