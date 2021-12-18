from django.shortcuts import render
from .models import Product , Cart , Order,CancelOrder , Category
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse , JsonResponse
from django.db.models import Avg, Count, Min,Max,Sum,F , Q
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
from django.views.generic import ListView


# Create your views here.
# shop page
def shoppage(request):
    ctx={}
    ctx['title'] = 'SHOP'
    ctx['description'] = 'shop_PAGE_DESCRIPTION'
    products=Product.objects.all().filter(active=True).order_by('-id')
    ctx['category_list'] = Category.objects.all()
    p = Paginator(products, 50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    ctx['products']=page_obj
    pagelist=[]
    for num in range(1,p.num_pages+1):
        pagelist.append(num)
    ctx['pages']=pagelist
    return render(request, 'storefront/shop.html',ctx)
    
# account page
@login_required
def accountpage(request):
    ctx={}
    ctx['cart'] = Cart.objects.all().filter(customer=request.user,ordered=True).filter(~Q(status='Cancel'))
    return render(request, 'shop/account.html',ctx)


# cancel order page
@login_required
def cancelorderpage(request):
    ctx={}
    if request.method =='POST':
        orderid=request.POST.get('orderid',False)    
        msg=request.POST.get('msg',False)
        b = CancelOrder(oid=orderid,message=msg,user=request.user)
        b.save()
        ctx['msg']='Your request has been sent.'
    ctx['cart'] = Cart.objects.all().filter(customer=request.user,ordered=True,status='Cancel')
    return render(request, 'shop/cancelorder.html',ctx)




# cart page
@login_required
def cartpage(request):
    ctx={}
    ctx['title'] = 'Cart'
    ctx['cart'] = Cart.objects.all().filter(customer=request.user,ordered=False)
    carttotal= Cart.objects.all().filter(customer=request.user,ordered=False).select_related().aggregate(total=Sum(F('product__price')*F('quantity')))
    ctx['carttotal'] = carttotal['total']
    return render(request, 'shop/cart.html',ctx)

# add to cart
@login_required
def addtocart(request):
    ctx = {}
    if request.method == "POST":
        productid=request.POST.get('productid',False)
        productobj=Product.objects.get(id=productid)
        userid = request.user
        msg = Cart.objects.get_or_create(customer=userid,product=productobj,ordered=False)    
        if msg[1]:
            ctx['msg1'] = "Added to cart"
            ctx['name']=productobj.name
            ctx['status']="success"
        else:
            ctx['msg1'] = "Already in cart"
            ctx['name']=productobj.name
            ctx["status"]="error"
        return JsonResponse(ctx)

# delete from cart
@login_required
def deletefromcart(request):
    ctx = {}
    if request.method == "POST":
        cartid=request.POST.get('cartid',False)
        userid = request.user
        msg=Cart.objects.filter(id=cartid).delete()
        if(msg[0]==1):
            ctx['msg1'] = "Product removed from cart"
            ctx['status']="success"
            return JsonResponse(ctx)
        

# update cart
@login_required
def updatecart(request):
    ctx={}
    if request.method == "POST":
        cart = request.POST
        for item,count in cart.items():
            # print(item+":"+count)
            msg =Cart.objects.filter(id=item).update(quantity=count)
        if(msg==1):
            ctx['msg1'] = "Cart Updated"
            ctx['status']="success"
            return JsonResponse(ctx)
        
# checkout page
@login_required
def checkoutpage(request):
    ctx={}
    ctx['title'] = 'Checkout'
    ctx['cart'] = Cart.objects.all().filter(customer=request.user,ordered=False)
    carttotal= Cart.objects.all().filter(customer=request.user,ordered=False).select_related().aggregate(total=Sum(F('product__price')*F('quantity')))
    ctx['carttotal'] = carttotal['total']
    if request.method =='GET':
        ctx['msg1'] = ""
    else:
        first_name=request.POST.get('firstname',False)    
        last_name=request.POST.get('lastname',False)    
        mail=request.POST.get('email',False)    
        mob=request.POST.get('mobile',False)    
        addr=request.POST.get('address',False)    
        nation=request.POST.get('country',False)    
        area=request.POST.get('state',False)    
        zip=request.POST.get('zipcode',False)    
        payment_type=request.POST.get('paymenttype',False)
        carttotal= Cart.objects.all().filter(customer=request.user,ordered=False).select_related().aggregate(total=Sum(F('product__price')*F('quantity')))['total']        
        msg=Order.objects.get_or_create(customer=request.user,firstname=first_name,lastname=last_name,email=mail,mobile=mob,address=addr,country=nation,state=area,zipcode=zip,paymenttype=payment_type,Total=carttotal)
        if msg[1]:
            ctx['msg1'] = "Order is placed"
            ctx['status']="success"
        else:
            ctx['msg1'] = "Something went wrong! Try after few minutes"
            ctx["status"]="error"
    return render(request, 'shop/checkout.html',ctx)

# search result
class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get('search')
        if query is not None:
            object_list=Product.objects.filter( Q(name__icontains=query))
        else:
            object_list = []
        return object_list

# product detail page
class ProductDetail(DetailView):
    model=Product
    