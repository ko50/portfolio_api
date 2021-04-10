from rest_framework import viewsets, generics

from .models import *
from .serializer import *

# Normal


class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMeInformation.objects.all()
    serializer_class = AboutMeSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# ListAPIView


class AboutMeListAPIView(generics.ListAPIView):
    queryset = AboutMeInformation.objects.all()
    serializer_class = AboutMeSerializer


class SkillListAPIView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class WorkListAPIView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
