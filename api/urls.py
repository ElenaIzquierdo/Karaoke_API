from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='VoluntariApp API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include('music.urls')),
    url(r'^docs/', schema_view),
]