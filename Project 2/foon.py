import os


print "FOON: Merge"

################################################################
# INPUT FILE NAMES

fileNameOne = raw_input("Input FOON file name: ")
fileKitchen = raw_input("Input Kitchen file name: ")
fileGoals = raw_input("Input Goals file name: ")


# fileNameOne = "foon.txt"
# fileKitchen = "kitchen_5.txt"
# fileGoals = "goal_nodes/goals_new_19.txt"

################################################################
# DISTRIBUTE FOON RECIPES INTO LISTS

folder = []

for filename in os.listdir('Individual_FOON_Subgraphs'):
	folder.append('Individual_FOON_Subgraphs/'+filename)

FUfolder = []
FUsub = []
FUfolderAux = []
FUfolderAuxSub = []
FUfolderAuxAux = []
i = 0
while (i < len(folder)):
	#FUfolderAux = []
	FUfolderAuxAux = []
	with open(folder[i]) as fileFolder:
		FUfolderAux = []
		for line in fileFolder:
			if (ord(line[0]) != 47):
				FUfolderAuxAux = line.split("\t")
				if (FUfolderAuxAux[len(FUfolderAuxAux) - 1][len(FUfolderAuxAux[len(FUfolderAuxAux) - 1])-2] == "\r"):
					FUfolderAuxAux[len(FUfolderAuxAux) - 1] = FUfolderAuxAux[len(FUfolderAuxAux) - 1][:-2]
					
				else:
					word = FUfolderAuxAux[len(FUfolderAuxAux) - 1]
					word = word[:-1]
					FUfolderAuxAux[len(FUfolderAuxAux) - 1] = word
				FUfolderAuxSub.append(FUfolderAuxAux)
			else:
				FUfolderAux.append(FUfolderAuxSub)
				FUfolderAuxSub = []
				FUfolderAux.append(line)	
		
	FUfolder.append(FUfolderAux)
	i = i + 1



#PRINTING FOR VERIFICATION 	
# print ("\nFU FOLDER\n")	
# i = 0
# while (i < len(FUfolder)):
# 	j = 0
# 	while (j < len(FUfolder[i])):
# 		k = 0
# 		while (k < len(FUfolder[j])):
# 			print FUfolder[i][j][k]
# 			k = k + 1
# 		j = j + 1
# 		
# 	print ("NEXT RECIPE: ")
# 	i = i + 1

# print ("\nFU FOLDER ---- ONE\n")
# 
# print FUfolder[0]
# 
# print ("\nFU FOLDER---- TWO\n")
# 
# print FUfolder[0][0]
# 
# print ("\nFU FOLDER---- THREE\n")
# 
# print FUfolder[0][0][0]

# i = 0
# while (i < len(FUfolder)):
# 	print FUfolder[i]
# 	i = i + 1	



################################################################

# FOON ARRAY
foonOne = []
foonOneAux = []

# KITCHEN ARRAY
kitchen = []
kitchenAux = []

# GOALS ARRAY
goals = []
goalsAux = []

foonResult = []


with open(fileNameOne) as fileOne:
	for line in fileOne:
		if (ord(line[0]) != 47):
			foonOneAux = line.split("\t")
			if (foonOneAux[len(foonOneAux) - 1] == "\n"):
				del foonOneAux[-1]
			else:
				word = foonOneAux[len(foonOneAux) - 1]
				word = word[:-1]
				foonOneAux[len(foonOneAux) - 1] = word
			foonOne.append(foonOneAux)
		else:
			foonOne.append(line)


with open(fileKitchen) as fileTwo:
	for line in fileTwo:
		kitchenAux = line.split("\t")
		if (kitchenAux[len(kitchenAux) - 1] == "\n"):
			del kitchenAux[-1]
		else:
			word = kitchenAux[len(kitchenAux) - 1]
			word = word[:-1]
			kitchenAux[len(kitchenAux) - 1] = word
		
		kitchen.append(kitchenAux)
		
		
