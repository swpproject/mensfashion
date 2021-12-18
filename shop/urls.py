from django.urls import path,include
from .views import shoppage , ProductDetail,accountpage , cartpage , addtocart , deletefromcart , updatecart,checkoutpage,SearchResultsView , cancelorderpage
urlpatterns = [
    path('',shoppage, name="shop"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('account/',accountpage, name="accountpage"),    
    path('cancelorder/',cancelorderpage, name="cancelorderpage"),    
    path('cart/',cartpage, name="cartpage"),
    path('addtocart/',addtocart,name="addtocart"),    
    path('deletefromcart/',deletefromcart,name="deletefromcart"),    
    path('updatecart/',updatecart,name="updatecart"),    
    path('checkout/',checkoutpage,name="checkout"),    
    path('<slug:slug>/',ProductDetail.as_view(), name="productdetail"),    
]