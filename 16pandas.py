import pandas

data =pandas.read_csv('emp_data.csv')
print(data)

print(data.salary.min())

print(data[data.emp_id == 105])
print(data[data.salary== data.salary.max()])

empid_103=data[data.emp_id ==103]
print(empid_103.fname.values[0] , empid_103.name.values[0])

print(data.salary.to_list())
print(data.to_dict())

data.loc[data.emp_id == 102 , 'salary'] =80000
print(data)

data= data.sort_values(by='salary')
print(data)