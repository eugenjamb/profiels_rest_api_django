from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name='hello-viewset')
router.register('profile', views.UserProfileVewSet, base_name='profile')
router.register('login', views.LoginVewSet, base_name='login')
router.register('feed', views.UserProfileFeedItem)


urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]