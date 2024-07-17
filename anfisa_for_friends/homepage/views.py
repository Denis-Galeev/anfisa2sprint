# from django.db.models import Q
from django.shortcuts import render
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.select_related(
        'category'
    ).filter(
        # В точности то же самое:
        category__is_published=True
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
