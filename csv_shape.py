import pandas as pd
import numpy as np
import re

def weapon_del():
    df = pd.read_csv("./weapon_ssr.csv")
    df = df.drop(columns=["画像", "奥義", "入手場所加入キャラ等", "カテゴリー"])
    df.columns = ["name", "attribute", "species","rank", "f_skill", "s_skill", "minhp", "minatk",
    "maxhp1", "maxatk1", "release"]

    weapon_name = np.array(df["name"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("]")
        if len(split) != 1:
            weapon_name[i] = split[1]
            # 正規表現でマッチする部分までを探す方法
            #regax = re.compile(r"]")
            #matchObj = re.search(regax, weapon_name[393])
            #print(matchObj.start())

    df["name"] = weapon_name

    df.drop(columns=["release"]).to_csv("weapon_ssr_whole.csv", index=None)
    df = df[df["release"].isnull()]

    df = df.drop(columns=["release"])
    print(df)

    df.to_csv("weapon_ssr_deled.csv", index=None)



def weapon_released4_del():
    columns = ["name", "attribute", "species", "f_skill", "s_skill",
    "maxhp2", "maxatk2", "chara", "date", "quest"]
    df = pd.read_csv("./weapon_ssr_released4.csv", names=columns)
    df = df.drop(columns=["chara", "date", "quest"])

    weapon_name = np.array(df["name"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("]")
        if len(split) != 1:
            weapon_name[i] = split[1]
        # 正規表現でマッチする部分までを探す方法
        #regax = re.compile(r"]")
        #matchObj = re.search(regax, weapon_name[393])
        #print(matchObj.start())

    df["name"] = weapon_name

    print(df)
    df.to_csv("weapon_ssr_released4_deled.csv", index=None)

def weapon_released5_del():
    columns = ["name", "attribute", "species", "f_skill", "s_skill",
    "maxhp3", "maxatk3", "chara", "date", "quest"]
    df = pd.read_csv("./weapon_ssr_released5.csv", names=columns)
    df = df.drop(columns=["chara", "date", "quest"])

    weapon_name = np.array(df["name"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("]")
        if len(split) != 1:
            weapon_name[i] = split[1]
        # 正規表現でマッチする部分までを探す方法
        #regax = re.compile(r"]")
        #matchObj = re.search(regax, weapon_name[393])
        #print(matchObj.start())

    df["name"] = weapon_name
    print(df)
    df.to_csv("weapon_ssr_released5_deled.csv", index=None)

def weapon_rokudo_del():
    columns = ["name", "attribute", "species", "ougi", "f_skill", "s_skill",
    "maxhp", "maxatk","quest"]
    df = pd.read_csv("./weapon_rokudo.csv", names=columns)
    df = df.drop(columns=["ougi", "quest"])

    weapon_name = np.array(df["name"])
    f_skill = np.array(df["f_skill"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("（")
        split1 = f_skill[i].split(" ")
        if len(split) != 1:
            weapon_name[i] = split[0]
            f_skill[i] = split1[0]
        # 正規表現でマッチする部分までを探す方法
        #regax = re.compile(r"]")
        #matchObj = re.search(regax, weapon_name[393])
        #print(matchObj.start())

    df["name"] = weapon_name
    df["f_skill"] = f_skill
    print(df)
    df.to_csv("weapon_rokudo_deled.csv", index=None)

def weapon_baha_del():
    columns = ["name", "attribute", "species", "rank", "ougi", "f_skill","minhp", "minatk",
    "maxhp", "maxatk","quest"]
    df = pd.read_csv("./weapon_baha.csv", names=columns)
    df = df.drop(columns=["ougi", "quest"])

    weapon_name = np.array(df["name"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("]")
        if len(split) != 1:
            weapon_name[i] = split[1]
        # 正規表現でマッチする部分までを探す方法
        #regax = re.compile(r"]")
        #matchObj = re.search(regax, weapon_name[393])
        #print(matchObj.start())

    df["name"] = weapon_name
    print(df)
    df.to_csv("weapon_baha_deled.csv", index=None)


def weapon_omega_del():
    columns = ["name", "species", "f_skill", "maxhp", "maxatk"]
    df = pd.read_csv("./weapon_omega.csv", names=columns)

    weapon_name = np.array(df["name"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("]")
        if len(split) != 1:
            weapon_name[i] = split[1]
        # 正規表現でマッチする部分までを探す方法
        #regax = re.compile(r"]")
        #matchObj = re.search(regax, weapon_name[393])
        #print(matchObj.start())

    df["name"] = weapon_name
    print(df)
    df.to_csv("weapon_omega_deled.csv", index=None)


def weapon_special_del():
    columns = ["name", "attribute", "species","rank", "f_skill", "s_skill", "minhp", "minatk",
    "maxhp1", "maxatk1"]
    df = pd.read_csv("./weapon_special.csv", names=columns)
    print(df)

    weapon_name = np.array(df["name"])
    for i in range(np.size(weapon_name)):
        split = weapon_name[i].split("]")
        if len(split) != 1:
            weapon_name[i] = split[1]
        # 正規表現でマッチする部分までを探す方法
        #regax = re.compile(r"]")
        #matchObj = re.search(regax, weapon_name[393])
        #print(matchObj.start())

    df["name"] = weapon_name
    print(df)
    df.to_csv("weapon_special_deled.csv", index=None)


def weapon_append():
    df1 = pd.read_csv("./weapon_ssr_released5_deled.csv")
    df2 = pd.read_csv("./weapon_ssr_released4_deled.csv")
    df3 = pd.read_csv("./weapon_ssr_deled.csv")
    df4 = pd.read_csv("./weapon_special_deled.csv")

    sp_weapon_name = np.array(df4["name"])
    weapon_name2 = np.array(df2["name"])

    for i in range(np.size(sp_weapon_name)):
        if "ノヴム" in sp_weapon_name[i] or "無垢" in sp_weapon_name[i] or "コスモス" in sp_weapon_name[i]:
            array = pd.Series(list(df4.iloc[i]), index = df3.columns)
            df3 = df3.append(array, ignore_index=True)
            print(array)
        if "六道" in sp_weapon_name[i] or "焔ノ太刀" == sp_weapon_name[i] or "シャフレワル" == sp_weapon_name[i]:
            array = pd.Series(list(df4.iloc[i]), index = df3.columns)
            df3 = df3.append(array, ignore_index=True)
            print(array)

        if "オメガ" in sp_weapon_name[i]:
            array = pd.Series(list(df4.iloc[i]), index = df3.columns)
            df3 = df3.append(array, ignore_index=True)
            print(array)

        if "フツルス" in sp_weapon_name[i] or "ヘルムヴィーゲ" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)

        if "ベルセルク・オクス" in sp_weapon_name[i] or "聖者の行進" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            list_4[1] = "-"
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)

        if "デモンズシャフト" in sp_weapon_name[i] or "浄瑠璃" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            list_4[1] = "-"
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)

        if "チャンピオンベルト" in sp_weapon_name[i] or "メース" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            list_4[1] = "-"
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)

        if "シャンゼリゼ" in sp_weapon_name[i] or "無銘金重" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            list_4[1] = "-"
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)

        if "テトラストリーマ" in sp_weapon_name[i] or "マッドネスシリンジ" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            list_4[1] = "-"
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)

        if "真" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)


        if "ラスト・シャフレワル" in sp_weapon_name[i] or "極マリシ烈火ノ太刀" in sp_weapon_name[i]:
            list_4 = list(df4.iloc[i])
            list_4.pop(3)
            list_4.pop(5)
            list_4.pop(5)
            array = pd.Series(list_4, index = df2.columns)
            df2 = df2.append(array, ignore_index=True)



    print(df2)
    df3.to_csv("./weapon_ssr_deled.csv", index=None)
    df2.to_csv("./weapon_ssr_released4_deled.csv", index=None)



if __name__ == "__main__":
    weapon_del()
    weapon_released4_del()
    weapon_released5_del()
    weapon_rokudo_del()
    weapon_baha_del()
    weapon_omega_del()
    weapon_special_del()
    weapon_append()
