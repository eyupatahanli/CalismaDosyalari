#Temel Pandas yapılarını keşfetmek tekrar için basit alıştırmalar

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

df = sns.load_dataset("titanic")

# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()

# Görev 4: pclass değişkeninin unique değerleri bulunuz.
df["pclass"].unique()
df.loc[:,"pclass"].unique()

# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[["pclass","parch"]].nunique()

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
df["embarked"].dtypes
df["embarked"] = df["embarked"].astype("category")
str(df["embarked"].dtypes)

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.

df[df["embarked"] == "C"].head()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[df["embarked"] != "S"].head()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df["sex"] == "Female") & (df["age"] < 30)].head()

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df[(df["fare"] > 500) | (df["age"] > 70)].head()

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12: who değişkenini dataframe'den düşürün.

df.drop("who",axis=1)

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

df["deck"].fillna(df["deck"].mode()[0],inplace=True)

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.

df["age"].fillna(df["age"].median(),inplace=True)

# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})


# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

def Age30 (age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : Age30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset("tips")
df.head(15)

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["time"]).agg({"total_bill":["min","max","mean","sum"]})

# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["day","time"]).agg({"total_bill":["min","max","mean","sum"]})

# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.


df[(df["sex"]=="Female") & (df["time"] == "Lunch")].groupby(["day"]).agg({"total_bill":["min","max","mean","sum"],
                                                                            "tip":["min","max","mean","sum"]})


# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?

df.loc[(df["size"] < 3) &(df["total_bill"] > 10),"total_bill"].mean()
df[(df["size"] < 3) &(df["total_bill"] > 10)]["total_bill"].mean()
df.head(15)

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]


# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulun.
# Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara bir verildiği yeni bir total_bill_flag değişkeni oluşturun.
# Dikkat !! Female olanlar için kadınlar için bulunan ortalama dikkate alıncak, male için ise erkekler için bulunan ortalama.
# parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayın. (If-else koşulları içerecek)


def a(sex,total_bill):
    female_avg = df[df["sex"] == "Female"]["total_bill"].mean()
    mela_avg = df[df["sex"] == "Male"]["total_bill"].mean()

    if sex == "Female":
        if total_bill < female_avg:
            return 0
        else:
            return 1
    if sex == "Male":
        if total_bill < mela_avg:
            return 0
        else:
            return 1

df["total_bill_flag"] =  df[["sex","total_bill"]].apply(lambda x: a(x["sex"],x["total_bill"]),axis=1)



# Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyin.
df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag":"count"})

# Görev 25: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

df2 = df.sort_values("total_bill_tip_sum",ascending=False)[:30]
df2.shape
df2.head(20)

