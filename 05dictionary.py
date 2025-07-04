#dats in form of key value pair
marks={'Hindi':80 ,
       'English':90  }
print(marks)
print(type(marks))
print(marks.get('English'))

marks['Maths']=100
print(marks.get('Maths'))

#to delete
del marks['Hindi']

#length of dictionary
print(len(marks))
