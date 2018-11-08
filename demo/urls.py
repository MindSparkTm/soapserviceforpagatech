from . import views
from django.conf.urls import url, include

urlpatterns = ()
urlpatterns += (

    url(r'^integration_service/', views.get_integration_services),
)
