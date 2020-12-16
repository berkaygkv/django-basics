from django.shortcuts import render

from .models import Restaurant
# Create your views here.

def restaurant_detail_view(request):
    objs = Restaurant.objects.all().values()
    cols = list(objs[15].keys())
    vals = list(Restaurant.objects.values_list())
    context = {
        'columns': cols,
        'values': vals
    }
    return render(request, 'resties/detail.html', context)