with open(fileGoals) as fileThree:
	for line in fileThree:
		goalsAux = line.split("\t")
		if (len(goalsAux) > 2):
			del goalsAux[-1]
		else:
			word = goalsAux[1]
			word = word[:-1]
			goalsAux[1] = word
		goals.append(goalsAux)


################################################################
# PRINTING FOR VERIFICATION 	
# print ("\nFOON ONE\n")	
# 
# i = 0
# while (i < len(foonOne)):
# 	print foonOne[i]
# 	i = i + 1	
# 	
# print ("\nKITCHEN ELEMENTS\n")	
# 
# i = 0
# while (i < len(kitchen)):
# 	print kitchen[i]
# 	i = i + 1
# 
# print ("\nGOALS\n")	
# i = 0
# while (i < len(goals)):
# 	print goals[i]
# 	i = i + 1

# END OF PRINTING	
################################################################



################################################################
# GROUPING GOALS INTO ARRAYS OF OBJECT -> STATE INSIDE OF AN ARRAY
groupedGoals = []
groupedGoalsAux = []

i = 0
while (i < (len(goals) - 1)):
	groupedGoalsAux = []
	groupedGoalsAux.append(goals[i][0])
	groupedGoalsAux.append(goals[i+1][0])
	groupedGoals.append(groupedGoalsAux)
	i = i + 2
	

# print ("\nGROUPED GOALS\n")	
# i = 0
# while (i < len(groupedGoals)):
# 	print groupedGoals[i]
# 	i = i + 1	

# END OF GROUPING GOALS
################################################################	
	
	

################################################################
# FINDING OCURRENCES OF ACTIONS (OBJECT -> STATE)

i = 0	
FU = []
foundM = 0
numFounds = 0

foundGoals = []


while (i < len(foonOne)-1):
	if (not foonOne[i][0].startswith('/')):
		FU.append(foonOne[i])
	else:


		k = 0
		while (k < len(groupedGoals)):
			j = 0
			foundM = 0
			while (j < len(FU)):
				if (FU[j][0].startswith('M')):
					foundM = 1
			
				if (j + 2 == len(FU)):
					if (FU[j][0].startswith('O')):
						if (FU[j][0] == groupedGoals[k][0] and FU[j+1][0] == groupedGoals[k][1]):
							numFounds = numFounds +1
							foundGoals.append(FU)
							foundGoals.append(["//"])
				j = j + 1
			k = k + 1					
		FU = []	
	i = i + 1
		
# print ("\nNUMBER OF FOUNDS\n")	
# print (numFounds)
# 	
# print ("\nGOALS FOUND ON FOON\n")
# i = 0
# while (i < len(foundGoals)):
# 	j = 0
# 	while (j < len(foundGoals[i])):
# 		print foundGoals[i][j]
# 		j = j + 1
# 	i = i + 1
	
# COPY OF FOUND GOALS 
copyfoundGoals = foundGoals
FG = foundGoals

# END OF
################################################################	



################################################################
# COMPUTE THE LENGTH OF THE GOALS COMPLETE RECIPE

lengths = []
numFU = 0
i = 0

# print ("\n **FG **\n")	
# print FG[0]
# 
# print ("\n **FUFOLDER **\n")	
# print FUfolder[0][1][0]

completeGoals = []
completeGoalsAux = []

while (i < len(FG)):
	j = 0
	while (j < len(FUfolder)):
		numFU = 0
		k = 0
		while (k < len(FUfolder[j])):
			if (not FUfolder[j][k][0] == "/"):
				if (FG[i] == FUfolder[j][k]):
					lengths.append(numFU)
					completeGoalsAux.append(FUfolder[j][k])
					completeGoals.append(completeGoalsAux)
					completeGoals.append("//\n")
					break
				else:
					completeGoalsAux.append(FUfolder[j][k])
					numFU = numFU + 1
			else:
				completeGoalsAux.append("//\n")
			k = k + 1
		completeGoalsAux = []
		j = j + 1
		
	i = i + 1
	
