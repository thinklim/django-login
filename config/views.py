from django.shortcuts import render


def get_index(request):
    if request.method == 'GET':
        return render(request, 'index.html')