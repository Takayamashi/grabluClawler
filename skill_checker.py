import numpy as np
import pandas as pd

df_na = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_normal_attack.csv")
df_ma = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_maguna_attack.csv")
df_exa = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_ex_attack.csv")
df_nd = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_normal_defence.csv")
df_md = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_maguna_defence.csv")
df_kamui = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_kamui.csv")
df_haisui = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_haisui.csv")
df_konshin = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_konshin.csv")
df_DATA = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_DATA.csv")
df_critical = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_critical.csv")
df_bahamut = pd.read_csv("./skill_effect/skill_effect_shaped/skill_effect_bahamut.csv")

skill_s = [""]
skill_amount_list1 = ["紅蓮", "霧氷", "乱気", "地裂", "天光", "奈落"]
skill_amount_list2 = ["業火", "渦潮", "竜巻", "大地", "雷電", "憎悪"]
skill_amount_list3 = ["火", "水", "風", "土", "光", "闇"]
skill_maguna_list = ["機炎", "海神", "嵐竜", "創樹", "騎解", "黒霧"]

def element_check(skill, skill_effect, species):
    element = skill_effect.split("属性")
    element = element[0]

    if len(element) > 1:
        element = species

    """if ("火" in skill) or ("業火" in skill) or ("紅蓮" in skill) or ("機炎" in skill):
        element = "火"

    elif ("水" in skill) or ("渦潮" in skill) or ("霧氷" in skill) or ("海神" in skill):
        element = "水"

    elif ("風" in skill) or ("竜巻" in skill) or ("乱気" in skill) or ("嵐竜" in skill):
        element = "風"

    elif ("土" in skill) or ("大地" in skill) or ("地裂" in skill) or ("創樹" in skill):
        element = "土"

    elif ("光" in skill) or ("雷電" in skill) or ("天光" in skill) or ("騎解" in skill):
        element = "光"

    elif ("闇" in skill) or ("憎悪" in skill) or ("奈落" in skill) or ("黒霧" in skill):
        element = "闇"""

    if "武器" in element:
        element = species


    return element

def element_check_no_effect(skill):
    element = ""

    if ("火" in skill) or ("業火" in skill) or ("紅蓮" in skill) or ("機炎" in skill) or ("ミカエル" in skill):
        element = "火"

    if ("水" in skill) or ("渦潮" in skill) or ("霧氷" in skill) or ("海神" in skill) or ("ガブリエル" in skill):
        element = "水"

    if ("風" in skill) or ("竜巻" in skill) or ("乱気" in skill) or ("嵐竜" in skill)or ("ラファエル" in skill):
        element = "風"

    if ("土" in skill) or ("大地" in skill) or ("地裂" in skill) or ("創樹" in skill) or ("ウリエル" in skill):
        element = "土"

    if ("光" in skill) or ("雷電" in skill) or ("天光" in skill) or ("騎解" in skill):
        element = "光"

    if ("闇" in skill) or ("憎悪" in skill) or ("奈落" in skill) or ("黒霧" in skill):
        element = "闇"


    return element


def normal_attack_check(df, i, index, skill_index, effect_index, species_index):
    skill = str(df.iloc[i,skill_index])
    skill_effect = str(df.iloc[i,effect_index])
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if "攻刃" in skill:
            if (type(skill_effect) is str):
                if "攻撃力上昇" in skill_effect:
                    for skill_amount in skill_amount_list3:
                        if "(小)" in skill_effect or skill_amount in skill:
                            element = element_check(skill, skill_effect, species)
                            list = df_na.loc[0].values.tolist()
                            list[0] = "通常攻刃(小)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                    for skill_amount in skill_amount_list2:
                        if "(中)" in skill_effect or skill_amount in skill:
                            element = element_check(skill, skill_effect, species)
                            list = df_na.loc[1].values.tolist()
                            list[0] = "通常攻刃(中)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                    for skill_amount in skill_amount_list1:
                        if "(大)" in skill_effect or skill_amount in skill:
                            element = element_check(skill, skill_effect, species)
                            list = df_na.loc[2].values.tolist()
                            list[0] = "通常攻刃(大)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res


                if "攻刃"+"II" in skill:
                    element = element_check(skill, skill_effect, species)
                    list = df_na.loc[3].values.tolist()
                    list[0] = "通常攻刃Ⅱ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res
                if "攻刃"+"III" in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_na.loc[4].values.tolist()
                    list[0] = "通常攻刃Ⅲ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            else:
                for skill_amount in skill_amount_list3:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)
                        list = df_na.loc[0].values.tolist()
                        list[0] = "通常攻刃(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)
                        list = df_na.loc[1].values.tolist()
                        list[0] = "通常攻刃(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list1:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)
                        list = df_na.loc[2].values.tolist()
                        list[0] = "通常攻刃(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res


                if "攻刃"+"II" in skill:
                    element = element_check(skill, skill_effect, species)
                    list = df_na.loc[3].values.tolist()
                    list[0] = "通常攻刃Ⅱ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res
                if "攻刃"+"III" in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_na.loc[4].values.tolist()
                    list[0] = "通常攻刃Ⅲ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

        if (type(skill_effect) is str):
            if ("方陣" not in skill) and ("攻撃力上昇(大)" in skill_effect) and ("属性" in skill_effect) and ("攻刃"+"II" not in skill):
                element = element_check(skill, skill_effect, species)
                list = df_na.loc[2].values.tolist()
                list[0] = "通常攻刃(大)"
                list.insert(0, element)
                res = ",".join(map(str, list))
                df.iloc[i, index] = res


