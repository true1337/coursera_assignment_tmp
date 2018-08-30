from django.conf.urls import url
from routing.views import simple_route, slug_route, sum_route, sum_get_method, sum_post_method
urlpatterns = [
    url(r'^simple_route/$', simple_route),
    url(r'^slug_route/(?P<slug>[a-zA-Z0-9_-]{1,16})/$', slug_route),
    url(r'^sum_route/(?P<number_1>-?\d+)/(?P<number_2>-?\d+)/$', sum_route),
    url(r'^sum_get_method/$', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method)
]
