import pandas as pd
import numpy as np
import re
import sys
import os

def skill_shaped_list():
    columns = ["skill_name", "effect", "remarks"]
    df1 = pd.read_csv("./weapon_data/weapon_ssr_list.csv")
    df2 = pd.read_csv("./weapon_data/weapon_ssr_released4_list.csv")
    df3 = pd.read_csv("./weapon_data/weapon_ssr_released5_list.csv")
    df_skill = pd.read_csv("./weapon_skill_list.csv", names=columns)

    f_skill1 = np.array(df1["f_skill"])
    f_skill2 = np.array(df2["f_skill"])
    f_skill3 = np.array(df3["f_skill"])
    pre_f_skill2 = np.array(df2["pre_f_skill"])
    pre_f_skill3 = np.array(df3["pre_f_skill"])

    s_skill1 = np.array(df1["s_skill"])
    s_skill2 = np.array(df2["s_skill"])
    s_skill3 = np.array(df3["s_skill"])
    pre_s_skill2 = np.array(df2["pre_s_skill"])
    pre_s_skill3 = np.array(df3["pre_s_skill"])

    df1["f_skill_effect"] = ""
    df2["f_skill_effect"] = ""
    df3["f_skill_effect"] = ""
    df1["s_skill_effect"] = ""
    df2["s_skill_effect"] = ""
    df3["s_skill_effect"] = ""

    df2["pre_f_skill_effect"] = ""
    df2["pre_s_skill_effect"] = ""
    df3["pre_f_skill_effect"] = ""
    df3["pre_s_skill_effect"] = ""

    f_skill_index1 = df1.columns.get_loc('f_skill_effect')
    s_skill_index1 = df1.columns.get_loc('s_skill_effect')
    f_skill_index2 = df2.columns.get_loc('f_skill_effect')
    s_skill_index2 = df2.columns.get_loc('s_skill_effect')
    f_skill_index3 = df3.columns.get_loc('f_skill_effect')
    s_skill_index3 = df3.columns.get_loc('s_skill_effect')

    pre_f_skill_index2 = df2.columns.get_loc('pre_f_skill_effect')
    pre_s_skill_index2 = df2.columns.get_loc('pre_s_skill_effect')
    pre_f_skill_index3 = df3.columns.get_loc('pre_f_skill_effect')
    pre_s_skill_index3 = df3.columns.get_loc('pre_s_skill_effect')

    skill_name = np.array(df_skill["skill_name"])
    effect_index = df_skill.columns.get_loc('effect')

    for i in range(np.size(skill_name)):
        for j in range(np.size(f_skill1)):
            if (f_skill1[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df1.iloc[j, f_skill_index1] = effect

            if (s_skill1[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df1.iloc[j, s_skill_index1] = effect

    for i in range(np.size(skill_name)):
        for j in range(np.size(f_skill2)):
            if (f_skill2[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df2.iloc[j, f_skill_index2] = effect

            if (s_skill2[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df2.iloc[j, s_skill_index2] = effect

            if (pre_f_skill2[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df2.iloc[j, pre_f_skill_index2] = effect

            if (pre_s_skill2[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df2.iloc[j, pre_s_skill_index2] = effect

    for i in range(np.size(skill_name)):
        for j in range(np.size(f_skill3)):
            if (f_skill3[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df3.iloc[j, f_skill_index3] = effect

            if (s_skill3[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df3.iloc[j, s_skill_index3] = effect

            if (pre_f_skill3[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df3.iloc[j, pre_f_skill_index3] = effect

            if (pre_s_skill3[j] == skill_name[i]):
                effect = df_skill.iloc[i, effect_index]
                df3.iloc[j, pre_s_skill_index3] = effect

    print(df3["s_skill"])
    df1.to_csv("./weapon_data/skill_shaped/weapon_ssr_list_skill.csv", index=None)
    df2.to_csv("./weapon_data/skill_shaped/weapon_ssr_released4_list_skill.csv", index=None)
    df3.to_csv("./weapon_data/skill_shaped/weapon_ssr_released5_list_skill.csv", index=None)







if __name__ == "__main__":
    #weapon_del()
    skill_shaped_list()
