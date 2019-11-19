#required fold equity
risk = float(input("What is the risk(amount you open for)? ")) 
potential_gain = float(input("What are the blinds and total antes?  ")) 


def req_fold_equity(r, pg):
    return (r/(r + pg) ) 

blind_steal = req_fold_equity(risk, potential_gain) 

print("Villian must fold to steal " + str(blind_steal *100) + "% of the time. ")

#This calculates the required fold equity to see if your steals are profitable
#look at the small and big blinds. If they fold less than this number than you can profitably steal
