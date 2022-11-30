#
# parses log files and counts clicks on user interface 1 (biodiv1) and user interface 2 (biodiv 2) 
# input: folder per user and a log file in each folder
#  
# output: columns with number of clicks added to user_ip.csv
#
# @author: Felicitas Loeffler, 2022

# import regex library
import re
import datetime
import os
import pandas as pd
import argparse



# pattern for sessionID
userRegex = "({(Organism|Process|Quality|Environment|Material)\s?inst\s?=\s?\"(http://purl.obolibrary.org/obo/[A-Za-z]+_[A-Z0-9]+)\"})"

#userFile
userFile = 'user_ip.csv'

path = "data/raw_data/survey_data/"
n_users = 20



def readLogfile():
	# open user file
	userPath = os.path.join(path+userFile)
	print(userPath)
	userMetadata = pd.read_csv(userPath, sep=";")

	for i in range(n_users):
		user_id = i+1
		# for each user
		log_path = os.path.join(path, f"User{user_id}", f"logs_user{user_id}.txt")
		print(log_path)
		user_data = userMetadata[userMetadata.index == i]
		#print(user_data)
		ip = user_data['ip']
		print(ip.to_string(index=False))
		ipClean = ip.to_string(index=False).replace('.','\.')
		pattern = r"\"ip\":\"<ip>\""
		patternClicksBiodiv1 = ".*(\W\w+\sclicked).*(\"biodiv1\").*(\"ip\":\"<ip>\")".replace('<ip>',ipClean)
		patternClicksBiodiv2 = ".*(\W\w+\sclicked).*(\"biodiv2\").*(\"ip\":\"<ip>\")".replace('<ip>',ipClean)
		patternShowBiodivClicksBiodiv1 = ".*(Show Biodiv clicked).*(\"biodiv1\").*(\"ip\":\"<ip>\")".replace('<ip>',ipClean)
		patternShowBiodivClicksBiodiv2 = ".*(Show Biodiv clicked).*(\"biodiv2\").*(\"ip\":\"<ip>\")".replace('<ip>',ipClean)
		patternExplanationClicksBiodiv1 = ".*(Explanation clicked).*(\"biodiv1\").*(\"ip\":\"<ip>\")".replace('<ip>',ipClean)
		patternExplanationClicksBiodiv2 = ".*(Explanation clicked).*(\"biodiv2\").*(\"ip\":\"<ip>\")".replace('<ip>',ipClean)
		
		#patternClicks = pattern.replace('<ip>',ipClean)
		#print(pattern)
		# open file
		try:
			logfile = open(log_path, "r")
			# for each line in the sparql file
			lines = logfile.readlines()
			countBiodiv1 = 0;
			countBiodiv2 = 0;
			countShowBiodivClickedBiodiv1 = 0;
			countShowBiodivClickedBiodiv2 = 0;
			countExplanationClickedBiodiv1 = 0;
			countExplanationClickedBiodiv2 = 0;
			for j,line in enumerate(lines): 
				# when matching the narrower pattern
				#print(pattern)
				regex = r"\"ip\":\"141\.35\.40\.29\""			   
				#print(line)
				biodiv1 = re.search(patternClicksBiodiv1, line)
				biodiv2 = re.search(patternClicksBiodiv2, line)
				showBiodivClicked_biodiv1 = re.search(patternShowBiodivClicksBiodiv1, line)
				showBiodivClicked_biodiv2 = re.search(patternShowBiodivClicksBiodiv2, line)
				explanationClicked_biodiv1 = re.search(patternExplanationClicksBiodiv1, line)
				explanationClicked_biodiv2 = re.search(patternExplanationClicksBiodiv2, line)
				if biodiv1:
					countBiodiv1 = countBiodiv1 + 1
					#print ("Match was found at line "+str(j)+", {start}-{end}: {match}".format(start = correct.start(), end = correct.end(), match = correct.group()))
					#print("user"+str(i)+": "+ line)
				if biodiv2:
					countBiodiv2 = countBiodiv2 + 1
				if showBiodivClicked_biodiv1:
					countShowBiodivClickedBiodiv1 = countShowBiodivClickedBiodiv1 + 1
				if showBiodivClicked_biodiv2:
					countShowBiodivClickedBiodiv2 = countShowBiodivClickedBiodiv2 + 1
				if explanationClicked_biodiv1:
					countExplanationClickedBiodiv1 = countExplanationClickedBiodiv1 + 1
				if explanationClicked_biodiv2:
					countExplanationClickedBiodiv2 = countExplanationClickedBiodiv2 + 1
			#print("clicks biodiv1: "+str(countBiodiv1))
			#print("clicks biodiv2: "+str(countBiodiv2))

			userMetadata.loc[(userMetadata.index == i), "clicksCountedBiodiv1"] = countBiodiv1
			userMetadata.loc[(userMetadata.index == i), "clicksCountedBiodiv2"] = countBiodiv2
			userMetadata.loc[(userMetadata.index == i), "BiodivClicksCountedBiodiv1"] = countShowBiodivClickedBiodiv1
			userMetadata.loc[(userMetadata.index == i), "BiodivClicksCountedBiodiv2"] = countShowBiodivClickedBiodiv2
			userMetadata.loc[(userMetadata.index == i), "ExplanationClicksCountedBiodiv1"] = countExplanationClickedBiodiv1
			userMetadata.loc[(userMetadata.index == i), "ExplanationClicksCountedBiodiv2"] = countExplanationClickedBiodiv2
			userMetadata.loc[(userMetadata.index == i), "clicksCounted"] = countBiodiv1 + countBiodiv2
			# close the file
			logfile.close()
		except FileNotFoundError:
			print(log_path + ' not found')
			continue
	userMetadata.to_csv(userPath, sep=";", index=False)
			


#main method
if __name__ == '__main__':
	try:
		now = datetime.datetime.now()
		print("\nProgram started " + str(now) + ".\n")
		
		#at first create the simple URI files - no expansion
		readLogfile()
		end = datetime.datetime.now()
		print("\nProgram ended " + str(end) + ".\n")
		
	except Exception as ex:
		print(ex)




