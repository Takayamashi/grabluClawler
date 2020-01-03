import pandas as pd
import numpy as np
import re
import sys
import os

def weapon_released5_list():
    columns = ["name", "attribute", "species", "f_skill", "s_skill",
    "minhp", "minatk","maxhp1", "maxatk1", "maxhp2", "maxatk2","maxhp3", "maxatk3"]
    df1 = pd.read_csv("./weapon_ssr_released5_deled.csv")
    df2 = pd.read_csv("./weapon_ssr_released4_deled.csv")
    df3 = pd.read_csv("./weapon_ssr_whole.csv")
    df4 = pd.read_csv("./weapon_ssr_deled.csv")

    df1["minhp"] = 0
    df1["minatk"] = 0
    df1["maxhp1"] = 0
    df1["maxatk1"] = 0
    df1["maxhp2"] = 0
    df1["maxatk2"] = 0
    df1["pre_f_skill"] = 0
    df1["pre_s_skill"] = 0

    pre_f_skill_index1 = df1.columns.get_loc('pre_f_skill')
    pre_s_skill_index1 = df1.columns.get_loc('pre_s_skill')

    f_skill_index1 = df1.columns.get_loc('f_skill')
    s_skill_index1 = df1.columns.get_loc('s_skill')
    f_skill_index3 = df3.columns.get_loc('f_skill')
    s_skill_index3 = df3.columns.get_loc('s_skill')

    weapon_name1 = np.array(df1["name"])
    weapon_name2 = np.array(df2["name"])
    weapon_name3 = np.array(df3["name"])
    weapon_name4 = np.array(df4["name"])


    minhp_index1 = df1.columns.get_loc('minhp')
    minatk_index1 = df1.columns.get_loc('minatk')
    minhp_index3 = df3.columns.get_loc('minhp')
    minatk_index3 = df3.columns.get_loc('minatk')

    maxhp1_index1 = df1.columns.get_loc('maxhp1')
    maxatk1_index1 = df1.columns.get_loc('maxatk1')
    maxhp1_index3 = df3.columns.get_loc('maxhp1')
    maxatk1_index3 = df3.columns.get_loc('maxatk1')

    maxhp2_index1 = df1.columns.get_loc('maxhp2')
    maxatk2_index1 = df1.columns.get_loc('maxatk2')
    maxhp2_index2 = df2.columns.get_loc('maxhp2')
    maxatk2_index2 = df2.columns.get_loc('maxatk2')

    for i in range(np.size(weapon_name3)):
        for j in range(np.size(weapon_name1)):
            if weapon_name3[i]==weapon_name1[j]:

                minhp = df3.iloc[i, minhp_index3]
                minatk = df3.iloc[i, minatk_index3]
                df1.iloc[j, minhp_index1] = minhp
                df1.iloc[j, minatk_index1] = minatk

    for i in range(np.size(weapon_name3)):
        for j in range(np.size(weapon_name1)):
            if weapon_name3[i]==weapon_name1[j]:

                maxhp1 = df3.iloc[i, maxhp1_index3]
                maxatk1 = df3.iloc[i, maxatk1_index3]
                df1.iloc[j, maxhp1_index1] = maxhp1
                df1.iloc[j, maxatk1_index1] = maxatk1

    for i in range(np.size(weapon_name2)):
        for j in range(np.size(weapon_name1)):
            if weapon_name2[i]==weapon_name1[j]:
                maxhp2 = df2.iloc[i, maxhp2_index2]
                maxatk2 = df2.iloc[i, maxatk2_index2]
                df1.iloc[j, maxhp2_index1] = maxhp2
                df1.iloc[j, maxatk2_index1] = maxatk2

    for i in range(np.size(weapon_name1)):
        k = 0
        for j in range(np.size(weapon_name3)):
            if (weapon_name3[j]==weapon_name1[i] and k==0):
                k = k+1
                f_skill3 = df3.iloc[j, f_skill_index3]
                s_skill3 = df3.iloc[j, s_skill_index3]
                f_skill1 = df1.iloc[i, f_skill_index1]
                s_skill1 = df1.iloc[i, s_skill_index1]

                if (f_skill3 != f_skill1 or s_skill3 != s_skill1):
                    df1.iloc[i, pre_f_skill_index1] = f_skill3
                    df1.iloc[i, pre_s_skill_index1] = s_skill3

    print(df1)
    for i in range(np.size(weapon_name1)):
        for j in range(np.size(weapon_name2)):
            if weapon_name2[j]==weapon_name1[i]:
                df2 = df2.drop(j, axis=0)

    for i in range(np.size(weapon_name1)):
        for j in range(np.size(weapon_name4)):
            if weapon_name4[j]==weapon_name1[i]:
                df4 = df4.drop(j, axis=0)

    print(df2)

    df4.to_csv("./weapon_ssr_deled.csv",index=None)
    df2.to_csv("./weapon_ssr_released4_deled.csv",index=None)
    df1.to_csv("./weapon_data/weapon_ssr_released5_list.csv",index=None)

