import Pankaj_a1

old=input("enter the old currency:-").upper().strip()
new=input("enter the new currency:-").upper().strip()
amt=input("enter the amount:-")
# DO NOT modify the following code
# if the source currency is not valid, quit
if(not(Pankaj_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
# if the target currency is not valid, quit
if(not(Pankaj_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()

new_amt=Pankaj_a1.exchange(old,new,amt)
print('You can exchange {0} {1} for {2} {3}'.format(amt,old,new_amt,new))