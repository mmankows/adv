from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'accounts', backend_views.AccountsViewSet, basename='accounts')
urlpatterns = router.urls

root_urlpatterns = [
#    path('admin/', admin.site.urls),
]

urlpatterns = [url(r'^api/v1/', include(router.urls))] + root_urlpatterns
