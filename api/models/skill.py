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

    name = models.CharField(max_length=32)
    description = models.TextField()
    icon = models.FileField(upload_to='skills/', null=True)
    skill_type = models.CharField(choices=SKILL_TYPE_SET, max_length=32)

    def __str__(self):
        return self.name
