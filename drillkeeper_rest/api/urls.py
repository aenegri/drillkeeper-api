from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShowView, SetView

urlpatterns = {
    url(r'^shows/$', ShowView.as_view(), name="create"),
    url(r'^sets/$', SetView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
}

urlpatterns = format_suffix_patterns(urlpatterns)