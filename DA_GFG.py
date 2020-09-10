import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
countries = pd.read_excel("IMVA.xlsx")
print(countries)

countries[countries['Periods'] == '1980']
print(countries)