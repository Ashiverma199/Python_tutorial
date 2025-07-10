import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('emp_data.csv')
# plt.bar(data.emp_id, data.salary)
plt.scatter(data.emp_id ,data.salary)

plt.xlabel('emp_id')
plt.ylabel('salary')
plt.title('Employee Id vs Salary')
plt.show()