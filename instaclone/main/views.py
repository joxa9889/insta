from django.shortcuts import render
from .models import User


# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User(username=username, password=password)
        user.save()
    return render(request, template_name='insta.html')
