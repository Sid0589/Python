import json
import os
import sys

output_datadir ='/Users/soupam/Downloads/tmp/'
input_datadir ='/Users/soupam/Downloads/job_skills_reco_gen/'


file = open(input_datadir + 'job_requirements.json','r')
jobreqvar = json.loads(file.read())
file.close()

finalDict ={}
for k,v in jobreqvar.iteritems():
	finalL =[]
	for eachrow in v:
		v2 = eachrow.replace('_',' ')
		finalL.append(v2.lower())
	finalDict[k] = finalL

for filename in os.listdir(input_datadir): 
	if filename.startswith('appln'):
		file = open(input_datadir+filename,'r')
		dictvar = json.loads(file.read())
		file.close()
		tmpKey = {}
		for i in finalDict.keys():
			matchSkills = list(set(dictvar['appln_skills']) & set(finalDict[i]))
			if len(matchSkills)>0:
				score =0
				for m in matchSkills:
					score += 10*(finalDict[i][::-1].index(m))
				tmpKey[i] = score
			else:
				tmpKey[i] =0
		dictvar.update(tmpKey)
		file = open(output_datadir + filename,'w')
		file.write(json.dumps(dictvar))
		file.close()

jobname = raw_input("Enter Designation of Job You want to Search:")
if jobname not in finalDict:
	print 'Type correct and available job name'
	exit(2)
counter = eval(raw_input("Enter the no of top candidates you want to select:"))
result =[]
for filename in os.listdir(output_datadir):
	if filename.startswith('appln'):
		jsonfile = open(output_datadir+filename,'r')
		jsonstr = jsonfile.read()
		dictvar = json.loads(jsonstr)
		jsonfile.close()
		result.append(dictvar[jobname])
result.sort(reverse=True)
cnt =0
res = []
for i in result:
	for filename in os.listdir(output_datadir): 
		if filename.startswith('appln'):
			file = open(output_datadir + filename,'r')
			dictvar = json.loads(file.read())
			file.close()
			if dictvar[jobname] == i:
				res.append([dictvar['appln_name'],dictvar['appln_num'],i])
				cnt+=1
				if cnt >= counter:
					print res
					exit(2)