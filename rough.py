def q7_assess_bolt(strength, diameter_error, amart_near):
    '''
    Returns one of three string messages depending on whether a
    bolt is of acceptable quality or not.
    Parameters:
    strength - the bolt's tensile strength in MPa
    diameter_error - the bolt's diameter variation in micrometres
    amart_near - True iff there is an Amart Furniture near the factory

    A bolt must have a tensile strength of at least 400 MPa to pass A bolt that is strong enough must 
    also have a diameter variation of no more than 75 micrometres in order to pass

    If a bolt doesn’t pass, but has a diameter variation less than 125 micrometres, and 
    there is an Amart Furniture nearby, then the company will sell it to Amart Furniture instead of discarding it

    Any bolt that does not pass and is not sold to Amart Furniture is rejected 

    PASS, REJECT, AMART = 'Pass', 'Reject', 'Sell to Amart'

    q7_assess_bolt(300, 60, False) the output is 'Sell to Amart' and not Reject like it should be

    '''
    if strength >= 400 and diameter_error <= 75:
        return 'PASS'    
    elif strength < 400 and diameter_error < 125 and amart_near is True:
        return 'AMART'
    elif strength < 400 and diameter_error <125 and amart_near is False:
        return 'REJECT'


    """
    res = q7_assess_bolt(300, 60, False)
if res: # res == True 
    print("Pass")
elif res == 10:# not True or not False:
    print("Sell to Amart")    
else: # res == False
    print("Reject") 
    """

res = q7_assess_bolt(400, 60, False)
if res == 'PASS': # res == True 
    print("Pass")
elif res == 'AMART':# not True or not False:
    print("Sell to Amart")    
else: # res == False
    print("Reject")     