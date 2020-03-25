#riley puts pot in the fridge, dean puts them in the produce basket
#def a func to put whatever in either list
shop = {
    'pantry' : ['bread', 'pasta', 'trail mix', 'rice'],
    'fridge' : ['milk', 'cheese', 'turkey slices'],
    'produce basket' : ['apples', 'bananas', 'potatoes'] 
}
print('Here\'s what\'s in the pantry...')
print(shop['pantry'])
print('Here\'s what\'s in the fridge...')
print(shop['fridge'])
print('Here\'s what\'s in the produce basket...')
print(shop['produce basket'])
def switch(list_one, thing, list_two):
    list_one.remove(thing)
    list_two.append(thing)
#how do i specify the potatoes in the produce basket shop list???
#i cant figure this outtttttttt wahhhhhhhh
shop['produce basket'].remove('potatoes')
print('Riley removes potatoes from the produce basket and puts them in the fridge!')
shop['fridge'].append('potatoes')
print(shop['fridge'])
print('Dean sees this and removes the potatoes from the fridge and adds them to the produce basket.')
shop['fridge'].remove('potatoes')
shop['produce basket'].append('potatoes')
print(shop['produce basket'])
print('All is well in the Relkin-Rey household.')
def swap(list_one, thing, list_two):
    list_one.remove('thing')
    list_two.append('thing')
#swap(shop['produce basket'], shop['produce basket'][2], 'shop[fridge]')
#i still want a function >:(((
def printing(list_one):
    print(list_one)
printing(shop['pantry'])
switch(shop['fridge'],'cheese',shop['pantry'])
printing(shop['pantry'])