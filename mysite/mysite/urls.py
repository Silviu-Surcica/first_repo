from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from .api import UserViewSet
from polls.api import QuestionViewSet,ChoiseViewSet
from cards.api import CardViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions',QuestionViewSet)
router.register(r'choises',ChoiseViewSet)
router.register(r'cards',CardViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cards/', include('cards.urls', namespace="cards")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
