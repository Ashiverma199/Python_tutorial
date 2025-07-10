# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("kindly do not divide by zero")
#
# try:
#     with open ("hola.txt") as f:
#         content=f.read()
# except FileNotFoundError:
#     print("file is not found")

try:
    with open('user_in.txt' , 'r') as file:
        content = file.readlines()
except Exception as e:
    print(e)
else:
    for line in content :
        print(f'welcome{line.rstrip()}')