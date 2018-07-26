from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^level1$', views.level1),
    url(r'^firstFlag$', views.firstFlag),
    url(r'^level2$', views.level2),
    url(r'^Hell$', views.Hell),
    url(r'^HellLogic$', views.HellLogic),
    url(r'^level3$', views.level3),
    url(r'^level3Logic$', views.level3Logic),
    url(r'^level4$', views.level4),
    url(r'^level4Logic$', views.level4Logic),
    url(r'^level5$', views.level5),
    url(r'^level5Logic$', views.level5Logic),
    url(r'^youWin$', views.youWin)
]
