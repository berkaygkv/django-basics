from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Restaurant
from django.core.cache import cache


# Create your views here.

def restaurant_detail_view(request):
    query_obj = request.POST.get('textfield', cache.get('last_q_country',''))
    cache.set('last_q_country', query_obj)
    unique_countries = Restaurant.objects.order_by().values_list('Country', flat=True).distinct()
    vals = Restaurant.objects.filter(Country=query_obj).values_list()
    cols = ''
    if vals:
        cols = [f.name for f in Restaurant._meta.get_fields()]
    page = request.GET.get('page', 1)
    paginator = Paginator(vals, 50)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'columns': cols,
        'values': users,
        'options':unique_countries
    }
    # cache.set('last_query', users)
    return render(request, 'resties/detail.html', context)





