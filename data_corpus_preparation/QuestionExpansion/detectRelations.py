#
# writes sparql queries into specific files
# input: folder with sparql queries, one query per file, per file (query) 4 different expansion strategies
#  
# output: sparql queries per expansion strategie
#
# @author: Felicitas Loeffler, 2020

# import regex library
import re
import requests
import os
import datetime
import argparse
# path to folder with query files
root = 'entities'

#files= ['query1_entities.txt','query2_entities.txt','query3_entities.txt','query4_entities.txt','query5_entities.txt']

# output folder containing the sparql queries per expansion type
#outputPath = 'relations/'

#method for getting the command line arguments
def commandLine():
	print("read command line")
	#path to sparql
	global pathToSparql
	#path to output folder
	global pathToOutput
	#expansion keyword
	global expansion

	try:
		#command line arguments
		parser = argparse.ArgumentParser(description="run a sparql query on BioCADDIE entities")
		#parser.add_argument("-e", "--expansion", help="Set keyword of expansion (broader, partOf, relationALL, coreRelation)", required=True)
		parser.add_argument("-s", "--sparql", help="Set path to sparql", required=True)
		parser.add_argument("-o", "--output", help="Set path to output folder", required=True)
		args = parser.parse_args()

		pathToSparql = args.sparql
		pathToOutput = args.output
		#expansion = args.expansion
		
	except:
		raise Exception("")


def create_file(request_result, file, entity1):
	#print('j: ',+j)
	# open the file
	filename = file.name.split('.')
	#print(filename[0])
	entity1 = entity1.replace('<','')
	
	entity1 = entity1.replace('>','')
	
	entity1 = re.sub(r"[\n\t]*", "", entity1)
	
	entity1 = entity1.split('/')
	
	file = open(pathToOutput+'/'+filename[0]+'_'+entity1[len(entity1)-1]+'.txt', 'a')
	file.write(request_result)
	file.close()


def relationAllQuery():
	countFiles = 0
	query = open(pathToSparql).read()
	with os.scandir(root) as entries:
		for file in entries:
			print(file)
			#print(file.name)
			countFiles = countFiles + 1
			# open file
			#sparqlFile = open(os.path.join(subdir, file), "r")
			entityFile = open(file, "r")
			# for each line in the sparql file
			lines = entityFile.readlines()
			#print('lines length: ', len(lines))
			entity1 = ""
			for i,line in enumerate(lines): 				
				entity1 = line
				# each line is a URI
				#print('query for object properties: '+URI)
				fullQuery = query.replace('?root', entity1)
				#fullQuery = fullQuery.replace('?entity2', entity2)
				
				#print(fullQuery)
				params = {'query': fullQuery}
				url = 'http://gfbio-git.inf-bb.uni-jena.de/graphDB/repositories/BIODIV'
				request_result = requests.post(url, params).text
				#result = request_result.replace('\n','')
				#if no result is returned the request.text contains 'property,object  ' (17 characters)
				print(len(request_result))
				if(len(request_result)>24):
					create_file(request_result, file, entity1)
			# close the file
			entityFile.close()

def getResults():
	countFiles = 0
	query = open(pathToSparql).read()
	with os.scandir(root) as entries:
		for file in entries:
			if(file):
				print(file)
				print(file.name)
				countFiles = countFiles + 1
				# open file
				entityFile = open(file, "r")
				# for each line in the sparql file
				lines = entityFile.readlines()
				for i,line in enumerate(lines):
					entity1 = line
					URIarray = line.split('/');
					graph = URIarray[len(URIarray)-1].split('_');
					#print('query for object properties: '+URI)
					fullQuery = query.replace('?root', entity1)
					fullQuery = fullQuery.replace('?graph', '<http://gfbio-git.inf-bb.uni-jena.de/BIODIV/'+graph[0].upper()+">")
					#print(fullQuery)
					params = {'query': fullQuery}
					url = 'http://gfbio-git.inf-bb.uni-jena.de/graphDB/repositories/BIODIV'
					request_result = requests.post(url, params).text
					#result = request_result.replace('\n','')
					#if no result is returned the request.text contains 'property,object  ' (17 characters)
					print(len(request_result))
					if(len(request_result)>0): # ?+ propertyLable = 22
						create_file(request_result, file, entity1)
					#if(len(request_result)==147):
					#	print(fullQuery) 
					#	print('entity1:' + entity1)					   
				# close the file
				entityFile.close()


def relationBroader():
	countFiles = 0
	query = open(pathToSparql).read()

	with os.scandir(root) as entries:
		for file in entries:
			print(file)
			#print(file.name)
			countFiles = countFiles + 1
			# open file
			#sparqlFile = open(os.path.join(subdir, file), "r")
			entityFile = open(file, "r")
			# for each line in the sparql file
			lines = entityFile.readlines()
			#print('lines length: ', len(lines))
			for i,line in enumerate(lines): 
				# each line is a URI
				entity = line
				URIarray = line.split('/');
				graph = URIarray[len(URIarray)-1].split('_');
				#print('query for object properties: '+URI)
				fullQuery = query.replace('?entity', entity)
				fullQuery = fullQuery.replace('?graph', '<http://gfbio-git.inf-bb.uni-jena.de/BIODIV/'+graph[0].upper()+">")
				#print(fullQuery)
				params = {'query': fullQuery}
				url = 'http://gfbio-git.inf-bb.uni-jena.de/graphDB/repositories/BIODIV'
				request_result = requests.post(url, params).text
				#result = request_result.replace('\n','')
				#if no result is returned the request.text contains 'property,object  ' (17 characters)
				#print(len(request_result))
				if(len(request_result)>8):
					create_file(request_result, file, entity, "")
			# close the file
			entityFile.close()

			
#main method
if __name__ == '__main__':
	try:
		now = datetime.datetime.now()
		print("\nProgram started " + str(now) + ".\n")
		commandLine()
		#if expansion == "allRelation":
		#	relationAllQuery()
		#elif expansion == "descendantsLabel":
		getResults()
		print("\nquery processed " + str(now) + ", result saved in "+pathToOutput+".\n")
		print("\nProgram ended " + str(now) + ".\n")
	except Exception as ex:
		print(ex)

