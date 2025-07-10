
# with open ('user_info.txt','w') as file:
#     file.write('this is my text file using python')
#
with open ('user_info.txt' ,'r') as file:
     content=file.readlines()

print(content)