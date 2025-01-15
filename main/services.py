from django.utils.text import slugify

def get_unique_slag(model, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{origin_slug}-{numb}'
        numb += 1
    return unique_slug