ItemsInCart = 0
# add 2 items in cart

#first method - raising exception
# if ItemsInCart != 2 :
#     raise Exception("Products cart count not matching")

# Second method - using assert statement
# assert (ItemsInCart == 0)


#Third method - code might fail but test execution needs to continue
# put code block in try block and catch the exception or explaination in except block
#
# try:
#     with open('filelog.txt', 'r') as reader:
#         reader.read()
#
# except:
#     print("failure in try block is captured here")

# this is useful in case of dynamic elements handling


try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)        # print actual python error received
    # No such file or directory: 'filelog.txt'
finally:
    print("Try and except block is executed")
    # This will always execute irrespective of passage/failure in try block
    # purpose - clean up any records, cookies created



ItemsInCart = 0


def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


# Example of using the function
try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)