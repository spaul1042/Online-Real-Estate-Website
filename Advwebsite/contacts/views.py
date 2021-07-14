from django.shortcuts import render, redirect
from django.contrib import messages
from.models import Contacts
from listings.models import Listing

def contact(request):
    if request.method =='POST':
        listing_title=request.POST['listing_title']
        listing_id = request.POST['listing_id']
        userid=request.POST['user_id']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        if request.user.is_authenticated:
            has_inquired = Contacts.objects.filter(listing_id=listing_id, user_id=userid)
            if has_inquired:
                messages.error(request, "You have already inquired for the given listing ")
                return redirect( "accounts:dashboard")
            else:
                contact=Contacts(listing_title=listing_title, listing_id=listing_id, user_id=userid,
                                 name=name, phone=phone,email=email,
                                 message=message)
                contact.save()
                return redirect("accounts:dashboard")
        else:
            contact = Contacts(listing_title=listing_title, listing_id=listing_id, user_id=userid,
                               name=name, phone=phone, email=email,
                               message=message)
            contact.save()
            listings=Listing.objects.all()
            contt={'listings' : listings}
            return render(request,"listings/listings.html", contt )


