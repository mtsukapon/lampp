# -*- coding: utf-8 -*-
from model import exchange
import sys

obj = exchange.proc()
if obj.checkPath():
    sys.exit()

currencies = ['EUR_JPY', 'USD_JPY']
for currency in currencies:
    obj.unitCsvRowData(currency)
    if obj.modifyColumn(currency):
        sys.exit()

obj.unitCsvColData()
