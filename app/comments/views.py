from django.http import HttpResponse
from django.shortcuts import render, redirect

# boom 누르는 순간 templates의 comments/boom.html로 이동
def boom(request):
    if request.method == 'GET':
        return render(request, 'comments/boom.html')
    else:
        return render(request, 'comments/boom.html')
