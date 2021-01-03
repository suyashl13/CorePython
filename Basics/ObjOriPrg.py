class Phone:
    phone_version = "S10"
    brand_name = "Samsung"
    user_name = ""

    # Function
    def BootLogo(self):
        print("Samsung")
        print(self.user_name)
        print(self.brand_name)

    # Constructor
    def __init__(self, user, brand_name):
        self.user_name = user
        self.brand_name = brand_name


suyash = Phone('suyash', "samsung")
suyash.BootLogo()
