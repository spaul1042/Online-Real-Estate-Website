from django.shortcuts import render, HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices , bathroom_choices, city_choices, state_choices


def index(request):
    listingslt=Listing.objects.order_by('-list_date').filter(is_published=True)
    contt={'listingslt':listingslt,
           'price_choices':price_choices,
           'bedroom_choices':bedroom_choices,
           'bathroom_choices': bathroom_choices,
           'city_choices': city_choices,
           'state_choices': state_choices}
    return render(request, 'pages/index.html', contt)

def about(request):
    realtors=Realtor.objects.all().order_by('-hire_date')
    contt={'realtors':realtors}
    return render(request, 'pages/about.html', contt)
