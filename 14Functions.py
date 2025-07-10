# def greeting(user_name , age=none):
#     print('*' * 20)
#     print(f'welcome {user_name}')
#     print(f'Age is {age}')
#     print('thank you for signing in ...')
# greeting('sham' , 30)
# greeting('baburam')


# def greeting(user_name , *hobbies):
#     print('*' * 20)
#     print(f'welcome {user_name}')
#     print('hobbies are:')
#     for hobby in hobbies:
#         print(f'-{hobby}')
#     print('thankyou for signing in...')
#     print('*' * 20)
#
# greeting('raju','singing','dancing','shooting')
# greeting('sham','playing','swimming')
# greeting('baburao','tv','football')

#dynamic argument function (**)
def user_detail(name , **user_info):
    print(f"Name - {name}")
    for key , value in user_info.items():
        print(f"- {key}: {value}")

user_detail('raju' , age =18)
user_detail('sham' , age=18, city='delhi')
