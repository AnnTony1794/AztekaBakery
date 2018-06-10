from django.urls import path
from .views import HomeView, ContactView, AboutView, StoreView, SampleView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('contact/', ContactView.as_view(),name='Contact'),
    path('about/', AboutView.as_view(), name='About'),
    path('store/', StoreView.as_view(), name='Store'),
    path('sample/', SampleView.as_view(), name='Sample')
]