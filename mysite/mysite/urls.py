from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cards/', include('cards.urls', namespace="cards")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