def maguna_attack_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if "方陣" in skill:
            if (type(skill_effect) is str):
                if "攻撃力上昇" in skill_effect:
                    if "(中)" in skill_effect:
                        element = element_check(skill, skill_effect, species)

                        list = df_ma.loc[0].values.tolist()
                        list[0] = "マグナ攻刃"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                    if "(大)" in skill_effect:
                        element = element_check(skill, skill_effect, species)

                        list = df_ma.loc[1].values.tolist()
                        list[0] = "マグナ攻刃Ⅱ"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res


            if "攻刃" in skill:
                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_ma.loc[0].values.tolist()
                    list[0] = "マグナ攻刃"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(大)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_ma.loc[1].values.tolist()
                    list[0] = "マグナ攻刃Ⅱ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

def ex_attack_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill_effect) is str):
        if "EX小" in skill_effect:
            element = element_check(skill, skill_effect, species)
            list = df_exa.loc[0].values.tolist()
            list[0] = "EX攻刃(小)"
            list.insert(0, element)
            res = ",".join(map(str, list))
            df.iloc[i, index] = res

        if "EX中" in skill_effect:
            element = element_check(skill, skill_effect, species)
            list = df_exa.loc[1].values.tolist()
            list[0] = "EX攻刃(中)"
            list.insert(0, element)
            res = ",".join(map(str, list))
            df.iloc[i, index] = res

        if "EX大" in skill_effect:
            element = element_check(skill, skill_effect, species)
            list = df_exa.loc[2].values.tolist()
            list[0] = "EX攻刃(大)"
            list.insert(0, element)
            res = ",".join(map(str, list))
            df.iloc[i, index] = res

        if "EX特大" in skill_effect:
            element = element_check(skill, skill_effect, species)
            list = df_exa.loc[3].values.tolist()
            list[0] = "EX攻刃(特大)"
            list.insert(0, element)
            res = ",".join(map(str, list))
            df.iloc[i, index] = res


def normal_defence_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if (type(skill_effect) is str):
            if "守護" in skill:
                if "最大HP上昇" in skill_effect:
                    for skill_amount in skill_amount_list3:
                        if "(小)" in skill_effect or skill_amount in skill:
                            element = element_check(skill, skill_effect, species)
                            list = df_nd.loc[0].values.tolist()
                            list[0] = "通常守護(小)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                    for skill_amount in skill_amount_list2:
                        if "(中)" in skill_effect or skill_amount in skill:
                            element = element_check(skill, skill_effect, species)
                            list = df_nd.loc[1].values.tolist()
                            list[0] = "通常守護(中)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                    for skill_amount in skill_amount_list1:
                        if "(大)" in skill_effect or skill_amount in skill:
                            element = element_check(skill, skill_effect, species)
                            list = df_nd.loc[2].values.tolist()
                            list[0] = "通常守護(大)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

        else:
            if "守護" in skill:
                    for skill_amount in skill_amount_list3:
                        if skill_amount in skill:
                            element = element_check_no_effect(skill)
                            list = df_nd.loc[0].values.tolist()
                            list[0] = "通常守護(小)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                    for skill_amount in skill_amount_list2:
                        if skill_amount in skill:
                            element = element_check_no_effect(skill)
                            list = df_nd.loc[1].values.tolist()
                            list[0] = "通常守護(中)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                    for skill_amount in skill_amount_list1:
                        if skill_amount in skill:
                            element = element_check_no_effect(skill)
                            list = df_nd.loc[2].values.tolist()
                            list[0] = "通常守護(大)"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res


        if "守護"+"II" in skill:
            element = element_check(skill, skill_effect, species)
            list = df_nd.loc[4].values.tolist()

            list[0] = "通常守護Ⅱ"
            list.insert(0, element)
            res = ",".join(map(str, list))
            df.iloc[i, index] = res

