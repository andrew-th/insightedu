from django.shortcuts import render
from .models import Enrollment
from .models import School
from .models import PssaExam
from .models import KeystoneExam
from .models import DistrictF
from django.http import JsonResponse
#from .models import District  

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

def get_counties(request):
    counties = DistrictF.objects.values_list('county_n', flat=True).distinct()
    return JsonResponse(list(counties), safe=False)

def get_districts(request, county_name):
    districts = DistrictF.objects.filter(county_n=county_name).values_list('d_name', flat=True)
    return JsonResponse(list(districts), safe=False)

def view_data(request):
    data = Enrollment.objects.all()  # Fetch all records from Enrollment
    return render(request, 'myapp/view.html', {'data': data})

def compare_view(request):
    data5 = DistrictF.objects.all()
    print(data5)
    return render(request, 'myapp/compare.html', {'data5':data5})

def display_table1_data(request):
    data1 = School.objects.all()
    print(data1)
    return render(request, 'myapp/data.html', {'data1': data1})

def display_pssa_exam_data(request):
    data2 = PssaExam.objects.all()
    print(data2)
    return render(request, 'myapp/examp.html', {'data2': data2})

def display_keystone_exam_data(request):
    data3 = KeystoneExam.objects.all()
    print(data3)
    return render(request, 'myapp/keystone.html', {'data3': data3})

def display_district_data(request):
    data4 = DistrictForm.objects.all()
    print(data4)  # Check if data is correctly fetched
    return render(request, 'myapp/district.html', {'data4': data4})

def compare_data(request):
    data5 = DistrictF.objects.all()
    return render(request, 'myapp/compare.html', {'data5':data5})
