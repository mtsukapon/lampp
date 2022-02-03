# -*- coding: utf-8 -*-
import os, shutil, glob
import pandas as pd

class proc:
    def __init__(self):
        current = str(os.getcwd())
        #in
        self.__input_path = current + "/in"
        #out
        self.__output_path = current + "/out"

    def checkPath(self):
        #in
        if not os.path.exists(self.__input_path):
            return True
        #out
        output = self.__output_path
        if os.path.exists(output):
            shutil.rmtree(output)
        os.mkdir(output)
        return False

    def unitCsvRowData(self, currency):
        search = self.__input_path + '/**/*' + currency + '*.csv'
        csvFiles = glob.glob(search, recursive=True)
        #1ファイル目のヘッダ行は使用する
        isHeader = True
        for csvFile in csvFiles:
            df = pd.read_csv(csvFile, engine='python', encoding='UTF-8')
            df.to_csv(self.__output_path + '/' + currency + '.csv', mode='a', header=isHeader, index=False)
            #2ファイル目以降のヘッダ行は使用しない
            isHeader = False