def maguna_defence_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if "方陣" in skill:
            if "守護" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_md.loc[0].values.tolist()
                    list[0] = "マグナ守護(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_md.loc[1].values.tolist()
                    list[0] = "マグナ守護(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(大)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_md.loc[2].values.tolist()
                    list[0] = "マグナ守護(大)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "II" in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_md.loc[4].values.tolist()
                    list[0] = "マグナ守護Ⅱ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

def kamui_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if "神威" in skill:
            if (type(skill_effect) is str):
                for skill_amount in skill_amount_list3:
                    if "(小)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_kamui.loc[0].values.tolist()
                        list[0] = "通常神威(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if "(中)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_kamui.loc[1].values.tolist()
                        list[0] = "通常神威(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res
            else:
                for skill_amount in skill_amount_list3:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)

                        list = df_kamui.loc[0].values.tolist()
                        list[0] = "通常神威(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)

                        list = df_kamui.loc[1].values.tolist()
                        list[0] = "通常神威(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res


            if "方陣" in skill:
                element = element_check(skill, skill_effect, species)

                list = df_kamui.loc[2].values.tolist()
                list[0] = "マグナ神威"
                list.insert(0, element)
                res = ",".join(map(str, list))
                df.iloc[i, index] = res

                if "II" in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_kamui.loc[3].values.tolist()
                    list[0] = "マグナ神威Ⅱ"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

def haisui_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if "背水" in skill:
            for skill_amount in skill_amount_list3:
                if "(小)" in skill_effect or skill_amount in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_haisui.loc[0].values.tolist()
                    list[0] = "通常背水(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            for skill_amount in skill_amount_list2:
                if "(中)" in skill_effect or skill_amount in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_haisui.loc[1].values.tolist()
                    list[0] = "通常背水(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            for skill_amount in skill_amount_list1:
                if "(大)" in skill_effect or skill_amount in skill:
                    element = element_check(skill, skill_effect, species)

                    list = df_haisui.loc[2].values.tolist()
                    list[0] = "通常背水(大)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            if "方陣" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_haisui.loc[0].values.tolist()
                    list[0] = "マグナ背水(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_haisui.loc[1].values.tolist()
                    list[0] = "マグナ背水(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(大)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_haisui.loc[2].values.tolist()
                    list[0] = "マグナ背水(大)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

def konshin_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if "渾身" in skill:
            if (type(skill_effect) is str):
                for skill_amount in skill_amount_list1:
                    if "(大)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)
                        list = df_konshin.loc[0].values.tolist()
                        list[0] = "通常渾身(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if "(中)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)
                        list = df_konshin.loc[1].values.tolist()
                        list[0] = "通常渾身(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res
            else:
                for skill_amount in skill_amount_list1:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)
                        list = df_konshin.loc[0].values.tolist()
                        list[0] = "通常渾身(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)
                        list = df_konshin.loc[1].values.tolist()
                        list[0] = "通常渾身(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

            if "方陣" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_konshin.loc[0].values.tolist()
                    list[0] = "マグナ渾身(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_konshin.loc[1].values.tolist()
                    list[0] = "マグナ渾身(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res


