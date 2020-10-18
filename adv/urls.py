from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from adv_datasets import views as dataset_views

router = DefaultRouter()
router.register(r'datasets', dataset_views.FetchedDatasetViewset, basename='datasets')
urlpatterns = router.urls

urlpatterns = [
    url(r'^api/', include(router.urls))
]
