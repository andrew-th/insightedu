from django.shortcuts import render
from .models import Enrollment
from .models import District  # Import the District model

def profile_view(request):
    districts = District.objects.all()  # Query all district records from the database
    data = Enrollment.objects.all() #Fetch all the records from the Table
    print(districts)  
    return render(request, 'myapp/profile.html', {'districts': districts, 'data': data})  # Pass the district data to the template

def index_view(request):
    data = Enrollment.objects.all()  # Fetch all records from Enrollment
    return render(request, 'myapp/index.html', {'data': data})

def compare_view(request):
    return render(request, 'myapp/compare.html')

def display_table1_data(request):
    data = Enrollment.objects.all()  # Fetch all records from Enrollment
    print(data)  # Check if data is being fetched
    return render(request, 'myapp/data.html', {'data': data})