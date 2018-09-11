from django.shortcuts import render


def HomeIndex(request):
    context = {}
    return render(request, 'home.html', context)