# -*- coding: utf-8 -*-
from model import exchange
from util import general
import sys

obj = exchange.proc()
if obj.checkPath():
    sys.exit()

currencies = ['EUR_JPY', 'EUR_USD', 'USD_JPY', 'WTI']
for currency in currencies:
    obj.unitCsvRowData(currency)
