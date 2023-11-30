from django.shortcuts import render
from .models import Enrollment
from .models import School
from .models import PssaExam
from .models import KeystoneExam
#from .models import District  # Import the District model

def profile_view(request):
    #districts = District.objects.all()  # Query all district records from the database
    data = Enrollment.objects.all() #Fetch all the records from the Table
    data1 = School.objects.all()
    year = request.GET.get('year', None)
    #Filter the records based on the year
    if year:
        data = Enrollment.objects.filter(year=year) #Filter records based on the year
    else:
        data = Enrollment.objects.all() #Fetch all the records if nothing has been selected
    #print(districts)  
    return render(request, 'myapp/profile.html', {'data': data, 'data1':data1})  # Pass the district data to the template

def index_view(request):
    data = Enrollment.objects.all()  # Fetch all records from Enrollment
    return render(request, 'myapp/index.html', {'data': data})

def compare_view(request):
    return render(request, 'myapp/compare.html')

def display_table1_data(request):
    data1 = School.objects.all()
    print(data1)
    return render(request, 'myapp/data.html', {'data1': data1})