# print ("\n ** COMPLETE GOALSSS **\n")	
# i = 0
# while (i < len(completeGoals)):
# 	j = 0
# 	while (j < len(completeGoals[i])):
# 		k = 0
# 		while (k < len(completeGoals[i][j])):
# 			print completeGoals[i][j][k]
# 			k = k + 1
# 		j = j + 1
# 	i = i + 1
# 
# print ("\n **LENGTHS **\n")	
# i = 0
# while (i < len(lengths)):
# 	print lengths[i]
# 	i = i + 1


# END OF
################################################################	

cleanCompleteGoals = []
i = 0
while (i < len(completeGoals)):
	j = 0
	#cleancompleteGoalsAux = []
	while (j < len(completeGoals[i])):
		k = 0
		cleancompleteGoalsAux = []
		while (k < len(completeGoals[i][j])):
			if (completeGoals[i][j][k][0][0].startswith('O')):
				del completeGoals[i][j][k][-1]
				cleancompleteGoalsAux.append(completeGoals[i][j][k])
			else:
				if (not completeGoals[i][j][k][0][0].startswith('M')):	
					cleancompleteGoalsAux.append(completeGoals[i][j][k])
				else:
					del completeGoals[i][j][k][-1]
			k = k + 1
			
		j = j + 1
		cleanCompleteGoals.append(cleancompleteGoalsAux)
	i = i + 1

print ("*** HEREEEEEEEEEEEEEEEE ***")

i = 0
while (i < len(cleanCompleteGoals)):
	j = 0
	while (j < len(cleanCompleteGoals[i])):
		print cleanCompleteGoals[i][j]
		j = j + 1
	i = i + 1



################################################################
# CHANGE foonOne TO THREE LEVEL LIST

orgfoonOne = []
orgfoonOneAux = []
i = 0
while (i < len(foonOne)):
	if (not foonOne[i][0][0] == "/"):
		orgfoonOneAux.append(foonOne[i])
	else:
		orgfoonOne.append(orgfoonOneAux)
		orgfoonOne.append(["//"])
		orgfoonOneAux = []
	
	i = i + 1



# END OF
################################################################	




################################################################
# CLEANING DATA FOUND GOALS
	
i = 0
cleanfoundGoals = []
while (i < len(foundGoals)):
	j = 0
	cleanfoundGoalsAux = []
	while(j < len(foundGoals[i])):
		if (foundGoals[i][j][0].startswith('O')):
			del foundGoals[i][j][-1]
			cleanfoundGoalsAux.append(foundGoals[i][j])
		else:
			if (not foundGoals[i][j][0].startswith('M')):	
				cleanfoundGoalsAux.append(foundGoals[i][j])
			else:
				del foundGoals[i][j][-1]
		j = j + 1
	cleanfoundGoals.append(cleanfoundGoalsAux)
	i = i + 1
	

# print ("\nCLEAN GOALS FOUND ON FOON\n")
# i = 0
# while (i < len(cleanfoundGoals)):
# 	j = 0
# 	while (j < len(cleanfoundGoals[i])):
# 		print cleanfoundGoals[i][j]
# 		j = j + 1
# 	i = i + 1
		
# END OF
################################################################	
	


FUgoal = []
FUcompleteAux = []
FUcomplete = []

missingIngredients = []
missingIngredientsAux = []
w = -1

print ("\nKITCHEN ITEM\n")

print kitchen[0]

print ("\nCLEAN COMPLETE GOAL ITEM\n")

print cleanCompleteGoals[1][0]
print len(cleanCompleteGoals)

print ("\nCLEAN FOUND GOAL ITEM\n")

print cleanfoundGoals[0][0]
print "\n"
i = 0




################################################################
# 
# 
FUgoal = []
FUcompleteAux = []
FUcomplete = []
FUcomplete2 = []
missingIngredients = []
missingIngredientsAux = []
w = -1

print ("\nCOMPLETE GOAL \n")

print completeGoals[0]

print ("\nCLEAN COMPLETE GOAL ITEM\n")

