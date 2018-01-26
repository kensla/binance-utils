#!/usr/bin/env python3
import json
from time import sleep
import urllib3


BASE_URL = "https://api.binance.com"


urllib3.disable_warnings()


def get_exchange_info():
    http = urllib3.PoolManager()

    ctxt = {'headers': {'Content-Type': 'application/json'},
            'method': 'GET',
            'url': BASE_URL + "/api/v1/exchangeInfo"}
	
    r = http.request(**ctxt)

    return json.loads(r.data.decode())


def get_ticker_price(symbol):
    http = urllib3.PoolManager()

    ctxt = {'headers': {'Content-Type': 'application/json'},
            'method': 'GET',
            'url': BASE_URL + "/api/v3/ticker/price?symbol={}".format(symbol)}
	
    r = http.request(**ctxt)

    return json.loads(r.data.decode())


def get_all_ticker_prices():
    http = urllib3.PoolManager()

    ctxt = {'headers': {'Content-Type': 'application/json'},
            'method': 'GET',
            'url': BASE_URL + "/api/v3/ticker/price"}
	
    r = http.request(**ctxt)

    return json.loads(r.data.decode())
