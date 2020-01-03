import pandas as pd
import numpy as np
import re
import sys
import os



def skill_effect_shaped_list():
    columns = ["skill"]
    for i in range(20):
        columns.append("Lv"+str(i+1))
    print(columns)
    df_na = pd.read_csv("./skill_effect/skill_effect_normal_attack.csv", names=columns)
    df_ma = pd.read_csv("./skill_effect/skill_effect_maguna_attack.csv", names=columns)
    df_exa = pd.read_csv("./skill_effect/skill_effect_ex_attack.csv", names=columns)
    df_nd = pd.read_csv("./skill_effect/skill_effect_normal_defence.csv", names=columns)
    df_md = pd.read_csv("./skill_effect/skill_effect_maguna_defence.csv", names=columns)
    df_kamui = pd.read_csv("./skill_effect/skill_effect_kamui.csv", names=columns)
    df_haisui = pd.read_csv("./skill_effect/skill_effect_haisui.csv", names=columns)
    df_konshin = pd.read_csv("./skill_effect/skill_effect_konshin.csv", names=columns)
    df_DATA = pd.read_csv("./skill_effect/skill_effect_DATA.csv", names=columns)
    df_critical = pd.read_csv("./skill_effect/skill_effect_critical.csv", names=columns)
    df_bahamut = pd.read_csv("./skill_effect/skill_effect_bahamut.csv", names=columns)

    df_na=df_na.fillna(0)
    df_ma=df_ma.fillna(0)
    df_exa=df_exa.fillna(0)
    df_nd=df_nd.fillna(0)
    df_md=df_md.fillna(0)
    df_kamui=df_kamui.fillna(0)
    df_haisui=df_haisui.fillna(0)
    df_konshin=df_konshin.fillna(0)
    df_DATA=df_DATA.fillna(0)
    df_critical=df_critical.fillna(0)
    df_bahamut = df_bahamut.fillna(0)
    print(df_na)
    print(len(df_na)-1)
    print(len(df_na.columns)-1)
    print(df_na.iloc[1, 12])

    for i in range(len(df_na)):
        for j in range(len(df_na.columns)-1):
            if '%' in str(df_na.iloc[i, j+1]):
                df_na.iloc[i, j+1] = float(df_na.iloc[i, j+1][:-1])
            if "％" in str(df_na.iloc[i, j+1]):
                df_na.iloc[i, j+1] = float(df_na.iloc[i, j+1][:-1])

    for i in range(len(df_ma)):
        for j in range(len(df_ma.columns)-1):
            if '%' in str(df_ma.iloc[i, j+1]):
                df_ma.iloc[i, j+1] = float(df_ma.iloc[i, j+1][:-1])
            if '％' in str(df_ma.iloc[i, j+1]):
                df_ma.iloc[i, j+1] = float(df_ma.iloc[i, j+1][:-1])

    for i in range(len(df_exa)):
        for j in range(len(df_exa.columns)-1):
            if '%' in str(df_exa.iloc[i, j+1]):
                df_exa.iloc[i, j+1] = float(df_exa.iloc[i, j+1][:-1])
            if '％' in str(df_exa.iloc[i, j+1]):
                df_exa.iloc[i, j+1] = float(df_exa.iloc[i, j+1][:-1])

    for i in range(len(df_nd)):
        for j in range(len(df_nd.columns)-1):
            if '%' in str(df_nd.iloc[i, j+1]):
                df_nd.iloc[i, j+1] = float(df_nd.iloc[i, j+1][:-1])
            if '％' in str(df_nd.iloc[i, j+1]):
                df_nd.iloc[i, j+1] = float(df_nd.iloc[i, j+1][:-1])

    for i in range(len(df_md)):
        for j in range(len(df_md.columns)-1):
            if '%' in str(df_md.iloc[i, j+1]):
                df_md.iloc[i, j+1] = float(df_md.iloc[i, j+1][:-1])
            if '％' in str(df_md.iloc[i, j+1]):
                df_md.iloc[i, j+1] = float(df_md.iloc[i, j+1][:-1])

    for i in range(len(df_kamui)):
        for j in range(len(df_kamui.columns)-1):
            if '%' in str(df_kamui.iloc[i, j+1]):
                df_kamui.iloc[i, j+1] = float(df_kamui.iloc[i, j+1][:-1])
            if '％' in str(df_kamui.iloc[i, j+1]):
                df_kamui.iloc[i, j+1] = float(df_kamui.iloc[i, j+1][:-1])

    for i in range(len(df_haisui)):
        for j in range(len(df_haisui.columns)-1):
            if '%' in str(df_haisui.iloc[i, j+1]):
                df_haisui.iloc[i, j+1] = float(df_haisui.iloc[i, j+1][:-1])
            if '％' in str(df_haisui.iloc[i, j+1]):
                df_haisui.iloc[i, j+1] = float(df_haisui.iloc[i, j+1][:-1])

    for i in range(len(df_konshin)):
        for j in range(len(df_konshin.columns)-1):
            if '%' in str(df_konshin.iloc[i, j+1]):
                df_konshin.iloc[i, j+1] = float(df_konshin.iloc[i, j+1][:-1])
            if '％' in str(df_konshin.iloc[i, j+1]):
                df_konshin.iloc[i, j+1] = float(df_konshin.iloc[i, j+1][:-1])

    for i in range(len(df_DATA)):
        for j in range(len(df_DATA.columns)-1):
            if '%' in str(df_DATA.iloc[i, j+1]):
                df_DATA.iloc[i, j+1] = float(df_DATA.iloc[i, j+1][:-1])
            if '％' in str(df_DATA.iloc[i, j+1]):
                df_DATA.iloc[i, j+1] = float(df_DATA.iloc[i, j+1][:-1])

    for i in range(len(df_critical)):
        for j in range(len(df_critical.columns)-1):
            if '%' in str(df_critical.iloc[i, j+1]):
                df_critical.iloc[i, j+1] = float(df_critical.iloc[i, j+1][:-1])
            if '％' in str(df_critical.iloc[i, j+1]):
                df_critical.iloc[i, j+1] = float(df_critical.iloc[i, j+1][:-1])

    for i in range(len(df_bahamut)):
        for j in range(len(df_bahamut.columns)-1):
            if '%' in str(df_bahamut.iloc[i, j+1]):
                df_bahamut.iloc[i, j+1] = float(df_bahamut.iloc[i, j+1][:-1])
            if '％' in str(df_bahamut.iloc[i, j+1]):
                df_bahamut.iloc[i, j+1] = float(df_bahamut.iloc[i, j+1][:-1])

    """baha_atkorhp = np.array(df_bahamut.iloc[0])
    baha_atkandhp = np.array(df_bahamut.iloc[1])
    baha_released_atk = np.array(df_bahamut.iloc[2])
    baha_released_andhp = np.array(df_bahamut.iloc[3])
    baha_released_hp = np.array(df_bahamut.iloc[4])
    baha_released_DATA = np.array(df_bahamut.iloc[5])"""

    for i in range(6):
        df_bahamut.iloc[2, i+10] = df_bahamut.iloc[2, i+1]
        df_bahamut.iloc[3, i+10] = df_bahamut.iloc[3, i+1]
        df_bahamut.iloc[4, i+10] = df_bahamut.iloc[4, i+3]
        df_bahamut.iloc[5, i+10] = df_bahamut.iloc[5, i+3]

    for i in range(9):
        df_bahamut.iloc[2, i+1] = 0
        df_bahamut.iloc[3, i+1] = 0
        df_bahamut.iloc[4, i+1] = df_bahamut.iloc[0, i+1]
        df_bahamut.iloc[5, i+1] = 0

    print(df_bahamut)


    df_na.to_csv("./skill_effect/skill_effect_shaped/skill_effect_normal_attack.csv", index=None)
    df_ma.to_csv("./skill_effect/skill_effect_shaped/skill_effect_maguna_attack.csv", index=None)
    df_exa.to_csv("./skill_effect/skill_effect_shaped/skill_effect_ex_attack.csv", index=None)
    df_nd.to_csv("./skill_effect/skill_effect_shaped/skill_effect_normal_defence.csv", index=None)
    df_md.to_csv("./skill_effect/skill_effect_shaped/skill_effect_maguna_defence.csv", index=None)
    df_kamui.to_csv("./skill_effect/skill_effect_shaped/skill_effect_kamui.csv", index=None)
    df_haisui.to_csv("./skill_effect/skill_effect_shaped/skill_effect_haisui.csv", index=None)
    df_konshin.to_csv("./skill_effect/skill_effect_shaped/skill_effect_konshin.csv", index=None)
    df_DATA.to_csv("./skill_effect/skill_effect_shaped/skill_effect_DATA.csv", index=None)
    df_critical.to_csv("./skill_effect/skill_effect_shaped/skill_effect_critical.csv", index=None)
    df_bahamut.to_csv("./skill_effect/skill_effect_shaped/skill_effect_bahamut.csv", index=None)



if __name__ == "__main__":
    skill_effect_shaped_list()
