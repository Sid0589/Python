import datetime

try:
    from urllib.parse import urljoin
except ImportError: 
    from urlparse import urljoin 

import requests
from datetime import date


class CurExchRate():
    BASE_URL = 'http://api.fixer.io/'
    LATEST_PATH = '/latest'
 
    def __init__(self, base='EUR'):
        self.base = base 
    @staticmethod
    def _create_payload(base):
        payload = {}
        if base is not None:
            payload['base'] = base
        return payload
    @staticmethod
    def _url(path):
        url = urljoin(CurExchRate.BASE_URL, path)
        return url
    def latest(self, base=None):
        try:
            base = base or self.base
            payload = CurExchRate._create_payload(base)
            url = CurExchRate._url(CurExchRate.LATEST_PATH)
            response = requests.get(url, params=payload)
            return response.json()
        except Exception as ex:
            print str(ex.args)
    def historical_rates(self,start_date,end_date,base=None):
        try:
            if not isinstance(start_date,datetime.date):
                print 'start_date:use date data type'
                exit(2)
            if not isinstance(end_date,datetime.date):
                print 'end_date:use date data type'
                exit(2)
            if start_date < datetime.date(1999,1,1):
                print "invalid start date"
                exit(2)
            if start_date > end_date:
                print 'end date is less than start date'
                exit(2)
            base = base or self.base
            diff = (end_date - start_date).days
            payload = CurExchRate._create_payload(base)
            result ={}
            for i in range(0,diff+1):
                date = (start_date + datetime.timedelta(days=i)).isoformat()
                url = CurExchRate._url(date)
                response = requests.get(url, params=payload)
                result[date] = response.json()
            return result
        except Exception as ex:
            print str(ex.args)
