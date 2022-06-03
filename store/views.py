from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q 
from django.views.generic import (
    ListView,
    DetailView,
)
from store.models import (
                            Product,
                            Store,
                            Department,
                            Category,
                            StoreProduct,
                            BannerItem,
                            StoreDetailItem,
                            StoreProductSaleItem,
                            FeaturedStoreProduct,
                            
                        )

# Create your views here.
def home(request):
    context = {}
    return render(request, 'new-store/index.html',context)

def store_home(request, store_slug):
    try:
        store = get_object_or_404(Store, slug=store_slug)
        main_banners = BannerItem.objects.filter(
            Q(store=store) &
            Q(isActive = True)
        )
        store_customer_promise = StoreDetailItem.objects.filter(
            Q(store = store) & 
            Q(store_detail_cat__name = 'customer-promise'),
            Q(isActive = True)
        )
        store_choose_us = StoreDetailItem.objects.filter(
            Q(store = store) & 
            Q(store_detail_cat__name = 'choose-us'),
            Q(isActive = True)
        )
        store_sale_products = StoreProductSaleItem.objects.filter(
            Q(store_product__store = store) &
            Q(isActive = True)
        )
        
        store_feat_products = FeaturedStoreProduct.objects.filter(
            Q(store_product__store = store) &
            Q(isActive = True)
        )
        print(store_feat_products)
         
    except Exception as e:
        raise e 
        store = None 
    context = {
        'store':store,
        'main_banners':main_banners,
        'store_customer_promise':store_customer_promise,
        'store_sale_products': store_sale_products,
        'store_choose_us':store_choose_us,
        'store_feat_products':store_feat_products
      
    }
    return render(request, 'store/store_home.html',context)

class DepartmentListView(ListView):
    model = Department
    #template_name = 'store/department_list.html'    #<app>/<model>_<viewtype>.html


def department_detail_view(request, dept_slug):
    try:
        department = get_object_or_404(Department, slug=dept_slug)
        categories = Category.objects.filter(
            Q(department=department)
        )
        store_products = StoreProduct.objects.filter(
            Q(product__category__in = categories.all())
        )
        #News.objects.filter(tag__id__in=news.tag.all())
    except Exception as e:
        raise e
        categories = None 
        store_products = None 
    context = {
        'department': department,
        'categories':categories,
        'store_products': store_products
    }
    print(categories)
    #print(store_products)
    return render(request, 'store/department_detail.html',context)
class CategoryListView(ListView):
    model = Category
    #template_name = 'store/department_list.html'    #<app>/<model>_<viewtype>.html


def category_detail_view(request, cat_slug):
    try:
        category = get_object_or_404(Category, slug=cat_slug)
        store_products = StoreProduct.objects.filter(
            Q(product__category = category)
        )
    except Exception as e:
        raise e 
        store_products = None 
    context = {'category': category, 'store_products':store_products}
    return render(request, 'store/category_detail.html',context)


class StoreProductListView(ListView):
    model = StoreProduct

    def get_queryset(self):
        self.store_slug = get_object_or_404(Store, slug = self.kwargs['store_slug'])
        return StoreProduct.objects.filter(
            Q(store = self.store_slug)
        )

class StoreProductDetailView(DetailView):
    model = StoreProduct

def about_us(request):
    context = {}
    return render(request, 'new-store/about-us.html',context)

def all_blog(request):
    context = {}
    return render(request, 'new-store/all-blog.html',context)

def all_product(request):
    context = {}
    return render(request, 'new-store/all-product.html',context)

def blog(request):
    context = {}
    return render(request, 'new-store/blog.html',context)

def cart(request):
    context = {}
    return render(request, 'new-store/cart.html',context)

def contact(request):
    context = {}
    return render(request, 'new-store/contact.html',context)

def crystal_directory(request):
    context = {}
    return render(request, 'new-store/crystal-directory.html',context)

def order_history(request):
    context = {}
    return render(request, 'new-store/order-history.html',context)

def single_blog(request):
    context = {}
    return render(request, 'new-store/single-blog.html',context)

def single_category(request):
    context = {}
    return render(request, 'new-store/single-category.html',context)

def single_product(request):
    context = {}
    return render(request, 'new-store/single-product.html',context)

def single_department(request):
    context = {}
    return render(request, 'new-store/single-department.html',context)


# TODO: stlying 
        # profile (users)
        # store login -> check login to see email is in store group --> change/reset password
        # blog (for store)
        # order
        # order_item
        # cart
        # cart_item
        # check-out




