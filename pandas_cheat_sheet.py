# PANDAS

"""pandas, veri işlemesi ve analizi için Python programlama dilinde yazılmış olan
bir yazılım kütüphanesidir. Bu kütüphane temel olarak zaman etiketli serileri ve
sayısal tabloları işlemek için bir veri yapısı oluşturur ve bu şekilde çeşitli
işlemler bu veri yapısı üzerinde gerçekleştirilebilir olur."""

import pandas as pd
a = pd.Series([3,4,8,9,2]) #seriler tek boyutludur.

type(a)
a.index #satır sütün bilgisi
a.dtype #içindeki verinin tipi
a.size #eleman sayısı
a.ndim #boyutu
a.values #değerleri numpy arrayi olarak döndürür
a.head()
a.tail(2)

# Veri Okuma
#df = pd.read_csv("dosya_dizini")
#df.head()

# Veriye Hızlı Bakış

import pandas as pd
import seaborn as sns #örnek veri yüklemek için kuruldu

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape #boyut bilgisi
df.info() #değişkenler ve değişken tipleri bilgisi
df.columns #sütunları liste olarak döndürür
df.index #satır sütün bilgileri

df.describe().T #değişken sayısı ortalaması std min max ve çeyrekleri verir ****

df.isnull().values.any() #hiç boş var mı
df.isnull().sum() #boşların toplamı

df["sex"].head()
df["sex"].value_counts() #erkek kadın kaçar tane var


#Seçim İşlemleri

df.index
df[0:14]
df.drop(0,axis=0).head() #drop=silme axis 0 satırlar 1 sütunlar
delete_indexes = [1,3,4]
df.drop(delete_indexes,axis=0).head(10)  #iplace= true kalıcı kale getirir


# Değişkeni Indexe Çevirmek

df["age"].head()
df.age.head()

df.index = df["age"] #index bilgisi yerine yaşı atar
df.drop("age",axis=1).head()
df.drop("age", axis=1, inplace=True)


# Indexi Değişkene Çevirmek
df.index
df.head()
df["age"] = df.index
df.head()

df.drop("age",axis=1,inplace=True)
df.head()

df = df.reset_index()
df.head()

# Değişkenler Üzerinde İşlemler

"age" in df #bu değişken bunun içinde var mı sorgusu ?

df["age"].head()
type(df["age"]) #bu bir pandas serisi döner             ***
type(df[["age"]]) # bu ise bir pandas df idir           ***

df[["age","alive"]] #çoklu değişken seçimi

col_names= ["age","adult_male","alive"]
df[col_names] #çoklu değişken seçimi

df["age2"] = df["age"] ** 2 # df de olmayan bir değişken eklenmek istenirse
df["age3"] = df["age"] / df["age2"]
df.head()

df.drop("age3",axis=1, inplace=True)
df.head()

df.drop(col_names,axis=1).head()

df.loc[:,~df.columns.str.contains("far")].head() #içinde "far" olan değişkenler dışındaki değişkenler ****

df.head()

# iloc & loc

df = sns.load_dataset("titanic")
#iloc = integer based selection
df.iloc[0:3]
df.iloc[0:1]

#loc label based selection #isimlendirmenin kendisini seçer ****
df.loc[0:3]     #3 dahil olur

df.iloc[0:3,0:3]
df.loc[0:3,"age"]

col_names = ["age", "embarked", "alive"]

df.loc[0:3,col_names]

# Koşullu Seçim (Conditional Selection)

df[df["age"] > 50].head()
df[df["age"]>50]["age"].count() #koşulu sağlayan kaç kişi var

df.loc[df["age"] > 50,["age","class"]].head()
df.loc[(df["age"]>50) & (df["sex"]=="male"), ["age","class"]].head()

df["embark_town"].value_counts()


df_new = df.loc[(df["age"]>50) & (df["sex"]=="male")
                & ((df["embark_town"]=="Cherbourg" ) | (df["embark_town"] == "Southampton")),
                     ["age","class","embark_town"]]

