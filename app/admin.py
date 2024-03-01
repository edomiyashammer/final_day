from django.contrib import admin
from app.models import Category, Product, UserProfile, Review, Subcategory



class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price")
    list_filter = ("category",)
    search_fields = ("title",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)



class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating")
    list_filter = ("product", "rating")
    search_fields = ("product__title", "user__username")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Subcategory)
