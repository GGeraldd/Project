import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

countries = pd.read_excel("IMVA.xlsx")

# 5iv (filtering asia countries from excel)
Asia1 = countries[['Periods', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ',
                   ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
                   ' Hong Kong ', ' China ', ' Taiwan ',
                   ' Korea, Republic Of ', ' India ', ' Pakistan ',
                   ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]
print(Asia1)
# splitting year and month for periods
Asia2 = Asia1["Periods"].str.split(expand=True)
print(Asia2)

Asia1 = Asia1.assign(Year=Asia2[0])
Asia1 = Asia1.assign(Month=Asia2[1])
print(Asia1)

# converting to numeric
Asia1['Year'] = pd.to_numeric(Asia1['Year'])
print(Asia1.dtypes)

# filter year
Asia3 = Asia1[(Asia1['Year'] >= 1988) & (Asia1['Year'] <= 1997)]
print(Asia3)

Asia4 = Asia3[[' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ',
               ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
               ' Hong Kong ', ' China ', ' Taiwan ',
               ' Korea, Republic Of ', ' India ', ' Pakistan ',
               ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]

ps = Asia4.sum().sort_values(ascending=False)
top3 = ps.head(3)
top3.index
print(ps)
print(top3)

import numpy as np

index = np.arange(len(top3.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3.index, fontsize=6, rotation=30)
plt.title("Top 3 Asian Countries from 1988-1997 (Period: 1988-1997)")
plt.bar(top3.index, top3.values / 1000)
plt.show();

index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=7, rotation=60)
plt.title('Total Asian Countries from 1988-1997 (Period: 1988-1997)')
plt.bar(ps.index, ps.values / 1000)
plt.show();