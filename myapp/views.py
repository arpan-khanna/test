from django.shortcuts import render

# Create your views here.

def view_name(request):
    return render(request, 'myapp.html', {})
