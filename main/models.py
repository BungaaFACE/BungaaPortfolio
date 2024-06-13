from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class SkillCategory(models.Model):
    name = models.CharField(_('Category name'), max_length=30, unique=True)

    class Meta:
        verbose_name = 'Skill Category'
        verbose_name_plural = 'Skill Categories'


class Skill(models.Model):
    name = models.CharField(_('Skill name'), max_length=30)
    percent = models.PositiveIntegerField(_("Aknowlegment Percent"))
    category = models.ForeignKey(SkillCategory, verbose_name=_("Skill Category"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


# Custom Field M-y string output
class MonthDateField(models.DateField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            return val.strftime("%m-%Y")
        return ''


class Experience(models.Model):
    company_name = models.CharField(_("Название компании"), max_length=50)
    vacancy_name = models.CharField(_("Название должности"), max_length=50)
    description = models.TextField(_("Описание"))
    date_start = MonthDateField(_("Дата начала"), auto_now=False, auto_now_add=False)
    date_finish = MonthDateField(_("Дата окончания"), auto_now=False, auto_now_add=False, **NULLABLE)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'


class ExperienceProject(models.Model):
    name = models.CharField(_("Название"), max_length=50)
    link = models.URLField(_("Ссылка"), max_length=200, **NULLABLE)
    description = models.TextField(_("Описание"))
    stack = models.CharField(_("Стэк"), max_length=50)
    experience = models.ForeignKey("Experience", 
                                   verbose_name=_("Опыт работы"), 
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Experience project'
        verbose_name_plural = 'Experience projects'

