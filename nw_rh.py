menu_option = ["1. buy data", "2. top up", "3. exit"]
buy_data = ["1. N100 for 100mb", "2. N200 for 200mb", "0.back"]
top_up = ["1. self", "2. third party", "0.back"]


def get_code():
    return input("Enter a code: ")


def mtn():
    print("Welcome to MTN!")
    print("Please, select a package")


def globacom():
    print("Welcome to GLOBACOM!")
    print("Please, select a package")


def airtel():
    print("Welcome to AIRTEL!")
    print("Please, select a package")


def main():
    code = get_code()

    if code == "*131#":
        mtn()
    elif code == "#124#":
        globacom()
    elif code == "#121#":
        airtel()
    else:
        print("Wrong USSD code!\nTry again")
        get_code()




if __name__ == "__main__":
    main()      
