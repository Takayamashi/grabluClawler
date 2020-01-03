from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import requests
import chardet
import pandas as pd

released5_list = [22, 25]

def weapon_ssr_list():
    url = "http://gbf-wiki.com/?%C9%F0%B4%EF%C1%B4%A5%EC%A5%A2%A5%EA%A5%C6%A5%A3%B0%EC%CD%F7#q015ff29"
    r = requests.get(url)
    print(r.encoding)
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.original_encoding)

    table = soup.findAll("table", {"class":"style_table"})[2]
    rows = table.findAll("tr")

    csvFile = open("weapon_ssr.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    finally:
        csvFile.close()

def weapon_ssr_list_released4():
    url = "http://gbf-wiki.com/index.php?%BA%C7%BD%AA%BE%E5%B8%C2%B2%F2%CA%FC%C9%F0%B4%EF"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_ssr_released4.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(3, 31, 1):
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        k=0

        for row in rows:
            k=k+1
            if (k <= 1 or i== 22 or i==25):
                continue

            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            if (i==3 or i==4):
                csvRow.pop(3)
            if (i>=26):
                csvRow.pop(0)
                if (i==27):
                    csvRow.pop(2)
                    csvRow.insert(1, "-")
                elif(i==26):
                    csvRow.pop(3)
                    csvRow.insert(4, "")
                else:
                    csvRow.pop(3)
            writer.writerow(csvRow)

def weapon_ssr_list_released5():
    url = "http://gbf-wiki.com/index.php?%BA%C7%BD%AA%BE%E5%B8%C2%B2%F2%CA%FC%C9%F0%B4%EF"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_ssr_released5.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in released5_list:
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            k=k+1
            if k<=1:
                continue
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)

def weapon_skill_list():
    url = "http://gbf-wiki.com/index.php?%A5%B9%A5%AD%A5%EB%B0%EC%CD%F7#tennkounokoujin"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_skill_list.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(1, 5, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            k=k+1
            if k<=1:
                continue
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)


def weapon_rokudo():
    url = "http://gbf-wiki.com/index.php?%C9%F0%B4%EF%B3%B5%CD%D7%2F%CF%BB%C6%BB%C9%F0%B4%EF"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_rokudo.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(2, 4, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        if i==3:
            for row in rows:
                k=k+1
                if k==4 or k<=2 or k==6 or k==7 or k==9 or k==10 or k==12 or k==14 or k==16 or k==18 or k==20:
                    continue
                csvRow = []
                for cell in row.findAll(["td", "th"]):
                    csvRow.append(cell.get_text())
                csvRow.insert(6, "0")
                writer.writerow(csvRow)

        else:
            for row in rows:
                k=k+1
                if k<=1:
                    continue
                csvRow = []
                for cell in row.findAll(["td", "th"]):
                    csvRow.append(cell.get_text())
                csvRow.insert(6, "0")
                writer.writerow(csvRow)

def weapon_baha():
    url = "http://gbf-wiki.com/index.php?%C9%F0%B4%EF%B3%B5%CD%D7%2F%A5%D0%A5%CF%A5%E0%A1%BC%A5%C8%A5%A6%A5%A7%A5%DD%A5%F3"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_baha.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(8, 11, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            k=k+1
            if k<=1:
                continue
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)

def weapon_omega():
    url = "http://gbf-wiki.com/index.php?%C9%F0%B4%EF%B3%B5%CD%D7%2F%A5%AA%A5%E1%A5%AC%A5%A6%A5%A7%A5%DD%A5%F3"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_omega.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(2, 4, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            k=k+1
            if k<=1:
                continue

            if k==2:
                csvRow = []
                for cell in row.findAll(["td", "th"]):
                    csvRow.append(cell.get_text())
                csvRow.pop(2)
                csvRow.pop(2)
                csvRow.pop(5)
                csvRow.insert(3, "0")
                writer.writerow(csvRow)

            else:
                csvRow = []
                for cell in row.findAll(["td", "th"]):
                    csvRow.append(cell.get_text())
                csvRow.insert(3, "0")
                writer.writerow(csvRow)


def weapon_special():
    url = "http://gbf-wiki.com/index.php?%C9%F0%B4%EFSSR%2F%C6%C3%BC%EC%C9%F0%B4%EF"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_special.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in range(4, 10, 1):
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        if i!= 7:
            if i==8:
                for row in rows:
                    k=k+1
                    if k<=1:
                        continue

                    if k==2 or k==12:
                        csvRow = []
                        for cell in row.findAll(["td", "th"]):
                            csvRow.append(cell.get_text())
                        csvRow.pop(4)
                        csvRow.insert(5, "0")
                        csvRow.pop(10)
                        csvRow.pop(10)
                        csvRow.pop(10)
                        csvRow.insert(2, "-")
                        writer.writerow(csvRow)

                    else:
                        csvRow = []
                        for cell in row.findAll(["td", "th"]):
                            csvRow.append(cell.get_text())
                        csvRow.insert(5, "0")
                        csvRow.pop(10)
                        csvRow.insert(2, "")
                        writer.writerow(csvRow)

            elif i==4:
                for row in rows:
                    k=k+1
                    if k<=1:
                        continue
                    csvRow = []
                    for cell in row.findAll(["td", "th"]):
                        csvRow.append(cell.get_text())

                    csvRow.pop(12)
                    csvRow.pop(12)
                    csvRow.pop(5)
                    writer.writerow(csvRow)

            elif i==9:
                for row in rows:
                    k=k+1
                    if k<=1:
                        continue
                    csvRow = []
                    for cell in row.findAll(["td", "th"]):
                        csvRow.append(cell.get_text())
                    csvRow.pop(12)
                    csvRow.pop(12)
                    csvRow.pop(12)
                    csvRow.pop(12)
                    csvRow.pop(5)
                    writer.writerow(csvRow)

            else:
                for row in rows:
                    k=k+1
                    if k<=1:
                        continue

                    else:
                        csvRow = []
                        for cell in row.findAll(["td", "th"]):
                            csvRow.append(cell.get_text())
                        csvRow.pop(5)
                        csvRow.pop(11)
                        csvRow.pop(11)
                        csvRow.pop(11)
                        writer.writerow(csvRow)


def weapon_job():
    url = "http://gbf-wiki.com/index.php?%BA%C7%BD%AA%BE%E5%B8%C2%B2%F2%CA%FC%C9%F0%B4%EF"
    r = requests.get(url)
    print(r.encoding)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
    print(soup.original_encoding)
    csvFile = open("weapon_job.csv", "wt", newline = '', encoding = "utf-8")
    writer = csv.writer(csvFile)

    for i in released5_list:
        k=0
        table = soup.findAll("table", {"class":"style_table"})[i]
        rows = table.findAll("tr")
        for row in rows:
            k=k+1
            if k<=1:
                continue
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)



if __name__ == "__main__":
    #weapon_ssr_list()
    #weapon_ssr_list_released4()
    #weapon_ssr_list_released5()
    #weapon_skill_list()
    #weapon_rokudo()
    #weapon_baha()
    #weapon_omega()
    weapon_special()