print cleanCompleteGoals[0][0]
totalFounds = 0
founds = 0
tempCompRecipes = []
CompRecipes = []
tempFU = []
w = 0
print "\n"
i = 0
while (i < len(cleanCompleteGoals)):
	
	if (not cleanCompleteGoals[i][0][0].startswith('/')):
		z = 0
		while (z < len(cleanCompleteGoals[i])):
			FUgoal.append(cleanCompleteGoals[i][z])
			
			z = z + 1
		
	else:
		if (len(FUgoal) == 0):
			print ("Total number: ")
			print totalFounds/2
			print ("Total number of founds: ")
			print founds
			
			if ( (totalFounds/2) == founds):
				w = w + 1
				print ("RECIPE AVAILABLE")
				tempFU.append(completeGoals[w])
				

			totalFounds = 0
			founds = 0
			
			
			print ("NEW RECIPE")
			
		print FUgoal
		print len(FUgoal)
		totalFounds = totalFounds + len(FUgoal)
		w = w + 1
		j = 0
		while (j < len(FUgoal)-1):
			k = 0
			ingredientsFound = 0
			found = 0

			while (k < len(kitchen)-1):
				if (FUgoal[j] == kitchen[k] and FUgoal[j+1] == kitchen[k+1]):
					FUcompleteAux.append(kitchen[k])
					FUcompleteAux.append(kitchen[k+1])
					print ("FOUND")
					founds = founds + 1
					found = 1
					break
				k = k + 1
				
			if (found == 0):
				missingIngredientsAux.append(FUgoal[j])
				missingIngredientsAux.append(FUgoal[j+1])
				print ("MISSING")
			
			j = j + 2
		
		if (FUcompleteAux == FUgoal):
			FUcomplete2.append(FUgoal)
			FUcomplete2.append(["//"])
		
		if (FUcompleteAux == FUgoal and (totalFounds/2) == founds and not len(FUgoal) == 0 ):
			FUcomplete.append(FUgoal)
			tempCompRecipes.append(FUgoal[-1])
			FUcomplete.append(["//"])
		
		if (not len(missingIngredientsAux) == 0):
			missingIngredients.append(missingIngredientsAux)
			missingIngredients.append(["//"])
			missingIngredientsAux = []
		FUgoal = []
		FUcompleteAux = []
	i = i + 1



print ("\nRECIPES AVAILABLE IN KITCHEN\n")
i = 0
while (i < len(FUcomplete)):
	j = 0
	while (j < len(FUcomplete[i])):
		print FUcomplete[i][j]
		j = j + 1
	i = i + 1



# print ("\nMISSING INGREDIENTS\n")
# i = 0
# while (i < len(missingIngredients)):
# 	j = 0
# 	while (j < len(missingIngredients[i])):
# 		print missingIngredients[i][j]
# 		j = j + 1
# 	i = i + 1



	




# 	i = i + 1

i = 0
with open('retrieve.txt', 'w') as f:
	while (i < len(FUcomplete)):
		j = 0
		while (j < len(FUcomplete[i])):
			str = ""
			k = 0
			while (k < len(FUcomplete[i][j])):
				str = str + FUcomplete[i][j][k] + "\t"
				
				k = k + 1
			if (str.startswith('/')):
				str = "//"
				f.write("%s\n" % str)	
			else:
				str = str[:-1]
				f.write("%s\n" % str)
			j = j + 1
		i = i + 1


i = 0
with open('retrieve2.txt', 'w') as f:
	while (i < len(FUcomplete2)):
		j = 0
		while (j < len(FUcomplete2[i])):
			str = ""
			k = 0
			while (k < len(FUcomplete2[i][j])):
				str = str + FUcomplete2[i][j][k] + "\t"
				
				k = k + 1
			if (str.startswith('/')):
				str = "//"
				f.write("%s\n" % str)	
			else:
				str = str[:-1]
				f.write("%s\n" % str)
			j = j + 1
		i = i + 1













