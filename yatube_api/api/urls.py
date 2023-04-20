from django.urls import path
from rest_framework.authtoken import views

app_name = 'api'

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/'),
    path('api/v1/posts/<int:post_id>/'),
    path('api/v1/groups/'),
    path('api/v1/groups/<int:group_id>/'),
    path('api/v1/posts/<int:post_id>/comments/'),
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/')
]
