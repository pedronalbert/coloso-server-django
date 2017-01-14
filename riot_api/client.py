import requests
from django.conf import settings
from pydash.arrays import find_index
from exceptions import NotFoundException, RiotServerError

API_KEY = settings.RIOT_API_KEY

def regionToPlatform(region):
    if region == 'br':
        return 'br1'
    elif region == 'eune':
        return 'eun1'
    elif region == 'euw':
        return 'euw1'
    elif region == 'jp':
        return 'jp1'
    elif region == 'kr':
        return 'kr'
    elif region == 'lan':
        return 'la1'
    elif region == 'las':
        return 'la2'
    elif region == 'na':
        return 'na1'
    elif region == 'oce':
        return 'oc1'
    elif region == 'ru':
        return 'ru'

def fetchSummonerByName(region, summonerName):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/by-name/' + summonerName
    response = requests.get(url, params={'api_key': API_KEY})

    if response.status_code == 200:
        jsonResponse = response.json()
        sumNameKey = list(jsonResponse.keys())[0]
        jsonResponse = jsonResponse[sumNameKey]
        jsonResponse['region'] = region

        return jsonResponse
    elif response.status_code == 404:
        raise NotFoundException('Invocador no encontrado')
    else:
        raise RiotServerError

def fetchSummonerById(region, summonerId):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/' + summonerId
    response = requests.get(url, params={'api_key': API_KEY})

    if response.status_code == 200:
        jsonResponse = response.json()
        jsonResponse = jsonResponse[summonerId]
        jsonResponse['region'] = region

        return jsonResponse
    elif response.status_code == 404:
        raise NotFoundException('Invocador no encontrado')
    else:
        raise RiotServerError

def fetchSummonerRunes(region, summonerId):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/' + summonerId + '/runes'
    response = requests.get(url, params={'api_key': API_KEY})

    if response.status_code == 200:
        groupPages = []
        jsonResponse = response.json()
        jsonResponse = jsonResponse[summonerId]
        jsonResponse['region'] = region

        for page in jsonResponse['pages']:
            groupRunes = []

            for slot in page['slots']:
                runeIndexInGrouped = find_index(groupRunes, lambda rune: rune['runeId'] == slot['runeId'])

                if runeIndexInGrouped >= 0:
                    groupRunes[runeIndexInGrouped]['count'] += 1
                else:
                    groupRunes.append({ 'runeId': slot['runeId'], 'count': 1})

            groupPages.append(groupRunes)

        return {
            'summonerId': summonerId,
            'region': region,
            'pages': groupPages,
        }
    elif response.status_code == 404:
      raise NotFoundException('Invocador no encontrado')
    else:
      raise RiotServerError

def fetchSummonerMasteries(region, summonerId):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/' + summonerId + '/masteries'
    response = requests.get(url, params={'api_key': API_KEY})

    if response.status_code == 200:
        jsonResponse = response.json()
        jsonResponse = jsonResponse[summonerId]
        jsonResponse['region'] = region

        return jsonResponse
    elif response.status_code == 404:
        raise NotFoundException('Maestrias no encontradas')
    else:
        raise RiotServerError

def fetchSummonerStatsSummary(region, summonerId, season):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.3/stats/by-summoner/' + summonerId + '/summary'
    response = requests.get(url, params={'api_key': API_KEY, 'season': season})

    if response.status_code == 200:
        jsonResponse = response.json()

        return {
            'summonerId': summonerId,
            'region': region,
            'season': season,
            'playerStatSummaries': jsonResponse['playerStatSummaries'],
        }
    elif response.status_code == 404:
        return {
            'summonerId': summonerId,
            'region': region,
            'season': season,
            'playerStatSummaries': [],
        }
    else:
        raise RiotServerError

def fetchSummonerChampionsMastery(region, summonerId):
    url = 'https://' + region + '.api.pvp.net/championmastery/location/' + regionToPlatform(region) + '/player/' + summonerId + '/topchampions'
    response = requests.get(url, params={'api_key': API_KEY, 'count': 200})

    if response.status_code == 200:
        jsonResponse = response.json()

        return {
            'summonerId': summonerId,
            'region': region,
            'masteries': jsonResponse,
        }
    elif response.status_code == 404:
        return {
            'summonerId': summonerId,
            'region': region,
            'masteries': [],
        }
    else:
        raise RiotServerError

def fetchSummonerGamesRecent(region, summonerId):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.3/game/by-summoner/' + summonerId + '/recent'
    response = requests.get(url, params={'api_key': API_KEY})

    if response.status_code == 200:
        jsonResponse = response.json()
        jsonResponse['region'] = region

        return jsonResponse
    elif response.status_code == 404:
        raise NotFoundException('Games recent not found')
    else:
        raise RiotServerError

def fetchSummonerLeagueEntry(region, summonerId):
    url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v2.5/league/by-summoner/' + summonerId + '/entry'
    response = requests.get(url, params={'api_key': API_KEY})

    if response.status_code == 200:
        jsonResponse = response.json()

        return {
            'summonerId': summonerId,
            'region': region,
            'entries': jsonResponse[summonerId],
        }
    elif response.status_code == 404:
        return {
            'summonerId': summonerId,
            'region': region,
            'entries': []
        }
    else:
        raise RiotServerError