def DATA_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = str(df.iloc[i,species_index])

    if (type(skill) is str):
        if (type(skill_effect) is str):
            if "二手" in skill:
                for skill_amount in skill_amount_list3:
                    if "(小)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[2].values.tolist()
                        list[0] = "通常二手(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if "(中)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[3].values.tolist()
                        list[0] = "通常二手(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list1:
                    if "(大)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[4].values.tolist()
                        list[0] = "通常二手(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

            if "三手" in skill:
                for skill_amount in skill_amount_list3:
                    if "(小)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[2].values.tolist()
                        list[0] = "通常三手(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if "(中)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[3].values.tolist()
                        list[0] = "通常三手(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list1:
                    if "(大)" in skill_effect or skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[4].values.tolist()
                        list[0] = "通常三手(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

        else:
            if "二手" in skill:
                for skill_amount in skill_amount_list3:
                    if skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[2].values.tolist()
                        list[0] = "通常二手(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[3].values.tolist()
                        list[0] = "通常二手(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list1:
                    if skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[4].values.tolist()
                        list[0] = "通常二手(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

            if "三手" in skill:
                for skill_amount in skill_amount_list3:
                    if skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[2].values.tolist()
                        list[0] = "通常三手(小)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list2:
                    if skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[3].values.tolist()
                        list[0] = "通常三手(中)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

                for skill_amount in skill_amount_list1:
                    if skill_amount in skill:
                        element = element_check(skill, skill_effect, species)

                        list = df_DATA.loc[4].values.tolist()
                        list[0] = "通常三手(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

        if "方陣" in skill:
            if "破壊" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[1].values.tolist()
                    list[0] = "マグナ破壊"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            if "二手" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[2].values.tolist()
                    list[0] = "マグナ二手(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[3].values.tolist()
                    list[0] = "マグナ二手(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(大)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[4].values.tolist()
                    list[0] = "マグナ二手(大)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            if "三手" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[2].values.tolist()
                    list[0] = "マグナ三手(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[3].values.tolist()
                    list[0] = "マグナ三手(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(大)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_DATA.loc[4].values.tolist()
                    list[0] = "マグナ三手(大)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

            if "破壊" in skill:
                element = element_check_no_effect(skill)

                list = df_DATA.loc[1].values.tolist()
                list[0] = "マグナ破壊"
                list.insert(0, element)
                res = ",".join(map(str, list))
                df.iloc[i, index] = res

def critical_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = df.iloc[i,species_index]

    if (type(skill) is str):
        if (type(skill_effect) is str):
            if "技巧" in skill:
                if "(小)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_critical.loc[0].values.tolist()
                    list[0] = "通常技巧(小)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(中)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_critical.loc[1].values.tolist()
                    list[0] = "通常技巧(中)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

                if "(大)" in skill_effect:
                    element = element_check(skill, skill_effect, species)

                    list = df_critical.loc[2].values.tolist()
                    list[0] = "通常技巧(大)"
                    list.insert(0, element)
                    res = ",".join(map(str, list))
                    df.iloc[i, index] = res

        if "方陣" in skill:
            if (type(skill_effect) is str):
                if "技巧" in skill:
                    if "(大)" in skill_effect:
                        element = element_check(skill, skill_effect, species)

                        list = df_critical.loc[3].values.tolist()
                        list[0] = "マグナ技巧(大)"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res


def boukun_check(df, i, index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = df.iloc[i,species_index]

    if (type(skill) is str):
            if "暴君" in skill:
                for skill_amount in skill_amount_list1:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)

                        list = df_na.loc[2].values.tolist()
                        list[0] = "通常暴君"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

            if "暴君II" in skill:
                for skill_amount in skill_amount_list1:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)

                        list = df_exa.loc[3].values.tolist()
                        list[0] = "通常暴君Ⅱ"
                        list.insert(0, element)
                        res = ",".join(map(str, list))
                        df.iloc[i, index] = res

            if "方陣" in skill:
                if "暴君" in skill:
                    for skill_amount in skill_maguna_list:
                        if skill_amount in skill:
                            element = element_check_no_effect(skill)

                            list = df_na.loc[2].values.tolist()
                            list[0] = "マグナ暴君"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res

                if "暴君II" in skill:
                    for skill_amount in skill_maguna_list:
                        if skill_amount in skill:
                            element = element_check_no_effect(skill)

                            list = df_exa.loc[3].values.tolist()
                            list[0] = "マグナ暴君Ⅱ"
                            list.insert(0, element)
                            res = ",".join(map(str, list))
                            df.iloc[i, index] = res


