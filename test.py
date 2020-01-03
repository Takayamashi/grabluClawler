import pandas as pd
import numpy as np
import re
import skill_checker as sc
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import requests
import chardet
import pandas as pd

url = "http://gbf-wiki.com/index.php?%BA%C7%BD%AA%BE%E5%B8%C2%B2%F2%CA%FC%C9%F0%B4%EF"
r = requests.get(url)
print(r.encoding)
soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(r.content.decode("euc-jp", "ignore"), "html.parser")
print(soup.original_encoding)
csvFile = open("test.csv", "wt", newline = '', encoding = "utf-8")
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
