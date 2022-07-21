"""NumPy (Numerical Python), çok boyutlu dizilerle ve matrislerle çalışmamızı sağlayan
 ve matematiksel işlemler yapabileceğimiz Python dili kütüphanelerindendir"""

import numpy as np

# NumPy Array Oluşturmak (Creating Numpy Arrays)

a = np.array([5, 4, 3, 2, 1])
b = np.array([2,4,5,3])
c = np.array([(1.5,2,3), (4,5,6)], dtype = float)
d = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]], dtype = float)

type(a) # numpy.ndarray

np.zeros(10 ,dtype=float) #sıfırlardan oluşan, 10 elemanlı, float tipli array
e = (np.ones((2,3,4),dtype=np.int16)) # 2 matris 3 satır 4 sütun
f = np.arange(10,55,5) # 10 dan 55 e kadar 5 er artan
g = np.linspace(0,2,9) #0 dan başla 2 ye kadar 9 eş parçaya böl
h = np.full((2,2),7)  # 2 ye 2 lik 7 lerden oluşan matris
k = np.eye(8) # 8 e 8 lik birim matrisi

np.random.random((2, 2)) # belirtilen ölçülerde 0-1 arası değerler alan matris
r = np.empty((2,3)) # boş
np.random.randint(0,100,size=10) #0-100 arasında değerlerden oluşan 10 elemanlı int tipli array
np.random.normal(5,1,(4,5)) #parametreleri verilen normal dağılım oluşturma

"""
 VERİ Tipleri 
>>> np.int64 Signed 64-bit integer types
>>> np.float32 Standard double-precision floating point
>>> np.complex Complex numbers represented by 128 floats
>>> np.bool Boolean type storing TRUE and FALSE values
>>> np.object Python object type
>>> np.string_ Fixed-length string type
>>> np.unicode_ Fixed-length unicode type
"""

"""
>>> a.shape Array dimensions
>>> len(a) Length of array
>>> b.ndim Number of array dimensions
>>> e.size Number of array elements
>>> b.dtype Data type of array elements
>>> b.dtype.name Name of data type
>>> b.astype(int) Convert an array to a different type
"""
a = np.array([(3.7,25,3), (2,9,11)])
b = np.array([(1.5,2,3), (4,5,6)])
g = a - b    #farkını alma
np.subtract(a,b)  #farkını alma

h = b + a # toplama
np.add(b,a) #toplama

a / b
np.divide(a,b)

a * b
np.multiply(a,b)

np.exp(b) #Exponentiation
np.sqrt(b) #Square root
np.sin(a) #Print sines of an array
np.cos(b) #Element-wise cosine
np.log(a) #Element-wise na

a == b #bool
a < 2 #bool

a.sum() #Array-wise sum
a.min() #Array-wise minimum value
b.max(axis=0) #Maximum value of an array row
b.cumsum(axis=1) #Cumulative sum of the elements
a.mean() #Mean
np.std(b) #Standard deviation

a.sort() #Sort an array
c.sort(axis=0) # Sort the elements of an array's axis

h = a.view() #Create a view of the array with the same data
np.copy(a) #Create a copy of the array
h = a.copy() #Create a deep copy of the array



# Yeniden Şekillendirme (Reshaping)

np.random.randint(1,10,size=12).reshape(3,4) #birinci argüman satır, ikinci sütun


# Index Seçimi (Index Selection)

a = np.random.randint(10,size = 10)
a[9]
a[2]
a[2] =12

b = np.random.randint(100,size = 12).reshape(4,3)
b
b[3,2] #birincisi sütüun ikincisi satır

b[:,2] #ikinci sütun tüm satırlar

b[1,:] #birinci  satır tüm sütunlar

b[1:4,1:3] # birinci satırdan dördüncü satıra kadar, birinci sütundan 3 üncü sütuna kadar


# Fancy Index

c = np.arange(0,100,5) # sıfırdan 100 e kadar 5 er artan eleman

catch= [ 1,3,5,6]
b = c[catch]

#seçim işlemleri

d = np.array((1,2,3,4,5,6,7,8))

#döngü ile
d2 = []
for i in d:
    if i < 4:
        d2.append(i)
#numpy ile

d3 = d[d < 6]
d3 = d[d > 2]
d3 = d[d != 3] # 3 olmayanları seç
d3 = d[d >= 3]


# Matematiksel İşlemler (Mathematical Operations)

e = np.array([1,2,3,4,5,])

e / 4
e * 5 / 10
e ** 2
e - 1

np.subtract(e,5) # her elemandan çıkar
np.add(e, 1) # her elemana ekle
np.mean(e) #ortalama
np.sum(e) #toplam
np.min(e) #en küçük
np.max(e) #en büyük
np.var(e) # varyans
