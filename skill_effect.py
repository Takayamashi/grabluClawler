from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import requests
import chardet
import pandas as pd

url = "http://gbf-wiki.com/index.php?%A5%B9%A5%AD%A5%EB%B8%FA%B2%CC"
r = requests.get(url)
print(r.encoding)
# soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")

def skill_effect_normal_attack():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_normal_attack.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[1]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0):
            k = k+1
            continue
        k = k+1
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_maguna_attack():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_maguna_attack.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[2]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0):
            k = k+1
            continue

        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_ex_attack():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_ex_attack.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[3]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0):
            k = k+1
            continue
        k = k+1
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_normal_defence():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_normal_defence.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(4, 5, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            if(k==0):
                k = k+1
                continue
            k = k+1
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)

def skill_effect_maguna_defence():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_maguna_defence.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(5, 6, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            if(k==0):
                k = k+1
                continue
            k = k+1
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)

def skill_effect_bahamut():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_bahamut.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(6, 10, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            if(k==0):
                k = k+1
                continue
            k = k+1
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)

def skill_effect_kamui():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_kamui.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[10]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0):
            k = k+1
            continue
        k = k+1
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_haisui():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_haisui.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[11]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0):
            k = k+1
            continue
        k = k+1
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_konshin():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_konshin.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[14]
    rows = table.findAll("tr")
    k = 0

    for row in rows:
        if(k==0):
            k = k+1
            continue
        k = k+1

        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_DATA():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_DATA.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[17]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0 or k==1):
            k+=1
            continue
        k = k+1
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

def skill_effect_critical():

    print(soup.original_encoding)
    csvFile = open("./skill_effect/skill_effect_critical.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    table = soup.findAll("table", {"class":"style_table"})[18]
    rows = table.findAll("tr")
    k=0
    for row in rows:
        if(k==0 or k==1 or k>5):
            k+=1
            continue
        k = k+1
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())

        print(csvRow)
        if (k==3):
            csvRow.pop(0)
        csvRow.pop(4)
        for i in range(8):
            csvRow.insert(2,"")
        for i in range(4):
            csvRow.insert(11,"")

        writer.writerow(csvRow)

if __name__ == "__main__":
    skill_effect_normal_attack()
    skill_effect_maguna_attack()
    skill_effect_ex_attack()
    skill_effect_normal_defence()
    skill_effect_maguna_defence()
    skill_effect_bahamut()
    skill_effect_kamui()
    skill_effect_haisui()
    skill_effect_konshin()
    skill_effect_DATA()
    skill_effect_critical()
