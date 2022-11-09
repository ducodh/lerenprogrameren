# name of student: duco den hartog
# number of student: 99072498
# purpose of program: wisselgeld uitrekenen
# function of program: wisselgeld uitrekenen
# structure of program: -

toPay = int(float(input('Amount to pay: '))* 100) # input for the amount that has to be paid
paid = int(float(input('Paid amount: ')) * 100) # input for the amount that has been paid
change = paid - toPay # calculating the change

if change > 0: # kijken of er wisselgeld nodig is
  coinValue = 500 # start value van de coins
  
  while change > 0 and coinValue > 0: # loop 
    nrCoins = change // coinValue # delen

    if nrCoins > 0: # hoeveel van de bepaalde munt terug moet
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: aflopende geldberdagen in cent
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50    
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als er nog over blijft
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')