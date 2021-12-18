from django.contrib import admin
from .models import Product,Category,Order,Cart,CancelOrder
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ProductAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','category','price','active','feature']
    list_editable =['active','feature']
    summernote_fields = ('description','specifications')
    readonly_fields=('slug',)
    search_fields = ('name','category',)
    list_per_page = 10

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('slug',)
    list_display=['id','name','slug',]

admin.site.register(Category,CategoryAdmin)


class CartInline(admin.TabularInline):
    model = Cart
    readonly_fields = ('customer','product','quantity','ordered')
    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 0
        return max_num
    def has_delete_permission(self, request, obj=None):
        return False

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','Total']
    inlines = [CartInline,]

admin.site.register(Order,OrderAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display=['id','customer','product','quantity','order','ordered','status']
    list_editable=['ordered']
    search_fields=['id']
    

admin.site.register(Cart,CartAdmin)


admin.site.register(CancelOrder)