from django.shortcuts import render

# Create your views here.

def retornar_index(request):
    # request=requisição
    return render(request, 'index.html')