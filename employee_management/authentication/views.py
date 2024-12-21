from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Employees, Employers
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')  # Get the first name
        last_name = request.POST.get('last_name')    # Get the last name
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')     # Get the user type (Employees or Employers)

        # Combine first name and last name to create a username
        username = f"{first_name}.{last_name}"  # Adjust this based on your username format

        # Authenticate using username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect based on user type
            if user_type == 'employee':
                return redirect('employee_dashboard')  # Replace with your employee dashboard view
            elif user_type == 'employer':
                return redirect('employer_dashboard')  # Replace with your employer dashboard view
            else:
                messages.error(request, 'Invalid user type selected')
                return render(request, 'authentication/login.html')
        else:
            # Invalid login attempt
            messages.error(request, 'Invalid credentials')
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_type = request.POST['user_type']

        if user_type == "employees":
            Employees.objects.create(username=username, password=password, email=email)
        else:
            Employers.objects.create(username=username, password=password, email=email)

        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'authentication/register.html')
