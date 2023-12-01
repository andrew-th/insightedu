from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('', views.index_view, name='index'),
    path('compare/', views.compare_view, name='compare'),
    path('data/', views.display_table1_data, name='display_table1_data'),
    path('examp/', views.display_pssa_exam_data, name='display_pssa_exam_data'),
    path('keystone/', views.display_keystone_exam_data, name='display_keystone_exam_data'),
    path('district/', views.display_district_data, name='display_district_data')
]
