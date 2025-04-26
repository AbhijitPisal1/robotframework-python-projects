from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn

@library
class Shop:

    def __init__(self):
        self.SeleniumLib = BuiltIn().get_library_instance("SeleniumLibrary")
        self.collectionLib = BuiltIn().get_library_instance("collections")
        self.BuiltInLib = BuiltIn().get_library_instance("builtin")
    # method name will be converted to keyword name
    @keyword
    def hello_world(self):
        print("hello")

    @keyword
    def add_items_to_cart_and_checkout(self, productsList):
        i = 1
        productsTitles = self.SeleniumLib.get_webelements(" css:.card-title")
        for productsTitle in productsTitles:
            if productsTitle.text in productsList:
                self.SeleniumLib.click_button("xpath:(//div[@class='card-footer'])["+str(i)+"]//button")

            i= i +1
        self.SeleniumLib.click_element("//a[@class='nav-link btn btn-primary']")






