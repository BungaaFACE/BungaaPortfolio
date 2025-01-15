from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from main.services import get_unique_slag

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


class ProjectTag(models.Model):
    name = models.CharField(_("Тэг"), max_length=50)

    class Meta:
        verbose_name = 'Project Tag'
        verbose_name_plural = 'Project Tags'


class Project(models.Model):
    name = models.CharField(_("Название"), max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", **NULLABLE)
    link = models.URLField(_("Ссылка"), max_length=200, **NULLABLE)
    description = models.TextField(_("Описание"))
    stack = models.CharField(_("Стэк"), max_length=50)
    demo = models.URLField(_("Ссылка"), max_length=200, **NULLABLE)
    tags = models.ManyToManyField(ProjectTag)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_unique_slag(Project, self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectImage(models.Model):
    image = models.ImageField('Attachment', upload_to='img/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project representation')

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'