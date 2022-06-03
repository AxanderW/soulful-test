from django.db import models
from django.urls import reverse

# Create your models here.
class Zipcode(models.Model):
    zip_code = models.CharField(max_length=20, unique=True, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=5, null=False, blank=False)
    county =  models.CharField(max_length=255, default='unknown')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('state',)
    def __str__(self) -> str:
        return f'Zipcode({self.zip_code}, {self.city}, {self.state}, {self.county})'

class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False )
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='industry',
            default = 'images/soulful_logo.png'
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'industry'
        verbose_name_plural = 'industries'

    def __str__(self) -> str:
        return self.name 

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False )
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='store',
            default = 'images/soulful_logo.png'
    )
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=12,null=True, blank=True)
    zipcode = models.ForeignKey(
        Zipcode,
        on_delete=models.SET_NULL,
        related_name= 'zipcode_stores',
        null = True,
        blank = True

    )
    industry = models.ForeignKey(
        Industry,
        on_delete=models.SET_NULL,
        related_name= 'industry_stores',
        null = True,
        blank = True

    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name 



class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False )
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='department',
            default = 'images/soulful_logo.png'
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name 

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'dept_slug':self.slug})

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False )
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='category',
            default = 'images/soulful_logo.png'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        related_name= 'department_categories',
        null = True,
        blank = True

    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name 

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'cat_slug':self.slug})


# TODO: add products and store products
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False )
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='brand',
            default = 'images/soulful_logo.png'
    )
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=12,null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name 


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False )
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='product',
            default = 'images/soulful_logo.png'
    )
    description = models.TextField()
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name= 'brand_products',
        null = True,
        blank = True

    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name= 'category_products',
        null = True,
        blank = True

    )
   
    healing_properties = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name 


class StoreProduct(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        null = False,
        blank = False

    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null = False,
        blank = False

    )
    description = models.TextField(null=True, blank=True)
    image_main = models.ImageField(upload_to='images/featured_products',
            default = 'images/soulful_logo.png'
    )
    image_2 = models.ImageField(upload_to='store_product/images/featured_products',
            null=True, blank = True
    )
    image_3 = models.ImageField(upload_to='store_product/images/featured_products',
            null=True, blank = True
    )
    image_4 = models.ImageField(upload_to='store_product/images/featured_products',
            null=True, blank = True
    )
    image_5 = models.ImageField(upload_to='store_product/images/featured_products',
            null=True, blank = True
    )
    image_6 = models.ImageField(upload_to='store_product/images/featured_products',
            null=True, blank = True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    digital = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 


    class Meta:
        ordering = ('product','store' )

    def __str__(self) -> str:
        return f'{self.product.name, self.store.name}' 


    def get_absolute_url(self):
        print(self.product.slug)
        return reverse('store-product-detail', kwargs={'pk':self.product.pk})

class FeaturedStoreProduct(models.Model):
    store_product = models.ForeignKey(StoreProduct,on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.store_product.product.name 

class StoreProductSaleCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    label = models.CharField(max_length=250, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 


    class Meta:
        ordering = ('name',)
        verbose_name = 'store_product_sale_category'
        verbose_name_plural = 'store_product_sale_categories'


    def __str__(self):
        return f'{self.slug}'

class StoreProductSaleItem(models.Model):
    sale_cat = models.ForeignKey(StoreProductSaleCategory,on_delete=models.CASCADE, blank=False, null=False)
    store_product = models.ForeignKey(StoreProduct,on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.store_product.product.name 

class StoreDetailCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 


    class Meta:
        ordering = ('name',)
        verbose_name = 'storedetailcategory'
        verbose_name_plural = 'storedetailcategories'


    def __str__(self):
        return f'{self.slug}'

class StoreDetailItem(models.Model):
    store_detail_cat = models.ForeignKey(StoreDetailCategory,on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=250, default='store_detail_generic')
    icon = models.ImageField(upload_to='store_detail/icon', default='images/soulful_logo.png')
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        null = False,
        blank = False

    )
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.name


class SocialMediaCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    icon = models.ImageField(upload_to='social_media/icon', default='images/soulful_logo.png')
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True) 


    class Meta:
        ordering = ('name',)
        verbose_name = 'socialmediacategory'
        verbose_name_plural = 'socialmediacategories'


    def __str__(self):
        return f'{self.slug}'

class SocialMediaItem(models.Model):
    social_media_cat = models.ForeignKey(SocialMediaCategory,on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=250, default='social_media_item_generic')
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        null = False,
        blank = False

    )
    handle_name = models.CharField(max_length=250)
    handle_url = models.CharField(max_length=250)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name 

class BannerCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'bannercategory'
        verbose_name_plural = 'bannercategories'


    def __str__(self):
        return f'{self.slug}'

class BannerItem(models.Model):
    banner_cat = models.ForeignKey(BannerCategory,on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, default='banner_generic')
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        null = False,
        blank = False

    )
    image = models.ImageField(upload_to='banners', default='images/soulful_logo.png')
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name 
   