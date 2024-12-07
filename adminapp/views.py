from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def AdminHomePage(request):
    return render(request, 'adminapp/admin_home.html')

from django.shortcuts import redirect
from django.contrib.auth import logout

def AdminLogout(request):
    logout(request)
    return redirect('eventapp:ProjectHomePage')

from django.shortcuts import render, redirect
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event = request.POST.get('event')
        return HttpResponse(f"Thank you for registering!")
    else:
        event_name = request.GET.get('event', 'Unknown Event')
        return render(request, 'adminapp/registration.html', {'event_name': event_name})