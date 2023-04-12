from django.shortcuts import render, redirect

from item.models import Category, Item
from core.models import CartItem
from django.contrib import messages

from django.contrib.auth import logout


from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {'cart_items': cart_items}
    return render(request, 'core/cart.html', context)


def add_to_cart(request, item_pk):
    item = Item.objects.get(id=item_pk)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        item=item,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart')


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    messages.info(request, 'Your password has been changed successfully!')
    return redirect('/')
