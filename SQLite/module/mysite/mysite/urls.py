from django.conf.urls import include, url
from django.contrib import admin

#在当前文件夹下创建views.py文件并引用里面的函数。
#在引用的时候在views文件的前面一定要加上 点（.）,即表示当前路径。
from .views import here
from .views import plus
from .views import math
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', plus),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
]
