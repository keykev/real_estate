from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            
            has_contacted = Contact.objects.filter(listing_id = listing_id, user_id = user_id)

            if has_contacted:
                messages.error(request,'Inquiry of this property has already been made.')
                return redirect('/listings/'+listing_id)

        contact = Contact.objects.create(listing = listing, listing_id = listing_id, name = name, email = email, phone = phone, message = message, user_id = user_id)

        contact.save()

        send_mail('You have an inquiry on a property','Please call me back at xxx-xxx-xxxx for more information on this inquiry.','kevinyang519@gmail.com',['phyang018@gmail.com'])

        return redirect('/listings/'+ listing_id)