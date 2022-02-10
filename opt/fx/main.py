# -*- coding: utf-8 -*-
from model import exchange
import sys

obj = exchange.proc()
if obj.checkPath():
    sys.exit()

currencies = ['EUR_JPY', 'EUR_USD', 'USD_JPY', 'WTI']
for currency in currencies:
    obj.unitCsvRowData(currency)
    if obj.modifyColumn(currency):
        sys.exit()

obj.unitCsvColData()
obj.complementDate()

for currency in currencies:
    obj.replaceMissingValue(currency)

obj.addDayOfWeekCode()
