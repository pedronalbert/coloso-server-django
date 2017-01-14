from django.http import JsonResponse
from riot_api import RiotApi
from exceptions import NotFoundException, RiotServerError

# Create your views here.

def findByName(request, region, summonerName):
    riotApi = RiotApi(region)

    try:
        summonerData = riotApi.getSummonerByName(summonerName)
        return JsonResponse(summonerData)
    except NotFoundException as e:
        return JsonResponse({ 'message': e.message }, status=404)
    except RiotServerError as e:
        return JsonResponse({ 'message': e.message }, status=500)

def findById(request, region, summonerId):
    riotApi = RiotApi(region)

    try:
        summonerData = riotApi.getSummonerById(summonerId)
        return JsonResponse(summonerData)
    except NotFoundException as e:
        return JsonResponse({ 'message': e.message }, status=404)
    except RiotServerError as e:
        return JsonResponse({ 'message': e.message }, status=500)

def getRunes(request, region, summonerId):
    riotApi = RiotApi(region)

    try:
        runesData = riotApi.getSummonerRunes(summonerId)
        return JsonResponse(runesData)
    except NotFoundException as e:
        return JsonResponse({ 'message': e.message }, status=404)
    except RiotServerError as e:
        return JsonResponse({ 'message': e.message }, status=500)

def getMasteries(request, region, summonerId):
    riotApi = RiotApi(region)

    try:
        masteries = riotApi.getSummonerMasteries(summonerId)
        return JsonResponse(masteries)
    except NotFoundException as e:
        return JsonResponse({ 'message': e.message }, status=404)
    except RiotServerError as e:
        return JsonResponse({ 'message': e.message }, status=500)

def getStatsSummary(request, region, summonerId):
    riotApi = RiotApi(region)
    season = request.GET.get('season', 'SEASON2017')

    try:
        stats = riotApi.getSummonerStatsSummary(summonerId, season)
        return JsonResponse(stats)
    except RiotServerError as e:
        return JsonResponse({ 'message': e.message }, status=500)

def getChampionsMastery(request, region, summonerId):
    riotApi = RiotApi(region)

    try:
        masteries = riotApi.getSummonerChampionsMastery(summonerId)
        return JsonResponse(masteries)
    except RiotServerError as e:
        return JsonResponse({ 'message': e.message }, status=500)
