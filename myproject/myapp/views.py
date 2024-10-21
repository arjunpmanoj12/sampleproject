from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')
def sell(request):
    return render(request, 'myapp/sell.html')
def buy(request):
    return render(request, 'myapp/buy.html')
def login(request):
    return render(request, 'myapp/login.html')
def profile(request):
    return render(request, 'myapp/profile.html')
