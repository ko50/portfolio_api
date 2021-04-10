from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/about_me/', include('about_me.urls', namespace='about_me')),
    path('api/v1/skills/', include('skills.urls', namespace='skills')),
    path('api/v1/works/', include('works.urls', namespace='works')),
    path('api/v1/contacts/', include('contacts.urls', namespace='contacts')),
]
