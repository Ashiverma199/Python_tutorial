#store unordered and unique elements

my_sets={'mon','tues','wed'}
print(type(my_sets))

my_sets.add('thurs')
print(my_sets)

my_list=['mon','tue','wed','mon','tue']
days_set=set(my_list)
print(days_set)