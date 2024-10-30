#Write a Python program to check if a person qualifies for a special offer based on the following criteria:

#Use and to check if the person has an annual income of at least $50,000 and is currently employed.
#Use not to ensure that the person does not have any unpaid debts.
#Use or to add an alternative condition that will pass if the person has a loyalty card, even if they don’t meet the income and employment criteria.
#If any of these conditions are met, print "Offer Granted!", otherwise print "No Offer".

annual_income = 55000
employed = True
unpaid_debts = False
has_loyality_cards = True

if ((annual_income >= 50000 and employed)
and not unpaid_debts or has_loyality_cards):
    print("offer Granted")
else:
    print("No offer")
    