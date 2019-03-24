#Dictionaries
my_stuff = {"key1":"calue", 'key2':'value2'}
print(my_stuff['key2'])

#Nested Dictionaries
print('Nested Dictionaries')
my_stuff = {"key1":"calue", 'key2':'value2','key3':{'1':[1,2,'grade'],'k3':['a','b','cook']}}
print(my_stuff['key3'])
print(my_stuff['key3']['k3'][2].upper())

print("Another Example")
my_stuff = {'lunch':'pizza', 'bfast':'eggs'}
#now if we want to change lunch value to Burger then
my_stuff['lunch'] ='burger'
print('After changing Lunch')
print(my_stuff['lunch'])
