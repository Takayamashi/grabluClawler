import pandas as pd
import numpy as np
import re
import sys
import os
import skill_checker as sc


def weapon_csv_making():
    df1 = pd.read_csv("./weapon_data/skill_shaped/weapon_ssr_list_skill.csv")
    df2 = pd.read_csv("./weapon_data/skill_shaped/weapon_ssr_released4_list_skill.csv")
    df3 = pd.read_csv("./weapon_data/skill_shaped/weapon_ssr_released5_list_skill.csv")

    df1["f_skill_detail1"] = 0
    df1["f_skill_detail2"] = 0
    df1["s_skill_detail1"] = 0
    df1["s_skill_detail2"] = 0
    df2["f_skill_detail1"] = 0
    df2["f_skill_detail2"] = 0
    df2["s_skill_detail1"] = 0
    df2["s_skill_detail2"] = 0
    df2["pre_f_skill_detail1"] = 0
    df2["pre_f_skill_detail2"] = 0
    df2["pre_s_skill_detail1"] = 0
    df2["pre_s_skill_detail2"] = 0
    df3["f_skill_detail1"] = 0
    df3["f_skill_detail2"] = 0
    df3["s_skill_detail1"] = 0
    df3["s_skill_detail2"] = 0
    df3["pre_f_skill_detail1"] = 0
    df3["pre_f_skill_detail2"] = 0
    df3["pre_s_skill_detail1"] = 0
    df3["pre_s_skill_detail2"] = 0

    """df1["f_skill_detail"] = df1["f_skill_detail"].str.split(',')
    df1["s_skill_detail"] = df1["s_skill_detail"].str.split(',')
    df2["f_skill_detail"] = df2["f_skill_detail"].str.split(',')
    df2["s_skill_detail"] = df2["s_skill_detail"].str.split(',')
    df2["pre_f_skill_detail"] = df2["pre_f_skill_detail"].str.split(',')
    df2["pre_s_skill_detail"] = df2["pre_s_skill_detail"].str.split(',')
    df3["f_skill_detail"] = df3["f_skill_detail"].str.split(',')
    df3["s_skill_detail"] = df3["s_skill_detail"].str.split(',')"""


    f_skill_index1 = df1.columns.get_loc('f_skill')
    s_skill_index1 = df1.columns.get_loc('s_skill')
    f_skill_index2 = df2.columns.get_loc('f_skill')
    s_skill_index2 = df2.columns.get_loc('s_skill')
    f_skill_index3 = df3.columns.get_loc('f_skill')
    s_skill_index3 = df3.columns.get_loc('s_skill')
    pre_f_skill_index2 = df2.columns.get_loc('pre_f_skill')
    pre_s_skill_index2 = df2.columns.get_loc('pre_s_skill')
    pre_f_skill_index3 = df3.columns.get_loc('pre_f_skill')
    pre_s_skill_index3 = df3.columns.get_loc('pre_s_skill')

    f_skill_effect_index1 = df1.columns.get_loc('f_skill_effect')
    s_skill_effect_index1 = df1.columns.get_loc('s_skill_effect')
    f_skill_effect_index2 = df2.columns.get_loc('f_skill_effect')
    s_skill_effect_index2 = df2.columns.get_loc('s_skill_effect')
    f_skill_effect_index3 = df3.columns.get_loc('f_skill_effect')
    s_skill_effect_index3 = df3.columns.get_loc('s_skill_effect')
    pre_f_skill_effect_index2 = df2.columns.get_loc('pre_f_skill_effect')
    pre_s_skill_effect_index2 = df2.columns.get_loc('pre_s_skill_effect')
    pre_f_skill_effect_index3 = df3.columns.get_loc('pre_f_skill_effect')
    pre_s_skill_effect_index3 = df3.columns.get_loc('pre_s_skill_effect')

    f_skill_detail1_index1 = df1.columns.get_loc('f_skill_detail1')
    s_skill_detail1_index1 = df1.columns.get_loc('s_skill_detail1')
    f_skill_detail2_index1 = df1.columns.get_loc('f_skill_detail2')
    s_skill_detail2_index1 = df1.columns.get_loc('s_skill_detail2')

    f_skill_detail1_index2 = df2.columns.get_loc('f_skill_detail1')
    s_skill_detail1_index2 = df2.columns.get_loc('s_skill_detail1')
    f_skill_detail2_index2 = df2.columns.get_loc('f_skill_detail2')
    s_skill_detail2_index2 = df2.columns.get_loc('s_skill_detail2')

    f_skill_detail1_index3 = df3.columns.get_loc('f_skill_detail1')
    s_skill_detail1_index3 = df3.columns.get_loc('s_skill_detail1')
    f_skill_detail2_index3 = df3.columns.get_loc('f_skill_detail2')
    s_skill_detail2_index3 = df3.columns.get_loc('s_skill_detail2')

    pre_f_skill_detail1_index2 = df2.columns.get_loc('pre_f_skill_detail1')
    pre_s_skill_detail1_index2 = df2.columns.get_loc('pre_s_skill_detail1')
    pre_f_skill_detail2_index2 = df2.columns.get_loc('pre_f_skill_detail2')
    pre_s_skill_detail2_index2 = df2.columns.get_loc('pre_s_skill_detail2')

    pre_f_skill_detail1_index3 = df3.columns.get_loc('pre_f_skill_detail1')
    pre_s_skill_detail1_index3 = df3.columns.get_loc('pre_s_skill_detail1')
    pre_f_skill_detail2_index3 = df3.columns.get_loc('pre_f_skill_detail2')
    pre_s_skill_detail2_index3 = df3.columns.get_loc('pre_s_skill_detail2')

    species_index1 = df1.columns.get_loc('attribute')
    species_index2 = df2.columns.get_loc('attribute')
    species_index3 = df3.columns.get_loc('attribute')

    weapon_index1 = df1.columns.get_loc('name')
    weapon_index2 = df2.columns.get_loc('name')
    weapon_index3 = df3.columns.get_loc('name')
    print(weapon_index1)

    df1 = df1.fillna(0)
    df2 = df2.fillna(0)
    df3 = df3.fillna(0)


    def skill_list(df, i, index1, index2, weapon_index, skill_index, effect_index, species_index):
        sc.normal_attack_check(df, i, index1, skill_index, effect_index, species_index)
        sc.maguna_attack_check(df, i, index1, skill_index, effect_index, species_index)
        sc.ex_attack_check(df, i, index1, skill_index, effect_index, species_index)
        sc.normal_defence_check(df, i, index1, skill_index, effect_index, species_index)
        sc.maguna_defence_check(df, i, index1, skill_index, effect_index, species_index)
        sc.kamui_check(df, i, index1, skill_index, effect_index, species_index)
        sc.haisui_check(df, i, index1, skill_index, effect_index, species_index)
        sc.konshin_check(df, i, index1, skill_index, effect_index, species_index)
        sc.DATA_check(df, i, index1, skill_index, effect_index, species_index)
        sc.critical_check(df, i, index1, skill_index, effect_index, species_index)
        sc.boukun_check(df, i, index1, skill_index, effect_index, species_index)
        sc.hukugou_check(df, i, index1,index2, skill_index, effect_index, species_index)
        sc.bahamut_check(df, i, index1,index2, weapon_index, skill_index, effect_index, species_index)
        sc.cosmos_check(df, i, index1, weapon_index, skill_index)
        sc.omega_check(df, i, index1, index2, weapon_index, skill_index)
        sc.seraph_check(df, i, index1, skill_index, effect_index, species_index)


    for i in range(len(df1)):
        skill_list(df1, i, f_skill_detail1_index1,f_skill_detail2_index1,
            weapon_index1, f_skill_index1, f_skill_effect_index1, species_index1)
        """skill_list(df1, i,
        f_skill_detail2_index1, f_skill_index1, f_skill_effect_index1, species_index1)"""
        skill_list(df1, i, s_skill_detail1_index1,s_skill_detail2_index1,
            weapon_index1, s_skill_index1, s_skill_effect_index1, species_index1)
        """skill_list(df1, i,
        s_skill_detail2_index1, s_skill_index1, s_skill_effect_index1, species_index1)"""


    for i in range(len(df2)):
        skill_list(df2, i,
        f_skill_detail1_index2,f_skill_detail2_index2, weapon_index2, f_skill_index2, f_skill_effect_index2, species_index2)
        skill_list(df2, i,
        s_skill_detail1_index2,s_skill_detail2_index2, weapon_index2, s_skill_index2, s_skill_effect_index2, species_index2)
        """skill_list(df2, i,
        f_skill_detail2_index2, f_skill_index2, f_skill_effect_index2, species_index2)
        skill_list(df2, i,
        s_skill_detail2_index2, s_skill_index2, s_skill_effect_index2, species_index2)"""

        skill_list(df2, i,
        pre_f_skill_detail1_index2,pre_f_skill_detail2_index2, weapon_index2, pre_f_skill_index2, pre_f_skill_effect_index2, species_index2)
        skill_list(df2, i,
        pre_s_skill_detail1_index2,pre_s_skill_detail2_index2, weapon_index2, pre_s_skill_index2, pre_s_skill_effect_index2, species_index2)
        """skill_list(df2, i,
        pre_f_skill_detail2_index2, pre_f_skill_index2, pre_f_skill_effect_index2, species_index2)
        skill_list(df2, i,
        pre_s_skill_detail2_index2, pre_s_skill_index2, pre_s_skill_effect_index2, species_index2)"""


    for i in range(len(df3)):
        skill_list(df3, i,
        f_skill_detail1_index3,f_skill_detail2_index3, weapon_index3, f_skill_index3, f_skill_effect_index3, species_index3)
        skill_list(df3, i,
        s_skill_detail1_index3,s_skill_detail2_index3, weapon_index3, s_skill_index3, s_skill_effect_index3, species_index3)
        """skill_list(df3, i,
        f_skill_detail2_index3, f_skill_index3, f_skill_effect_index3, species_index3)
        skill_list(df3, i,
        s_skill_detail2_index3, s_skill_index3, s_skill_effect_index3, species_index3)"""

        skill_list(df3, i,
        pre_f_skill_detail1_index3,pre_s_skill_detail1_index3, weapon_index3, pre_f_skill_index3, pre_f_skill_effect_index3, species_index3)
        skill_list(df3, i,
        pre_s_skill_detail1_index3,pre_s_skill_detail2_index3, weapon_index3, pre_s_skill_index3, pre_s_skill_effect_index3, species_index3)
        """skill_list(df3, i,
        pre_f_skill_detail2_index3, pre_f_skill_index3, pre_f_skill_effect_index3, species_index3)
        skill_list(df3, i,
        pre_s_skill_detail2_index3, pre_s_skill_index3, pre_s_skill_effect_index3, species_index3)"""


    """df1["f_skill_detail"] = df1["f_skill_detail"].str.split(',')
    df1["s_skill_detail"] = df1["s_skill_detail"].str.split(',')
    df2["f_skill_detail"] = df2["f_skill_detail"].str.split(',')
    df2["s_skill_detail"] = df2["s_skill_detail"].str.split(',')
    df2["pre_f_skill_detail"] = df2["pre_f_skill_detail"].str.split(',')
    df2["pre_s_skill_detail"] = df2["pre_s_skill_detail"].str.split(',')"""


    df1.to_csv("./weapon_data/skill_shaped/skill_effect/weapon_ssr_list_effect.csv", index=None)
    df2.to_csv("./weapon_data/skill_shaped/skill_effect/weapon_ssr_released4_list_effect.csv", index=None)
    df3.to_csv("./weapon_data/skill_shaped/skill_effect/weapon_ssr_released5_list_effect.csv", index=None)

if __name__ == "__main__":
    weapon_csv_making()
