from django.urls import path, include
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/v1/posts/', PostViewSet, basename='post') 
router.register('api/v1/groups/', GroupViewSet, basename='group')
router.register('api/v1/posts/<int:post_id>/comments/', CommentViewSet, basename='comment')


app_name = 'api'

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include((router.urls, 'api'), namespace='post')),
    path('', include((router.urls, 'api'), namespace='group')),
    path('', include((router.urls, 'api'), namespace='comment')),
]
