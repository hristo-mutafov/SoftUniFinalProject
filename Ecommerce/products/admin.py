import os

from django.contrib import admin

from Ecommerce.core.s3 import s3
from Ecommerce.products.forms import ProductForm
from Ecommerce.products.models import Product, Category
from Ecommerce.settings import STATICFILES_DIRS
from Ecommerce.utils.admin_mixins import AdminPermissionMixin
from Ecommerce.utils.save_file import upload_photo


@admin.register(Product)
class ProductAdmin(AdminPermissionMixin, admin.ModelAdmin):
    add_form_template = 'admin/custom_product_add.html'

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                data = form.cleaned_data

                photo_name = data['photo'].name
                path = os.path.join(STATICFILES_DIRS[0], photo_name) # Get the full path to the file
                upload_photo(data['photo'], path)  # Get that file in that folder location
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


@admin.register(Category)
class CategoryAdmin(AdminPermissionMixin, admin.ModelAdmin):
    pass



