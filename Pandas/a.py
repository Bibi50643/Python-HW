import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
data = pd.read_csv('diabetes.csv')

data1=data.where(data.Outcome == 1)
data2=data.where(data.Outcome == 0)
a='Mean value of insulin sick patients',"Mean value of insulin healthy patients"
b=data1['Insulin'].mean(),data2['Insulin'].mean()
plt.subplot(221)
plt.bar(a,b,color='Blue')

plt.subplot(222)
d=data1['Glucose'].max(),data2['Glucose'].max()
c='Max value of glucose sick patients',"Max value of glucose healthy patients"
plt.bar(c,d,color='Green')

plt.subplot(223)
f=data1['Pregnancies'].max(),data2['Pregnancies'].max()
e='Max amount of pregnancy sick patients',"Max amount of pregnancy healthy patients"
plt.bar(e,f,color='Red')

plt.subplot(224)
g=data1['BMI'].mean(),data2['BMI'].mean()
h='Mean value of BloodPressure sick patients',"Mean value of BloodPressure  healthy patients"
plt.bar(h,g,color='Yellow')

plt.show()

print(data.loc[data.Outcome == 1]["Outcome"].sum()) #число больных
print(data.loc[data.Outcome == 0]["Outcome"].count()) #число  не больных
print(data['Outcome'].value_counts())
print("Average glucose value: ", data["Glucose"].mean())
max_preg_w = data[data['Pregnancies']==data['Pregnancies'].max()]
print("Woman with the highest number of pregnancies:")
print(max_preg_w)
print("Real data shape:",data.shape)

data[['Glucose','BloodPressure','Insulin','BMI']]=data[['Glucose','BloodPressure','Insulin','BMI']].replace(0,np.nan)

max_preg = data['Pregnancies'].max()
print("Highest number of pregnancies:")
print(max_preg)
data=data[data.Outcome==1] # выбирает только больных
new=data[data['Age'].where ((data['Insulin']>90)).notna()] 
new=new.dropna(axis = 0, how ='any') #удаляет строки с NaN
new.to_csv('neww.csv')
new=pd.read_csv('neww.csv')
print("New data shape:",new.shape)#shape changed
mask =new['Age'] > 50
print("Number of sick women over 50: ",new[mask])
print("The age of sick patients in which most people have insulin is more than 90:")
print(new.Age.mode())






