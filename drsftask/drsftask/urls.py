from django.conf.urls import patterns, include, url

from django.contrib import admin

from rest_framework import routers

from todo.views import TodoViewSet, UserListApiView, UserDetailView

admin.autodiscover()

router = routers.DefaultRouter()
router.register('todos', TodoViewSet, 'todo')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drsf_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', UserListApiView.as_view()),
    url(r'^users/(?P<username>\w+)/$', UserDetailView.as_view()),
    url(r'^', include(router.urls))
)
