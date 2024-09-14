from django.urls import path
from .views import user_login, index, export_products_to_excel, import_products
urlpatterns = [
    path('', index, name='index'),
    path("login/", user_login, name="login"),
    path('export/products/', export_products_to_excel, name='export_products'),
    path('import/products/', import_products, name='import_products'),
]