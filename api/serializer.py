from rest_framework import serializers

from .models import *


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeInformation
        fields = ('title', 'content')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description', 'logo_path', 'skill_type')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'snapshot_path', 'link', 'tagas')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'user_name', 'service_link', 'logo_path')