def hukugou_check(df, i, index1,index2, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = df.iloc[i,species_index]

    if (type(skill) is str):
        if "無双" in skill:
                element = element_check_no_effect(skill)

                list1 = df_na.loc[1].values.tolist()
                list1[0] = "通常無双"
                list1.insert(0, element)
                res = ",".join(map(str, list1))
                df.iloc[i, index1] = res

                list2 = df_DATA.loc[3].values.tolist()
                list2[0] = "通常無双"
                list2.insert(0, element)
                res = ",".join(map(str, list2))
                df.iloc[i, index2] = res


        if "無双II" in skill:
            element = element_check_no_effect(skill)

            list1 = df_na.loc[3].values.tolist()
            list1[0] = "通常無双Ⅱ"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

            list2 = df_DATA.loc[5].values.tolist()
            list2[0] = "通常無双Ⅱ"
            list2.insert(0, element)
            res = ",".join(map(str, list2))
            df.iloc[i, index2] = res

        if "方陣" in skill:
            if "無双" in skill:
                element = element_check_no_effect(skill)

                list1 = df_ma.loc[0].values.tolist()
                list1[0] = "マグナ無双"
                list1.insert(0, element)
                res = ",".join(map(str, list1))
                df.iloc[i, index1] = res

                list2 = df_DATA.loc[3].values.tolist()
                list2[0] = "マグナ無双"
                list2.insert(0, element)
                res = ",".join(map(str, list2))
                df.iloc[i, index2] = res


        if "乱舞" in skill:
            element = element_check_no_effect(skill)

            list1 = df_na.loc[0].values.tolist()
            list1[0] = "通常乱舞"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

            list2 = df_DATA.loc[0].values.tolist()
            list2[0] = "通常乱舞"
            list2.insert(0, element)
            res = ",".join(map(str, list2))
            df.iloc[i, index2] = res


        if "克己" in skill:
            element = element_check_no_effect(skill)

            list1 = df_DATA.loc[3].values.tolist()
            list1[0] = "通常克己"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

            list2 = df_critical.loc[1].values.tolist()
            list2[0] = "通常克己"
            list2.insert(0, element)
            res = ",".join(map(str, list2))
            df.iloc[i, index2] = res

        if "刹那" in skill:
            for skill_amount in skill_amount_list3:
                if skill_amount in skill:
                    element = element_check_no_effect(skill)

                    list1 = df_na.loc[0].values.tolist()
                    list1[0] = "通常刹那(小)"
                    list1.insert(0, element)
                    res = ",".join(map(str, list1))
                    df.iloc[i, index1] = res

                    list2 = df_critical.loc[0].values.tolist()
                    list2[0] = "通常刹那(小)"
                    list2.insert(0, element)
                    res = ",".join(map(str, list2))
                    df.iloc[i, index2] = res

            for skill_amount in skill_amount_list2:
                if skill_amount in skill:
                    element = element_check_no_effect(skill)

                    list1 = df_na.loc[1].values.tolist()
                    list1[0] = "通常刹那(中)"
                    list1.insert(0, element)
                    res = ",".join(map(str, list1))
                    df.iloc[i, index1] = res

                    list2 = df_critical.loc[0].values.tolist()
                    list2[0] = "通常刹那(中)"
                    list2.insert(0, element)
                    res = ",".join(map(str, list2))
                    df.iloc[i, index2] = res


            if "方陣" in skill:
                for skill_amount in skill_maguna_list:
                    if skill_amount in skill:
                        element = element_check_no_effect(skill)

                        list1 = df_ma.loc[0].values.tolist()
                        list1[0] = "マグナ刹那(中)"
                        list1.insert(0, element)
                        res = ",".join(map(str, list1))
                        df.iloc[i, index1] = res

                        list2 = df_critical.loc[1].values.tolist()
                        list2[0] = "マグナ刹那(中)"
                        list2.insert(0, element)
                        res = ",".join(map(str, list2))
                        df.iloc[i, index2] = res

        if "方陣" in skill:
            if "軍神" in skill:
                element = element_check_no_effect(skill)

                list1 = df_nd.loc[0].values.tolist()
                list1[0] = "マグナ軍神"
                list1.insert(0, element)
                res = ",".join(map(str, list1))
                df.iloc[i, index1] = res

                list2 = df_DATA.loc[2].values.tolist()
                list2[0] = "マグナ軍神"
                list2.insert(0, element)
                res = ",".join(map(str, list2))
                df.iloc[i, index2] = res


        if "方陣" in skill:
            if "意思" in skill:
                element = element_check_no_effect(skill)

                list1 = df_critical.loc[1].values.tolist()
                list1[0] = "マグナ技巧(中)"
                list1.insert(0, element)
                res = ",".join(map(str, list1))
                df.iloc[i, index1] = res


        if "方陣" in skill:
            if "不可侵" in skill:
                element = element_check_no_effect(skill)

                list1 = df_md.loc[0].values.tolist()
                list1[0] = "マグナ守護(小)"
                list1.insert(0, element)
                res = ",".join(map(str, list1))
                df.iloc[i, index1] = res


        if "刮目" in skill:
            element = element_check_no_effect(skill)

            list1 = df_DATA.loc[2].values.tolist()
            list1[0] = "通常二手(小)"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res


            if "方陣" in skill:
                element = element_check_no_effect(skill)

                list1 = df_DATA.loc[0].values.tolist()
                list1[0] = "マグナ二手(小)"
                list1.insert(0, element)
                res = ",".join(map(str, list1))
                df.iloc[i, index1] = res




def bahamut_check(df, i, index1,index2, weapon_index, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = df.iloc[i,species_index]
    weapon = df.iloc[i,weapon_index]

    if (type(skill) is str):
        if "ウィス" in skill:
            element = "0"

            list1 = df_bahamut.loc[0].values.tolist()
            list1[0] = "バハ攻撃"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

        if "ルーベル" in skill or "ケルレウス" in skill and "無垢" not in weapon and "オメガ" not in weapon:
            element = "0"
            list1 = df_bahamut.loc[1].values.tolist()
            list1[0] = "バハ攻撃/HP"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

            list2 = df_bahamut.loc[1].values.tolist()
            list2[0] = "バハ攻撃/HP"
            list2.insert(0, element)
            res = ",".join(map(str, list2))
            df.iloc[i, index2] = res


        if "メンス" in skill:
            element = "0"
            list1 = df_bahamut.loc[4].values.tolist()
            list1[0] = "バハHP"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

        if "コンキリオ" in skill and "ルーベル" not in skill and "ケルレウス" not in skill:
            element = "0"
            list1 = df_bahamut.loc[2].values.tolist()
            list1[0] = "バハ攻撃/HP"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

            list2 = df_bahamut.loc[3].values.tolist()
            list2[0] = "バハ攻撃/HP"
            list2.insert(0, element)
            res = ",".join(map(str, list2))
            df.iloc[i, index2] = res

        if "ビス" in skill:
            element = "0"
            list1 = df_bahamut.loc[5].values.tolist()
            list1[0] = "バハDATA"
            list1.insert(0, element)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res


def omega_check(df, i, index1, index2, weapon_index, skill_index):
    skill = df.iloc[i,skill_index]
    weapon = df.iloc[i,weapon_index]

    if "無垢" in weapon or "オメガ" in weapon and skill != "0":
        if skill != "0":
            element = "なし"

            list1 = [0,0,0,0,0,0,0,0,0,0,20]
            list1[0] = "オメガ基礎"
            list1.insert(0, element)
            for j in range(10):
                list1.append(0)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res

            list2 = [0,0,0,0,0,0,0,0,0,0,10]
            list2[0] = "オメガ基礎"
            list2.insert(0, element)
            for j in range(10):
                list2.append(0)
            res = ",".join(map(str, list2))
            df.iloc[i, index2] = res
            print(df.iloc[i, index2])
            print(i, index2)
            print(skill)

def cosmos_check(df, i, index1, weapon_index, skill_index):
    skill = df.iloc[i,skill_index]
    weapon = df.iloc[i,weapon_index]

    if "コスモス" in weapon and skill != "0":
        if "スタンス" not in skill:
            element = "なし"

            list1 = [0]
            list1[0] = "コスモス"
            list1.insert(0, element)
            for j in range(20):
                list1.append(0)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res


def seraph_check(df, i, index1, skill_index, effect_index, species_index):
    skill = df.iloc[i,skill_index]
    skill_effect = df.iloc[i,effect_index]
    species = df.iloc[i,species_index]

    if (type(skill) is str):
        if "祝福II" in skill:
            element = element_check_no_effect(skill)

            list1 = [0]
            list1[0] = "天司Ⅱ"
            list1.insert(0, element)
            for j in range(20):
                list1.append(0)
            res = ",".join(map(str, list1))
            df.iloc[i, index1] = res
