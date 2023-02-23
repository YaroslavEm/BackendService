from django.urls import path

from . import views

urlpatterns = [
    path('wiki/', views.home_view, name='home'),
    path('wiki/<slug:title>', views.ArticleViewSet.as_view({'get': 'list', 'put': 'update'}), name='article'),
]
