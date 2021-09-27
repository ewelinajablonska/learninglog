from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for the requesting logs"""
    return render(request, 'learning_log/index.html')