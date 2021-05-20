from rest_framework import serializers

from .models import *


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeInformation
        fields = ('title', 'content')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description', 'skill_type', 'icon')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'screenshot', 'link', 'tags')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'user_name', 'service_link', 'logo')
