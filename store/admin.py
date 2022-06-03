from django.contrib import admin
from store.models import(
    Zipcode,
    Industry, 
    Store,
    Department,
    Category,
    Brand,
    #Color,
    #HealingCategory,
    #HealingProperty,
    Product,
    StoreProduct,
    FeaturedStoreProduct,
    StoreProductSaleCategory,
    StoreProductSaleItem,
    StoreDetailCategory,
    StoreDetailItem,
    SocialMediaCategory,
    SocialMediaItem,
    BannerCategory,
    BannerItem,
)


class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'city', 'state', 'county','is_active']
    list_editable = ['county','is_active']
    list_per_page = 10

admin.site.register(Zipcode, ZipcodeAdmin)

class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    list_editable = []
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Industry, IndustryAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'email','phone','zipcode','industry','is_active']
    list_editable = ['email','phone','zipcode','industry','is_active']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Store, StoreAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Department, DepartmentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image','department','is_active']
    list_editable = ['department','is_active']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'email','phone','is_active']
    list_editable = ['email','phone','is_active']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','image','description','brand','category','is_active']
    list_editable = ['description','brand','category','is_active']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Product, ProductAdmin)

class StoreProductAdmin(admin.ModelAdmin):
    list_display = ['store','product','price','stock','available','digital','created_on','updated']
    list_editable = ['price','stock','available','digital']
    list_per_page = 10

admin.site.register(StoreProduct, StoreProductAdmin)

# register other models
admin.site.register(BannerCategory)
admin.site.register(BannerItem)
admin.site.register(StoreDetailCategory)
admin.site.register(StoreDetailItem)
admin.site.register(StoreProductSaleCategory)
admin.site.register(StoreProductSaleItem)
admin.site.register(FeaturedStoreProduct)