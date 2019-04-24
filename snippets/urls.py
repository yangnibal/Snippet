from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
'''
from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers, routers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'particle_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', snippet_list, name='snipped-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snipped-detail'),
    path('users/', user_list, name='snipped-highlight'),
    path('users/<int:pk>', user_detail, name='user-list'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='user-detail'),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
'''

