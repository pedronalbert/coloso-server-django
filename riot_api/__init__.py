from .client import fetchSummonerByName, fetchSummonerById, fetchSummonerRunes, fetchSummonerMasteries, fetchSummonerStatsSummary, fetchSummonerChampionsMastery, fetchSummonerGamesRecent

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
