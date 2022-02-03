# -*- coding: utf-8 -*-
import os, shutil, glob
import pandas as pd
from util import general

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

    def modifyColumn(self, currency):
        #結合したCSVファイルが/outになければ後続の処理を行わない
        path = self.__output_path
        file = path + '/' + currency + '.csv'
        if not os.path.exists(file):
            return True
        df = pd.read_csv(file, engine='python', encoding='UTF-8')
        #不要カラムの削除
        df = general.dropColumn(df)
        #カラム名の変更
        df = general.renameColumn(df, currency)
        #ファイルの差し替え
        general.switchingFile(df, path, currency)
        return False

    def unitCsvColData(self):
        output = self.__output_path
        df1 = pd.read_csv(output + '/EUR_JPY.csv')
        df2 = pd.read_csv(output + '/USD_JPY.csv')
        df = pd.merge(df1, df2, on='date', how='outer')
        df.to_csv(output + '/exchange.csv', index=False)
