from django.conf.urls import url,include
from .views import HelloAPIView,HelloViewset,PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('hello-viewset',HelloViewset,base_name = "hello-viewset")
router.register('polls-viewset',PollViewSet,base_name = "polls-viewset")

urlpatterns = [
    url(r'^hello-view/',HelloAPIView.as_view()),
    url(r'',include(router.urls)),
    # url(r'',include(router.urls))
]
