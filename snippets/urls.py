from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snipped-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snipped-detail'),
    path('users/', views.UserList.as_view(), name='snipped-highlight'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-list'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='user-detail'),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

