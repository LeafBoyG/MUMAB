from django.shortcuts import render

def index(request):
    """
    This view renders the main landing page.
    """
    return render(request, 'index.html')