#global variables are defined here:

menu_option = ["1. buy data", "2. top up", "3. exit"]
buy_data = ["1. N100 for 100mb", "2. N200 for 200mb", "0.back"]
top_up = ["1. self", "2. third party", "0.back"]

def ussd_app(code):
    if code == "*131#":
            print("Welcome to MTN!")
            print("Please, select a package")
            for item in menu_option:               
                print(item)
            menu = int(input("Select package: "))
            if menu == 1:
                for item in buy_data:
                    print(item)
                buy_data_plan = int(input("Choose a plan: "))
                if buy_data_plan == 1:
                    return f"You have selected\n\n{buy_data[0]}"
                elif buy_data_plan == 2:
                    return f"You have selected\n\n{buy_data[1]}"
                elif buy_data_plan == 0:
                    return main()
                else:
                    return f"Wrong input!"
            elif menu == 2:
                print("Select a top up plan!")
                for item in top_up:
                    print(item)
                top_up_plan = int(input("Select a top up plan: "))
                if top_up_plan == 1:
                    self_num = input("Enter your number: ")
                    return f"Successfully credited airtime on {self_num}"
                elif top_up_plan == 2:
                    third_party_num = input("Enter third party number: ")
                    return f"Successfully credited airtime on {third_party_num}"
                elif top_up_plan == 0:
                    return main()
                else:
                    return f"Wrong input!"
            elif menu == 3:
                return f"You have exit the USSD interface!"
    #Another telecom ussd code #codelines for Globacom telecommunication

    if code == "#124#":
        print("Welcome to GLOBACOM!")
        print("Please, select a package")
        for item in menu_option:
            print(item)
        menu = int(input("Select package: "))
        if menu == 1:
            for item in buy_data:
                print(item)
            buy_data_plan = int(input("Choose a plan: "))
            if buy_data_plan == 1:
                return f"You have selected\n\n{buy_data[0]}"
            elif buy_data_plan == 2:
                return f"You have selected\n\n{buy_data[1]}"
            else:
                return f"Wrong input!"
        elif menu == 2:
            print("Select a top up plan!")
            for item in top_up:
                print(item)
            top_up_plan = int(input("Select a top up plan: "))
            if top_up_plan == 1:
                self_num = input("Enter your number: ")
                return f"Successfully credited airtime on {self_num}"
            elif top_up_plan == 2:
                third_party_num = input("Enter third party number: ")
                return f"Successfully credited airtime on {third_party_num}"
            else:
                return f"Wrong input!"
        elif menu == 3:
            return f"You have exit the USSD interface!"
    #Final telecom ussd code #code lines for airtel communication

    if code == "#121#":
        print("Welcome to AIRTEL!")
        print("Please, select a package")
        for item in menu_option:
            print(item)
        menu = int(input("Select package: "))
        if menu == 1:
            for item in buy_data:
                print(item)
            buy_data_plan = int(input("Choose a plan: "))
            if buy_data_plan == 1:
                return f"You have selected\n\n{buy_data[0]}"
            elif buy_data_plan == 2:
                return f"You have selected\n\n{buy_data[1]}"
            else:
                return f"Wrong input!"
        elif menu == 2:
            print("Select a top up plan!")
            for item in top_up:
                print(item)
            top_up_plan = int(input("Select a top up plan: "))
            if top_up_plan == 1:
                self_num = input("Enter your number: ")
                return f"Successfully credited airtime on {self_num}"
            elif top_up_plan == 2:
                third_party_num = input("Enter third party number: ")
                return f"Successfully credited airtime on {third_party_num}"
            else:
                return f"Wrong input!"
       elif menu == 3:
           return f"You have exit the USSD interface!"
    else:
        return f"Wrong USSD code!"

print(ussd_app(input("Enter a code: ")))        