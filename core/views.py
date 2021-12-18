from django.shortcuts import render
from shop.models import Product
from .models import Contact
# Create your views here.

def homepage(request):
    ctx={}
    ctx['title'] = 'HOME'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['products']=Product.objects.all().filter(feature=True,active=True)[:15]    
    return render(request, 'storefront/index.html',ctx)


def aboutpage(request):
    ctx={}
    ctx['title'] = 'ABOUT'
    ctx['description'] = 'About_PAGE_DESCRIPTION'
    return render(request, 'storefront/about.html',ctx)


def contactpage(request):
    ctx={}
    ctx['title'] = 'CONTACT'
    ctx['description'] = 'Contact_PAGE_DESCRIPTION'
    if request.method =='POST':
        mail=request.POST.get('email',False)    
        msg=request.POST.get('msg',False)
        b = Contact(email=mail,message=msg)
        b.save()
        ctx['msg']='Your message has been sent.'
    return render(request, 'storefront/contact.html',ctx)