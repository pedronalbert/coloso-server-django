from django.conf.urls import url
from django.contrib import admin
from summoner import views as summonerViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/by-name/(?P<summonerName>[\w\s]+)$', summonerViews.findByName),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)$', summonerViews.findById),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/runes$', summonerViews.getRunes),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/masteries$', summonerViews.getMasteries),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/stats/summary$', summonerViews.getStatsSummary),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/champions-mastery$', summonerViews.getChampionsMastery),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/games/recent$', summonerViews.getGamesRecent),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/games/current$', summonerViews.getGameCurrent),
    url(r'^riot-api/(?P<region>\w{1,4})/summoner/(?P<summonerId>\d+)/league/entry$', summonerViews.getLeagueEntry),
]
