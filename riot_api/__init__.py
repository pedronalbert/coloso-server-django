from .client import fetchSummonerByName, fetchSummonerById, fetchSummonerRunes, fetchSummonerMasteries, fetchSummonerStatsSummary, fetchSummonerChampionsMastery, fetchSummonerGamesRecent, fetchSummonerLeagueEntry, fetchSummonerGameCurrent, fetchSummonersLeagueEntry
from pydash.objects import has_path

class RiotApi:
    def __init__(self, region):
        self.region = region

    def getSummonerByName(self, summonerName):
        return fetchSummonerByName(self.region, summonerName)

    def getSummonerById(self, summonerId):
        return fetchSummonerById(self.region, summonerId)

    def getSummonerRunes(self, summonerId):
        return fetchSummonerRunes(self.region, summonerId)

    def getSummonerMasteries(self, summonerId):
        return fetchSummonerMasteries(self.region, summonerId)

    def getSummonerStatsSummary(self, summonerId, season):
        return fetchSummonerStatsSummary(self.region, summonerId, season)

    def getSummonerChampionsMastery(self, summonerId):
        return fetchSummonerChampionsMastery(self.region, summonerId)

    def getSummonerGamesRecent(self, summonerId):
        return fetchSummonerGamesRecent(self.region, summonerId)

    def getSummonerLeagueEntry(self, summonerId):
        return fetchSummonerLeagueEntry(self.region, summonerId)

    def getSummonerGameCurrent(self, summonerId):
        gameCurrent = fetchSummonerGameCurrent(self.region, summonerId)
        summonerIds = []

        for participant in gameCurrent['participants']:
            summonerIds.append(participant['summonerId'])

        leagueEntries = fetchSummonersLeagueEntry(self.region, summonerIds)

        for participant in gameCurrent['participants']:
            if has_path(leagueEntries, str(participant['summonerId'])):
                participant['leagueEntries'] = leagueEntries[str(participant['summonerId'])]

        return gameCurrent
