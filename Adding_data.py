import pandas as pd
from datetime import datetime

x = pd.read_csv("./Tr_data.csv", sep=",")

date       = x["Tarih"].values.tolist()
case       = x["Toplam Vaka Sayısı"].values.tolist()
new_cases  = x["Yeni Vaka Sayısı"].values.tolist()
deaths     = x["Ölüm Sayısı"].values.tolist()
made_tests = x["Yapılan Test Sayısı"].values.tolist()

i = 1
while i<=len(date):
    variable = date[i-1]
    date[i-1] = datetime.strptime(variable, '%Y-%m-%d').date()
    i=i+1
    
i = 1
while i<=len(case):
    case[i-1] = int(case[i-1])
    i=i+1
    
i = 1
while i<=len(new_cases):
    new_cases[i-1] = int(new_cases[i-1])
    i=i+1
    
i= 1
while i<=len(deaths):
    deaths[i-1] = int(deaths[i-1])
    i=i+1

i= 1
while i<=len(made_tests):
    made_tests[i-1] = int(made_tests[i-1])
    i=i+1
    
i_date       = input("Tarih: ")
i_case       = int(input("Vaka sayısı: "))
i_new_case   = i_case - case[-1]
i_made_tests = int(input("Yapılan test sayısı: "))
i_deaths     = int(input("Ölüm sayısı: "))

date.append(datetime.strptime(i_date, '%d.%m.%Y').date())
case.append(i_case)
new_cases.append(i_new_case)
made_tests.append(i_made_tests)
deaths.append(i_deaths)


df = pd.DataFrame({"Tarih": date,
                   "Toplam Vaka Sayısı": case,
                   "Yeni Vaka Sayısı": new_cases,
                   "Ölüm Sayısı": deaths,
                   "Yapılan Test Sayısı": made_tests
                  })

df.to_csv("Tr_data.csv", index=False)