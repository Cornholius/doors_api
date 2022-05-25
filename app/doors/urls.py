from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Company', views.CompanyViewSet)
router.register(r'Collection', views.CollectionViewSet)
router.register(r'Doors', views.DoorsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('delete/<type>/<id>/', views.DeleteItemView.as_view(), name='delete'),
]
