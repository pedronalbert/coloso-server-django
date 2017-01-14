from .client import fetchSummonerByName, fetchSummonerById, fetchSummonerRunes, fetchSummonerMasteries

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
