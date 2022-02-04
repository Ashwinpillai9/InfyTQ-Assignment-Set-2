"""
You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. 
You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.
"""
#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    if(rupees_to_make%5!=0 and rupees_to_make>5):
        while(rupees_to_make%5!=0):
            rupees_to_make-=1
            one_needed+=1
    elif(rupees_to_make<5):
        one_needed=rupees_to_make
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
        return
    if(rupees_to_make%5==0):
        five_needed = rupees_to_make//5
    else:
        print(-1)
        return
    
    if(five_needed>no_of_five):
        extra= five_needed - no_of_five
        five_needed-=extra
        one_needed+= extra*5
        if(one_needed>no_of_one):
            print(-1)
            return
        
    if(one_needed>no_of_one):
            print(-1)
            return

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    print("No. of Five needed :", five_needed)
    print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(103,20,2)
