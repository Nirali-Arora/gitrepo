import pandas
db=pandas.read_csv('SalaryData.csv')
x=db['YearsExperience'].values.reshape(30,1)
y=db['Salary']
from sklearn.linear_model import LinearRegression
mind= LinearRegression()
mind.fit(x,y)
exp=input("To predict salary enter years of experience :" )
out=mind.predict([[exp]])
print("predicted salary = {}".format(out))