def weapon_released4_list():
    df2 = pd.read_csv("./weapon_ssr_released4_deled.csv")
    df3 = pd.read_csv("./weapon_ssr_deled.csv")
    df4 = pd.read_csv("./weapon_ssr_whole.csv")
    df5 = pd.read_csv("./weapon_special_deled.csv")

    df2["minhp"] = 0
    df2["minatk"] = 0
    df2["maxhp1"] = 0
    df2["maxatk1"] = 0

    minhp_index2 = df2.columns.get_loc('minhp')
    minatk_index2 = df2.columns.get_loc('minatk')
    minhp_index4 = df4.columns.get_loc('minhp')
    minatk_index4 = df4.columns.get_loc('minatk')
    minhp_index5 = df5.columns.get_loc('minhp')
    minatk_index5 = df5.columns.get_loc('minatk')

    maxhp_index2 = df2.columns.get_loc('maxhp1')
    maxatk_index2 = df2.columns.get_loc('maxatk1')
    maxhp_index4 = df4.columns.get_loc('maxhp1')
    maxatk_index4 = df4.columns.get_loc('maxatk1')
    maxhp_index5 = df5.columns.get_loc('maxhp1')
    maxatk_index5 = df5.columns.get_loc('maxatk1')

    maxhp2_index2 = df2.columns.get_loc('maxhp2')
    maxatk2_index2 = df2.columns.get_loc('maxatk2')
    df2 = df2.fillna(0)
    df2 = df2.replace("???", 0)
    df2 = df2.replace("????", 0)


    weapon_name2 = np.array(df2["name"])
    weapon_name3 = np.array(df3["name"])
    weapon_name4 = np.array(df4["name"])
    weapon_name5 = np.array(df5["name"])

    for i in range(np.size(weapon_name2)):
        k = 0
        for j in range(np.size(weapon_name4)):
            if (weapon_name4[j]==weapon_name2[i] and k==0):
                k = k+1
                maxhp = int(df4.iloc[j, maxhp_index4])
                maxatk = int(df4.iloc[j, maxatk_index4])
                maxhp2 = int(df2.iloc[i, maxhp2_index2])
                maxatk2 = int(df2.iloc[i, maxatk2_index2])

                if (maxhp2 != maxhp):
                    df2.iloc[i, maxhp_index2] = maxhp
                if (maxatk2 != maxatk):
                    df2.iloc[i, maxatk_index2] = maxatk

        for j in range(np.size(weapon_name5)):
            if (weapon_name5[j]==weapon_name2[i] and k==0):
                k = k+1
                maxhp = int(df5.iloc[j, maxhp_index5])
                maxatk = int(df5.iloc[j, maxatk_index5])
                maxhp2 = int(df2.iloc[i, maxhp2_index2])
                maxatk2 = int(df2.iloc[i, maxatk2_index2])

                if (maxhp2 != maxhp):
                    df2.iloc[i, maxhp_index2] = maxhp
                if (maxatk2 != maxatk):
                    df2.iloc[i, maxatk_index2] = maxatk

    for i in range(np.size(weapon_name2)):
        k = 0
        for j in range(np.size(weapon_name4)):
            if (weapon_name4[j]==weapon_name2[i] and k==0):
                k = k+1
                minhp = df4.iloc[j, minhp_index4]
                minatk = df4.iloc[j, minatk_index4]
                df2.iloc[i, minhp_index2] = minhp
                df2.iloc[i, minatk_index2] = minatk

        for j in range(np.size(weapon_name5)):
            if (weapon_name5[j]==weapon_name2[i] and k==0):
                k = k+1
                minhp = df5.iloc[j, minhp_index5]
                minatk = df5.iloc[j, minatk_index5]
                df2.iloc[i, minhp_index2] = minhp
                df2.iloc[i, minatk_index2] = minatk

    f_skill_index2 = df2.columns.get_loc('f_skill')
    s_skill_index2 = df2.columns.get_loc('s_skill')
    f_skill_index4 = df4.columns.get_loc('f_skill')
    s_skill_index4 = df4.columns.get_loc('s_skill')
    f_skill_index5 = df5.columns.get_loc('f_skill')
    s_skill_index5 = df5.columns.get_loc('s_skill')

    df2["pre_f_skill"] = 0
    df2["pre_s_skill"] = 0

    pre_f_skill_index2 = df2.columns.get_loc('pre_f_skill')
    pre_s_skill_index2 = df2.columns.get_loc('pre_s_skill')

    for i in range(np.size(weapon_name2)):
        k = 0
        for j in range(np.size(weapon_name4)):
            if (weapon_name4[j]==weapon_name2[i] and k==0):
                k = k+1
                f_skill4 = df4.iloc[j, f_skill_index4]
                s_skill4 = df4.iloc[j, s_skill_index4]
                f_skill2 = df2.iloc[i, f_skill_index2]
                s_skill2 = df2.iloc[i, s_skill_index2]

                if (f_skill4 != f_skill2 or s_skill4 != s_skill2):
                    df2.iloc[i, pre_f_skill_index2] = f_skill4
                    df2.iloc[i, pre_s_skill_index2] = s_skill4

        for j in range(np.size(weapon_name5)):
            if (weapon_name5[j]==weapon_name2[i] and k==0):
                k = k+1
                f_skill5 = df5.iloc[j, f_skill_index5]
                s_skill5 = df5.iloc[j, s_skill_index5]
                f_skill2 = df2.iloc[i, f_skill_index2]
                s_skill2 = df2.iloc[i, s_skill_index2]

                if (f_skill5 != f_skill2 or s_skill5 != s_skill2):
                    df2.iloc[i, pre_f_skill_index2] = f_skill5
                    df2.iloc[i, pre_s_skill_index2] = s_skill5

    for i in range(np.size(weapon_name2)):
        for j in range(np.size(weapon_name3)):
            if weapon_name2[i]==weapon_name3[j]:
                df3 = df3.drop(j, axis=0)



    df3.to_csv("./weapon_data/weapon_ssr_list.csv", index=None)
    df2.to_csv("./weapon_data/weapon_ssr_released4_list.csv",index=None)


def weapon_rokudo_baha_omega():
    df_rokudo = pd.read_csv("./weapon_rokudo_deled.csv")
    df_baha = pd.read_csv("./weapon_baha_deled.csv")
    df_omega = pd.read_csv("./weapon_omega_deled.csv")

    df_rokudo["minhp"] = 0
    df_rokudo["minatk"] = 0
    df_baha["minhp"] = 0
    df_baha["minatk"] = 0
    df_omega["minhp"] = 0
    df_omega["minatk"] = 0



if __name__ == "__main__":
    weapon_released5_list()
    weapon_released4_list()
