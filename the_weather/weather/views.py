from django.shortcuts import render


def index(request):

    # returns the index.html template
    return render(request, 'weather/index.html')
