from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user import views


router = DefaultRouter()
router.register('user-profile', views.UserViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]