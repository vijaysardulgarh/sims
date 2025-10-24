
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index after successful login
        else:
            error = "Invalid username or password"
            return render(request, 'login.html', {'error': error})

    # If GET request, show login page
    return render(request, 'login.html')