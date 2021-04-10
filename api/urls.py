from django.urls import path

from .views import *


app_name = 'api'
urlpatterns = [
    path('about_me', AboutMeListAPIView.as_view(), name='about_me'),
    path('skills', SkillsListAPIView.as_view(), name='skills'),
    path('works', WorksListAPIView.as_view(), name='works'),
    path('contacts', ContactsListAPIView.as_view(), name='contacts'),
]
