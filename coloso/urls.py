from django.conf.urls import url
from django.contrib import admin
from summoner import views as summonerViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/by-name/(?P<summonerName>[\w\s]+)$', summonerViews.findByName),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)$', summonerViews.findById),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/runes$', summonerViews.getRunes),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/masteries$', summonerViews.getMasteries),
]
