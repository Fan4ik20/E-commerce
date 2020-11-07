from .models import Category

# Context processor - ф-ція, яка приймає один аргумент й повертає словник
# Повернений словник буде доступним в любому місці коду.


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
