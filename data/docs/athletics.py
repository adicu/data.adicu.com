from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.athletics.athletics_functions as athletics

lead = """The athletics endpoint is kind of broken down by
                feed -- results and schedules.  Play around with the different
                sports, as some can be pretty interesting! After you've pinged
                it a couple times you'll start to notice the differences in
                format between results, and schedules and how sports names are
                formatted"""
endpoints = {
                    "athletics" : {
                        "request": "http://data.adicu.com/athletics?win=true&pretty=true&api_token=TOKEN",
                        "response": """ {
    "status_code": 200,
    "data": [
        {
            "feed": "results",
            "sport": "wrestling",
            "title": "Wrestling: vs San Francisco State (01/06/2013) - W (28-8)",
            "win": true,
            "article_link": "http://www.gocolumbialions.com/ViewArticle.dbml?DB_OEM_ID=9600&amp;ATCLID=205878762",
            "score": "28-8",
            "link": "http://www.gocolumbialions.com//SportSelect.dbml?DB_OEM_ID=9600&SPID=3876&SPSID=43591&Q_SEASON=2012",
            "location": "San Luis Obispo, Calif.",
            "time": "2013-01-06 15:00:00",
            "opponent": "San Francisco State"
        },""",
                        "queries" : c(mem(athletics, func)),
                    },
        }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
