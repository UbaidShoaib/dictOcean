from django.urls import path
from .views import index, inner_page, portfolio_details, contact_view

urlpatterns = [
    path('', index, name='index'),
    path('inner_page', inner_page,name='inner_page'),
    path('portfolio_details', portfolio_details, name='portfolio_details'),
    path('contact/', contact_view, name='contact'),
]
