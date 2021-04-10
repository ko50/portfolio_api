from django.db import models


class Skill(models.Model):
    SKILL_TYPE_LANG = 'Languages'
    SKILL_TYPE_FRAMEWORK = 'Frameworks'
    SKILL_TYPE_TOOL = 'Tools'
    SKILL_TYPE_SET = (
        (SKILL_TYPE_LANG, 'Languages'),
        (SKILL_TYPE_FRAMEWORK, 'Frameworks'),
        (SKILL_TYPE_TOOL, 'Tools')
    )

    name = models.CharField(max_length=8)
    description = models.TextField()
    logo_path = models.TextField()
    skill_type = models.CharField(choices=SKILL_TYPE_SET, max_length=32)
