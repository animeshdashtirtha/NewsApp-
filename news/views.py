from django.shortcuts import render
import requests
from django.conf import settings

Api_key = settings.NEWS_API_KEY

def home(request):
    Search = request.GET.get('q')
    Search_in = request.GET.get('search_in', 'title,description,content') 

    if Search:
        # when user searches
        api_url = (
            f'https://newsapi.org/v2/everything'
            f'?q={Search}'
            f'&searchIn={Search_in}'
            f'&language=en'
            f'&sortBy=popularity'
            f'&apiKey={Api_key}'
        )
    else:
        # when no search -- show top headlines
        api_url = (
            f'https://newsapi.org/v2/top-headlines'
            f'?language=en'
            f'&apiKey={Api_key}'
        )

    response = requests.get(api_url)
    data = response.json()
    articles = data.get('articles', [])

    context = {
        'articles': articles,
        'selected_search_in': Search_in
    }

    return render(request, 'news/home.html', context)
