from django.urls import path
from .views import BlogView, CategoryView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='Blog'),
    path('category/<int:pk>/<slug:title>', CategoryView.as_view(), name='Category')
]