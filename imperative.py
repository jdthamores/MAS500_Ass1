# Print out all the total votes count from obama and romney
# Coded in the "imperative" style

f = open('2012_US_election_state.csv', 'r')
print "Opened file:"

obama_vote = 0
romney_vote = 0
all_lines = f.readlines()
for line in all_lines:
    columns = line.split(",")
    if columns[3].isdigit():
    	if columns[3]:
    		obama_vote = obama_vote + int(columns[3])
    	if columns[5]:
    		romney_vote = romney_vote + int(columns[5])

print "done ("+str(len(all_lines))+" lines)"
print "total votes count obama: "+ str(obama_vote)
print "total votes count romney: "+ str(romney_vote)
