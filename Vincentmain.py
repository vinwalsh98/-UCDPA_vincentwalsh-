# Vincent Walsh. vincentwalsh98@outlook.com

import csv

import austin as austin
import numpy as np
import pandas as pd
import sns as sns

# Importing a csv file into a Pandas Dataframe


led=pd.read_csv("led 2.csv", encoding='latin-1')
print(led)

# Retrieving data from online APIs

import requests
request=requests.get('https://www.kaggle.com/augustus0498/life-expectancy-who')
print(request.status_code)
print(request.text)

## code inserted to expand number of columns shown
desired_width = 50000
width = pd.set_option('display.width', desired_width)
size = pd.set_option('display.max_columns', 20)

df = pd.DataFrame(led)
lifeex = ['Lifeexpectancy']
lifeex_index = (df.sort_values(by=(lifeex)).set_index('Year')['Country']) #indexing
lifeex_sort = (df.sort_values(by=['Lifeexpectancy'])) #sorting by number ascending
print(lifeex_sort)
print(lifeex_index)


# dropping duplicate dates

drop_led = led.drop_duplicates(subset=['Year'])
print(drop_led)



lifeex_iloc= lifeex_sort.iloc[[1, 6], 0 : 5] #iloc used to break down 2 rows and 6 columns
print(lifeex_iloc)



## to show data on missing rows

print(led.isnull().sum())



## information on missing values changed
clean_data = led.fillna("information currently unavailable")
print(clean_data)

## missing data is then removed
print(clean_data.isnull().sum())

## for loop

head = (clean_data.head(4))
for columnName in head: #for loop to gather column names
    print(columnName)

for k,v in head.iterrows(): # iterrows
    print(k)
    print(v)

data2010=pd.read_csv('Data_2010.csv', encoding='latin-1')
data2015=pd.read_csv('Data_2015.csv', encoding='latin-1')


#importing second dataframe for merging
merge_data = pd.merge_ordered(data2010, data2015, on='Age', suffixes=('_data2010','_data2015'), fill_method='ffill')
print(merge_data)





# Used dictionary to create an unordered sequence of values as an array

reader = csv.DictReader(open('Data_2015.csv'))
dict_row = next(reader)
print(dict_row)

# calculating mean age of parent locations
mean_region=(data2010.groupby("ParentLocation")["Age"].mean())
print(mean_region)

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

eu=pd.read_csv("life_expect_eu.pdnew.csv", encoding='latin-1')
print(eu)

# Chart 1
#plt.rcParams["figure.figsize"] = [16,9]
#fig, ax = plt.subplots()
#plt.plot(eu['Country'], eu['Total'], color='g', label='Waterford')
#plt.plot(eu['Country'], eu['Males'], color='r', label='Galway')
#plt.plot(eu['Country'], eu['Females'], color='hotpink', label='Limerick')
#plt.xticks(fontsize=7, rotation=90)
#plt.xlabel("Quarterly Year")
#plt.ylabel("Country")
#plt.title("Selected Regional Second Hand Housing Prices per Quarter 1997-2016 (EUR)")
#ax.xaxis.set_major_locator(plt.MaxNLocator(42))
#plt.legend()
#plt.show()


df = pd.read_csv("life_expect_eu.pdnew.csv")
def cm_to_inch(value):
    return value/2.54
country = df['Country'].values
x = np.arange(len(country)) #use of numpy
w = 0.2
y_pos = range(len(country))
plt.figure(figsize=(cm_to_inch(50), cm_to_inch(25)))
plt.bar(x-w, df['Total'].values, width=w, label='Total')
plt.bar(x, df['Males'].values, width=w, label='Males')
plt.bar(x+w, df['Females'].values, width=w, label='Females')
plt.gca().yaxis.set_major_locator(tck.MultipleLocator(5))
#plt.xticks(x, country)
plt.title("Selected EU Country's Life Expectancy 2018")
plt.xlabel("Country")
plt.ylabel("Age")
plt.xticks(y_pos, country, rotation=90, fontsize=6)
plt.subplots_adjust(left=0.05, bottom=0.19, top=0.82)
plt.ylim([0,100])
plt.legend(loc='best')
plt.show()



import matplotlib.pyplot as plt

led=pd.read_csv("led 2.csv", encoding='latin-1')
print(led)

led_dev= led.loc[led['Status'] == 'Developed'] #filter only for developed nations
import sys
sys.stdout.flush()
print(led_dev)

led_dev2015= led_dev.loc[(led_dev['Year'] >= 2015)] #filter only for developed nations for year 2015
sys.stdout.flush()
print(led_dev2015)


import seaborn as sns


sns.set(style="darkgrid")
plt.figure(figsize=(cm_to_inch(50), cm_to_inch(25)))
plt.subplots_adjust(left=0.09, bottom=0.11, top=0.82)
rel = sns.scatterplot(x="Lifeexpectancy", y="GDP", data=led_dev2015, hue="Country");
plt.setp(rel.get_legend().get_texts(), fontsize='7')
plt.setp(rel.get_legend().get_title(), fontsize='10')
plt.title("GDP v Life Expectancy for Developed Nations 2015")
plt.xlabel("Life Expectancy")
plt.ylabel("GDP Per Capita ($)")
rel.legend(loc='best', ncol=1, borderpad=0.02, prop={'size':7})
plt.show()



