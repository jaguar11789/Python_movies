import requests
from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):

    url = 'https://api.themoviedb.org/3/movie/popular'

    params = {
        'api_key' : settings.TMDB_API_KEY,
        'language': 'ko-KR',
        'page'    : 1,
    }
    response = requests.get(url, params=params)

    data = response.json()

    context = {
        'movies': data['results'],
    }
    return render(request, 'movies/main.html', context)

def detail(request, movie_id):

    url = f'https://api.themoviedb.org/3/movie/{movie_id}'

    params = {
        'api_key'           : settings.TMDB_API_KEY,
        'language'          : 'ko-KR',
        'append_to_response': 'credits',
    }

    response = requests.get(url, params=params)

    data = response.json()

    context = {
        'movie': data,
        'cast' : data.get('credits', {}).get('cast', []),
    }
    return render(request, 'movies/detail.html', context)

def popular(request):

    page = int(request.GET.get('page', 1))

    url = 'https://api.themoviedb.org/3/movie/popular'

    params = {
        'api_key' : settings.TMDB_API_KEY,
        'language': 'ko-KR',
        'page'    : page,
    }
    response = requests.get(url, params=params)

    data = response.json()

    total_pages = data['total_pages']

    page_group = (page - 1) // 10

    start_page = page_group * 10 + 1
    end_page   = min(start_page + 9, total_pages)

    page_range = range(start_page, end_page + 1)

    context = {
        'movies'      : data['results'],
        'current_page': page,
        'total_pages' : total_pages,
        'page_range'  :page_range,
    }
    return render(request, 'movies/popular.html', context)

def movie_list(request):

    genre_id = request.GET.get('genre')
    page = int(request.GET.get('page', 1))

    url = 'https://api.themoviedb.org/3/discover/movie'

    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'ko-KR',
        'page': page,
    }
    if genre_id:
        params['with_genres'] = genre_id

    response = requests.get(url, params=params)

    data = response.json()
    total_pages = data['total_pages']

    page_group = (page - 1) // 10

    start_page = page_group * 10 + 1
    end_page = min(start_page + 9, total_pages)

    page_range = range(start_page, end_page + 1)

    context = {
        'movies': data['results'],
        'current_page': data['page'],
        'total_pages': data['total_pages'],
        'selected_genre': genre_id,
        'page_range': page_range,
    }
    return render(request, 'movies/movie_list.html', context)