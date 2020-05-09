from django.shortcuts import render


def sign_up(request):
    return render(request, 'accounts/sign_up.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # TODO: Need to route to home page
    return render(request, 'accounts/sign_up.html')  
