from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import account.views

@login_required
def registration_count(request):
    admin = request.user.is_staff
    if not admin:
        return redirect("dashboard")

    from plata.shop.models import Order, OrderItem
    from simple_shop.models import Product
    import codecs

    CO = Product.objects.filter(name__contains=u'Conference Track')
    TU_A = Product.objects.filter(name__contains=u'Advanced Tutorials')
    TU_B = Product.objects.filter(name__contains=u'Beginner Tutorials')

    all_o = Order.objects.all()

    co_n = 0
    tu_a_n = 0
    tu_b_n = 0

    all_u = set()

    for o in all_o:
        if o.status != 40:
            continue
        for i in o.items.all():
            if i.product in CO:
                co_n += i.quantity
            elif i.product in TU_A:
                tu_a_n += i.quantity
            elif i.product in TU_B:
                tu_b_n += i.quantity
        all_u.add(o.user)

    msg = """Adv. Tutorials Registration : %i
Beg. Tutorials Registration : %i
Conference Registration     : %i
Unique users                : %i
""" % (tu_a_n, tu_b_n, co_n, len(all_u))
 

    ctx = {
        "msg": msg,
    }

    return render(request, "registration_count.html", ctx)
