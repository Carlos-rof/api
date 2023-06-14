from django.shortcuts import render


def home(request):
    return render(request, "apinews/home.html")

def search_results(request):
    query = request.GET.get('q')
    return render(request, 'apinews/search_results.html', {'results': [1, 2], 'query': query})
