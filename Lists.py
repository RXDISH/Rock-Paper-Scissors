grocery_list = ['🥚 Eggs', '🥑 Avocados', '🍪 Cookies', '🌶 Hot Pepper Jam', '🫐 Blueberries', '🥦 Broccoli']
print(grocery_list)



lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]
print(len(lego_parts)) # gives the total length of a list
print(max(lego_parts)) # gives the highest number in the list
print(min(lego_parts)) # gives the lowest number in the list



books = ['Zero to One', 'The Lean Startup', 'The Mom Test' ,'Make It Stick', 'Life in Code']
books.insert(2, 'Zero to Sold')
books.pop(1)
books.remove('Zero to One')
print(books)