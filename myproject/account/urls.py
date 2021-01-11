from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('register', views.UserProfileViewSet, basename='hello-viewset')

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls)),
    path("post-create/", views.PostView.as_view()),
    path("post-list/", views.PostView.as_view()),
    path("post-delete/<int:pk>", views.PostView.as_view()),
    path("comment/", views.CommentView.as_view()),
]