from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Listing
from .choices import state_choices, bedroom_choices, price_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_listings = paginator.get_page(page_number)

    context = {'listings': page_listings,}
    return render(request,'listings/index.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    context = {'listing':listing,}
    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords: 
            queryset_list = queryset_list.filter(description__icontains = keywords)
    
    if 'city' in request.GET:
        keywords = request.GET['city']
        if keywords:
            queryset_list = queryset_list.filter(city__iexact = keywords)

    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            queryset_list = queryset_list.filter(state__iexact = keywords)
    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']
        if keywords:
            queryset_list = queryset_list.filter(bedrooms__lte = keywords)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)

    print(request.GET)
    context = {'state_choices': state_choices, 'price_choices': price_choices, 'bedroom_choices': bedroom_choices, 'listings':queryset_list, 'values': request.GET}
    return render(request, 'listings/search.html', context)