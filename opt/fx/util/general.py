# -*- coding: utf-8 -*-
import os

def dropColumn(df):
    df = df.drop(columns=[
        '前日比%',
        '始値',
        '終値',
    ], axis=1)
    return df

def renameColumn(df, prefix):
    df = df.rename(columns={
        '日付け': 'date',
        '高値': prefix + '_high',
        '安値': prefix + '_low',
        })
    return df

def switchingFile(df, path, currency):
    file = path + '/' + currency + '.csv'
    temp = path + '/' + currency + '.tmp'
    if os.path.exists(temp):
        os.remove(temp)
    df.to_csv(temp, mode='a', header=True, index=False)
    if os.path.exists(file):
        os.remove(file)
    os.rename(temp, file)
