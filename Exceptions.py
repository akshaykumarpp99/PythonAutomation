
itemsInCart = 0

if itemsInCart != 2:
    # raise Exception("Product card count not matching")
    pass

# assert(itemsInCart == 2)
assert(itemsInCart == 0)

# try:
#     with open('readme.md','r') as reader:
#         reader.read()
# except:
#     print("No such file found")

try:
    with open('text.py', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning process")