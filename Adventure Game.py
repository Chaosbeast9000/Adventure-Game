#Adventure Game ChadDumke

menu = {}
menu['1']="Dungeons" 
menu['2']="Inventory"
menu['3']="Character Stats"
menu['4']="Exit"

if selection == '1': 
   print ("Dungeons") 
  elif selection == '2':
        print ("Inventory")
  elif selection == '3':
      print ("Character Stats") 
  elif selection == '4': 
      break
  else: 
      print "Unknown Option Selected!" 


print("you are lost underground in a maze of tunnels.")
import random
dangerTunnel = random.randint(1,3)
diceRoll= random.randint(1,2)
gold_pieces= int()

#inventory code 
inv = ['Sword','Armor','gold_pieces']
item_values = {'Sword':['Sword',5,1,15,2],
               'Armor':['Armor',0,10,25,5]}

print('Name\tAtk\tArm\tLb\tVal')
print(item_values[inv[0]][0],'\t',item_values[inv[0]][1],'\t',item_values[inv[0]][2],'\t',item_values[inv[0]][3],'\t',item_values[inv[0]][4])
print(item_values[inv[1]][0],'\t',item_values[inv[1]][1],'\t',item_values[inv[1]][2],'\t',item_values[inv[1]][3],'\t',item_values[inv[1]][4])



 # Menu system!
def menu():
    print ("Menu")
    return int(raw_input())

    

# print ("Dragon in tunnel ", dangerTunnel)
tunnelChoice = 0
while tunnelChoice < 1 or tunnelChoice > 3:
  tunnelChoice = int(input("Choose tunnel 1, tunnel 2, or tunnel 3: "))
  print ("You chose tunnel ", tunnelChoice)
if tunnelChoice == dangerTunnel:
    print ("You enter a tunnel with a dragon. Watch out.")
else:
    print ("You enter an empty tunnel. You are safe for now.")
if tunnelChoice !=dangerTunnel and diceRoll == 2:
  gold_pieces =+ 50
  print (" And You find treasure worth 50 gold pieces")

  