from django.shortcuts import render


def home(request):
    return render(request, 'music/home.html', {'music': 'song'})