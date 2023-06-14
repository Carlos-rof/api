from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from .serializers import GetArticlesSerializer
from .resources import request_apinews

def home(request):
    return render(request, "apinews/home.html")

def search_results(request):
    query = request.GET.get('q')
    _page = request.GET.get('page')
    data = request_apinews(query=query, page=_page if _page else 1)
    paginator = Paginator(["items"] * data["totalResults"], 100)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'apinews/search_results.html', {'results': data["articles"], 'query': query, 'page': page})

api_view("GET")
def get_articles(request):
    query = request.GET.get("query")
    first_page_only = request.GET.get("first_page_only")
    data = request_apinews(query=query, first_page_only=bool(int(first_page_only)) if first_page_only.isdigit() else True)
    data = [x for x in data["articles"] if x["author"] and x["title"] and x["description"]]
    serializer = GetArticlesSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=True)
    return HttpResponse(serializer.data)
