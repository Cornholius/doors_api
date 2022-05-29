from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'collection', views.CollectionViewSet)
router.register(r'doors', views.DoorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete/<type>/<id>/', views.DeleteItemView.as_view(), name='delete'),
]
