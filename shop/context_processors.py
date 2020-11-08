from .models import Category, Cart, CartItem

from .views import _cart_id
# Context processor - ф-ція, яка приймає один аргумент й повертає словник
# Повернений словник буде доступним в любому місці коду.


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0

    return {'item_count': item_count}


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


