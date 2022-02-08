# -*- coding: utf-8 -*-
import os, shutil, glob
import pandas as pd
from util import general

class proc:
    EXCHANGE_FILE = "exchange.csv"

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
        df.to_csv(output + '/' + self.EXCHANGE_FILE, index=False)

    def complementDate(self):
        output = self.__output_path
        df = pd.read_csv(output + '/' + self.EXCHANGE_FILE)
        #yyyy年㎜月dd日からyyyy-mm-ddに形式を置換
        df['date'] = df['date'].str.replace('年', '-')
        df['date'] = df['date'].str.replace('月', '-')
        df['date'] = df['date'].str.replace('日', '')
        #日付型に置換
        df['date'] = pd.to_datetime(df['date'])
        #日付順に並び替え
        df = df.sort_values('date', ascending=True)
        #インデックスを日付に指定
        df.set_index(df['date'], inplace=True)
        #インデックスの最小値/最大値を取得
        min_date = df.index.min()
        max_date = df.index.max()
        #欠落日を補完
        df = df.reindex(pd.date_range(min_date, max_date), fill_value="NaN")
        #インデックスを日付に置き換える
        df['date'] = df.index
        df.to_csv(output + '/' + self.EXCHANGE_FILE, index=False)

    def replaceMissingValue(self, currency):
        output = self.__output_path
        df = pd.read_csv(output + '/' + self.EXCHANGE_FILE)
        #型変換 print(df.dtypes)
        df = df.astype({
            currency + "_high": float,
            currency + "_low": float,
        })
        #欠損値を0に置換
        df = df.fillna({
            currency + "_high": 0,
            currency + "_low": 0,
        })
        df.to_csv(output + '/' + self.EXCHANGE_FILE, index=False)
