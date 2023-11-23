from django.shortcuts import render

from django.shortcuts import render
from .models import District  # Import the District model

def profile_view(request):
    districts = District.objects.all()  # Query all district records from the database
    print(districts)  
    return render(request, 'myapp/profile.html', {'districts': districts})  # Pass the district data to the template

def index_view(request):
    return render(request, 'myapp/index.html')

def compare_view(request):
    return render(request, 'myapp/compare.html')
