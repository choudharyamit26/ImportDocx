from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ImportDocx

app_name = 'src'

urlpatterns = [
    path('',ImportDocx.as_view(),name='import')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
