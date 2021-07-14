from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import price_choices, bedroom_choices , bathroom_choices, city_choices, state_choices

# Create your views here.
def index(request):
    listings=Listing.objects.all()
    contt={'listings':listings}
    return render(request, 'listings/listings.html', contt)
def listing(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id)
    contt={'listing':listing}
    return render(request, 'listings/listing.html', contt)
def search(request):
    query_list = Listing.objects.order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        query_list = query_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        query_list = query_list.filter(city__iexact=city)

     #state
    if 'state' in request.GET:
        state = request.GET['state']
        query_list = query_list.filter(state__iexact=state)

    # price
    if 'price' in request.GET:
         price = request.GET['price']
         query_list = query_list.filter(price__lte=price)

    contt={'listings': query_list,
           'price_choices':price_choices,
           'bedroom_choices':bedroom_choices,
           'bathroom_choices': bathroom_choices,
           'city_choices': city_choices,
           'state_choices': state_choices}
    return render(request, 'listings/search.html', contt)