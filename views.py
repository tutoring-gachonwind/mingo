from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .scraper import get_song_data

def index(request):
    return render(request, 'music/index.html')

@csrf_exempt
def search(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            artist = data.get('artist')
            print(f"Received search request for title: {title}, artist: {artist}")  # 디버깅 로그 추가
            results = get_song_data(title, artist)
            print(f"Scraping results: {results}")  # 디버깅 로그 추가
            return JsonResponse(results, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
