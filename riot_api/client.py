import requests
from django.conf import settings
from pydash.arrays import find_index
from exceptions import NotFoundException, RiotServerError

API_KEY = settings.RIOT_API_KEY


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
