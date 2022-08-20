def q7_assess_bolt(strength, diameter_error, amart_near):
    passed = False
    if strength >= 400 and diameter_error <= 75:
        passed = True
    if not passed and strength < 400 and diameter_error < 125 and amart_near is True:
        print("Sell to Amart")
    else:
        print("Reject")       

q7_assess_bolt(300, 60, True)