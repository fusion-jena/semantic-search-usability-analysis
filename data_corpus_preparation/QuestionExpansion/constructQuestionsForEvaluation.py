#
# writes sparql queries into specific files
# input: folder with sparql queries, one query per file, per file (query) 4 different expansion strategies
#  
# output: sparql queries per expansion strategie
#
# @author: Felicitas Loeffler, 2020

# import regex library
import re
import datetime
import os

# path to folder with query files
root = 'revised'
#files= ['query13.sparql', 'query14.sparql']
files= ['query1.sparql', 'query2.sparql', 'query3.sparql', 'query4.sparql', 'query5.sparql', 'query6.sparql', 'query7.sparql', 'query8.sparql', 'query9.sparql', 'query11.sparql','query13.sparql']
#exclude_directories = set(['expanded'])

# output folder containing the sparql queries per expansion type
outputPath = 'expanded/'

# pattern for inst annotations with inst queries
URIRegex = "### simple URI query"

# general pattern for a category with an instance
instPattern = "<http://purl\.obolibrary\.org/obo/[A-Za-z]+_[A-Z0-9]+>"

#coreRelation keyword
coreRelation = "coreRelation"

#stop pattern
stopPattern = "###+"

def remove_last_line_from_string(s):
	return s[:s.rfind('#+')]


def create_expansion_file(expansion):
	#print('j: ',+j)
	# open the file
    outputFile = open(outputPath+expansion+'.txt', 'a')
    inputFile = open('original_questions.txt', 'r')
    lines = inputFile.readlines()
    for i,line in enumerate(lines): 
		# when matching the inst pattern
        #print(line)
        instArray = re.findall(instPattern, line)
        #replacement = {}
        #print(len(instArray))
        for j in instArray:
			#j - URI, e.g: <http://purl.obolibrary.org/obo/NCIT_C12453>
			#j[2] - URI...
            #print(j)
            URI = j[1:-1]
            graphArray = URI.split('/')
            #print(URI)
            #replacement[URI] = []
            graph = graphArray[len(graphArray)-1].split('_');
            if expansion == 'descendants':
                try:
                    path = expansion+'/query'+str(i+1)+'_entities_'+graph[0]+'_'+graph[1]+'.txt'
                    #print(path)
                    expansionFile = os.path.isfile(path)
					
                    replacementArrayURI = getExpansion(i+1,expansion,graph[0],graph[1])
					# replace it only if broader terms could be found
                    if len(replacementArrayURI) >0:
                        for k in replacementArrayURI:
                            newline = re.sub(j, ' | ' + k,line)
                            newline = re.sub(instPattern,'',newline)
                            outputFile.write(newline)
                        #line = re.sub(j,' OR ' + replacement,line,count=1)
                        #print(len(replacementArrayURI))
                        #replacement[URI] = replacementArrayURI
                except:
                    print("no file found for "+ URI)
            #print(replacement[URI])
        #outputFile.write(line)
    outputFile.close()
    inputFile.close()

def getExpansion(i,expansion,graph,graphID):
    replacementArray = [];
    #if expansion == 'broader':
	#	replacement = '('
	#else:
	#	replacement = "({"+category+" "+inst+"=\"http://purl.obolibrary.org/obo/"+graph+"_"+graphID+"\"}"
    try:
        file = open(expansion+'/query'+str(i)+'_entities_'+graph+'_'+graphID+'.txt', 'r')
        lines = file.readlines()
        count = 0
        replacement = ""
        for j,fileLine in enumerate(lines): 
            fileLine = fileLine.replace('\n', '')
			#jump over first line --> only "label"
            if count < 1 or fileLine == '' or fileLine.startswith('_:node') or fileLine == 'label':
                count = count + 1 # just go on, nothing to do here
            else:
                length = len(replacement)
                if length > 2:
                    replacement = replacement + " | "
                replacement = replacement + "'" + fileLine + "'"
                count = count + 1
            if (count >= 100):
                replacementArray.append(replacement)
                replacement=""
                count = 0
        file.close()
    except:
        print("no file found - simple URI replacement")
		#replacement = "{"+category+" "+inst+"=\"http://purl.obolibrary.org/obo/"+graph+"_"+graphID+"\"}"
    replacementArray.append(replacement)
    return replacementArray



#for subdir, dirs, files in os.walk(root):	#this loop though directies recursively 
#	sortedFiles = sorted(os.listdir(root))
	#files[:] = [d for d in sortedFiles if d not in exclude_directories] # exclude directory if in exclude list 





#main method
if __name__ == '__main__':
	try:
		now = datetime.datetime.now()
		print("\nProgram started " + str(now) + ".\n")
		#at first create the simple URI files - no expansion
		#createURIfile()
		# create the "partOf" expansion file
		#create_expansion_file("partOf")
		# create the "narrower" expansion file
		#create_expansion_file("narrower")
		# create the "broader" expansion file
		create_expansion_file("descendants")
		# create the "coreRelations" expansion file
		#create_expansion_file(coreRelation)
	except Exception as ex:
		print(ex)




