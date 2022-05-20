from django.urls import path
from .views import school_list

app_name = 'school'
urlpatterns = [
    path('', school_list, name='school')
]
