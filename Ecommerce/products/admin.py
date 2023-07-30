import os

from django.contrib import admin
from django.shortcuts import get_object_or_404

from Ecommerce.core.s3 import s3
from Ecommerce.products.forms import ProductForm
from Ecommerce.products.models import Product, Category
from Ecommerce.settings import STATICFILES_DIRS
from Ecommerce.utils.admin_mixins import AdminPermissionMixin
from Ecommerce.utils.save_file import upload_photo


@admin.register(Product)
class ProductAdmin(AdminPermissionMixin, admin.ModelAdmin):
    add_form_template = 'admin/custom_product_add.html'
    ordering = ('name',)
    list_display = ('name', 'price', 'category', 'quantity')
    list_filter = ('price', 'brand', 'quantity', 'added_on')
    search_fields = ('name', 'brand', 'made_in', 'category')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'price', 'category', 'quantity')
        }),
        ('Additional Information', {
            'fields': ('image', 'description', 'made_in')
        }),
    )

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                data = form.cleaned_data

                photo_name = data['photo'].name
                path = os.path.join(STATICFILES_DIRS[0], photo_name)
                upload_photo(data['photo'], path)
                image_url = s3.upload(path, photo_name)
                os.remove(path)

                del data['photo']
                product = form.save()

                product.image = image_url
                product.save()

                return self.response_add(request, product)

        else:
            form = ProductForm()

        context = {
            'form': form
        }
        return super().add_view(request, form_url=form_url, extra_context=context)

    def delete_model(self, request, obj):
        path = obj.image.split('/')[3]
        a = s3.delete(path)

        super().delete_model(request, obj)


@admin.register(Category)
class CategoryAdmin(AdminPermissionMixin, admin.ModelAdmin):
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)



