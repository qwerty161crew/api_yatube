from django.urls import path, include
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='post')
router.register('v1/groups', GroupViewSet, basename='group')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
print(router.urls)


app_name = 'api'

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include((router.urls, 'api'), namespace='post')),
    path('', include((router.urls, 'api'), namespace='group')),
    path('', include((router.urls, 'api'), namespace='comment')),
]
