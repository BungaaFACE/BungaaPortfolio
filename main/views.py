from django.shortcuts import render
from main.models import Experience, SkillCategory


def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def resume(request):
    experience = Experience.objects.all().order_by('-date_start')
    return render(request, 'main/resume.html', context={'experience': experience})

def skills(request):
    context_data = dict()
    for category in SkillCategory.objects.all():
        context_data[category.name] = list(category.skill_set.all())

    return render(request, 'main/skills.html', context={'context': context_data})