#df_new öncelikle 2 farklı değişkenden 2 farklı koşulun aynı anda olmasını istedik,(age ve sex),
#bunların yanında embark_town değişkenine 2 farklı senaryonu veya ile bağladık,
#sonuç itibariyle 3 farklı koşulu seçip, koşulu seçtiğimiz değişkenlerin bilgilerini yeni df e atadık.
#koşul seççimlerini yaparken mantıksal op kullandık ve parantezlerle birbirinden ayırdık . *****

df_new["embark_town"].value_counts()

# Toplulaştırma ve Gruplama (Aggregation & Grouping)

# - count() #saydır
# - first() #ilk
# - last()  #son
# - mean() #ortalama
# - median() #medyan
# - min()
# - max()
# - std()
# - var() #varyans
# - sum() #toplama
# - pivot table
pd.set_option("display.max_columns", None)

df =sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean() #cinsiyete göre yaşın ortalaması hangi cinsiyetin yaşının ortalaması ne kadar
#groupby da neye göre sorusunun cevabı ilk parantez içinde olmalı ****



df.groupby("sex").agg({"age":"mean"})
#cinsiyete göre grupla,sözlük içindeki key değerinin sözlük içindeki value değerindeki hesapları getir


df.groupby("sex").agg({"age": ["mean" , "sum"],
                       "survived" : "mean"})
#cinsiyete göre grupla, yaşa göre listedeki hesapları yap, hayatta kalma yüzdelerini de gözlemle

df.groupby(["embark_town","sex","class"]).agg({"age":["mean","sum","max"],
                                               "survived":["mean","sum","min"],
                                               "sex":"count"})
#sırasıyla 3 değişkene göre grupla, her spesifik grubun liste içinde verilen hesaplarını yap   *******
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})


# Pivot table

df.groupby("sex").agg({"age" : "mean","embark_town":"count"})

#birinci argüman ortalama (varsayılan olarak ortalamadır. ,
#değiştirilmek istenirse "aggfunc" isimli parametre girişi yapılır
#ikinci argüman satırlar
#üçüncü argüman sütunlar

df.pivot_table("age", "embarked", "sex")

df["new_age_group"] = pd.cut(df["age"], [0,10,18,28,35,50,90])
#cut ve qcut fonksiyonları sayısal değişkenleri kategorik değişkenlere
#çevirmek için kullanılan fonksiyonlardır.
#cut fonksiyonunda bölmek istediğimiz değerleri biz gireriz.
#qcut fonksiyonunda ise çeyreklik değerlerine göre kendisi otomatik bölerr  * ** * **




df.pivot_table("survived",["sex","class"],"new_age_group")

# Apply ve Lambda

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500) # çıktının yanya görünmesi için yapılan ayar
df = sns.load_dataset("titanic")


df["age2"] = df["age"]*2
df["age3"] = df["age"]*5
df.head()

(df["age"]/10).head()
(df["age2"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/100

df.head()

df[["age","age2","age3"]].apply(lambda x: x/10).head(20)

df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/10).head(19)
df.loc[:,df.columns.str.contains("age")].apply(lambda x:(x -x.mean()) / x.std()).head(10)

def standart_scaler(col_name):
    return(col_name-col_name.mean()) / col_name.std()

df.loc[:,df.columns.str.contains("age")]  = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler)

df.head()

# Birleştirme (Join) İşlemleri


import pandas as pd
import numpy as np

m = np.random.randint(1, 30, size=(5,3)) #1-30 arası 5 satır 3 sütun
df1 = pd.DataFrame(m,columns=["var1","var2","var3"])
df2 = df1 + 234

pd.concat([df1,df2])

pd.concat([df1,df2],ignore_index=True)


# Merge ile Birleştirme İşlemleri
df3 = pd.DataFrame({"employees": ["john", "ahmet", "mehmet", "ümit"],
                    "group": ["mühendis", "İk", "çaycı","başkan"]})

df4 = pd.DataFrame({"employees": ["john", "ahmet", "mehmet", "ümit"],
                                  "start_date": [2012,2013,2020,2022]})

pd.merge(df3,df4)
pd.merge(df3,df4, on="employees")

#her çalışanın müdürünün bilgisine erişmek istiyoruz.
df5 = pd.merge(df3,df4)
df6 = pd.DataFrame({"group": ["mühendis", "çaycı", "İk"],
                    "manager": ["Eyüp","mehmet","ayşe"]})
df6

pd.merge(df5 , df6)
