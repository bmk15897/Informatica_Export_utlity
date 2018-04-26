import pandas as pd
import operator

def import_control_file_creation_function(a,b):
	#"pandas_simple.xlsx"
	global af
	df = pd.read_excel(b,sheet_name="Resolution Specification")

	#print(df)

	af=df.sort_values(by=['Folder Name','Object Type'])
	af=af.reset_index(drop=True)

	funCTLcreate(a+".ctl")

def funCTLcreate(export_file):
	global af
	try:
		with open(export_file,"w") as f:
			f.write("<?xml version = \"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<importParams xmlns=\"http://www.informatica.com/oie/importControl/9\">\n<folderMaps>\n")
			used = set()
			folders = [x for x in af['Folder Name'] if x not in used and (used.add(x) or True)]
			del used
			#print(folders)
			objNameSeries=af.groupby('Folder Name')['Source Object Name'].apply(list)
			objTypeSeries=af.groupby('Folder Name')['Object Type'].apply(list)
			objResolutionSeries=af.groupby('Folder Name')['Object Resolution'].apply(list)
			objTargetNameSeries=af.groupby('Folder Name')['Target Object Name'].apply(list)
			objNameList=objNameSeries.tolist();	#this contains the Source Object name
			objTypeList=objTypeSeries.tolist();	#this contains the Object type
			objResolutionList=objResolutionSeries.tolist();	#this contains the Object resolution
			objTargetNameList=objTargetNameSeries.tolist();	#this contains the Target Object name
			#print(objNameList)
			#print(objTypeList)
			#print(objResolutionList)
			
			connection=[]
			for i,n in enumerate(folders):
				if n!='-':
					f.write("<folderMap sourceProject=\""+n+"\" targetProject=\""+n+"\">\n")
					temp = []
					for j,k,l,m in zip(objNameList[i],objTypeList[i],objResolutionList[i],objTargetNameList[i]):
						temp.append([j,k,l,m])
					#print(temp)	
					#temp = sorted(temp, key = operator.itemgetter(1))
					#used=set()
					#types = [x for x in objTypeList if x not in used and (used.add(x) or True)]
					
					types = list(set(objTypeList[i]))
					types.sort()
					#print(types)
					#print(temp)
					cnt=0
					for j in types:
						f.write("<objectList type=\""+j+"\">\n")
						while temp[cnt][1]==j:
							if temp[cnt][2]=='rename':
								f.write("<object name=\""+temp[cnt][0]+"\" resolution=\""+temp[cnt][2]+"\" renameTo=\""+temp[cnt][3]+"\"/>\n")
							else:
								f.write("<object name=\""+temp[cnt][0]+"\" resolution=\""+temp[cnt][2]+"\"/>\n")
							cnt+=1
							if len(temp)==cnt:
								break
						f.write("</objectList>\n")
						if len(temp)==cnt:
							f.write("</folderMap>\n")
							break
					#print(n)
					#print(temp)
				else:
					for j,k,l in zip(objNameList[i],objTypeList[i],objResolutionList[i]):
						connection.append([j,k,l])
			f.write("</folderMaps>\n")
			f.write("<connectionInfo>\n")
			f.write("<rebindMap>\n")
			for con in connection:
				f.write("<rebind source=\""+con[0]+"\" target=\""+con[0]+"\"/>\n")
			f.write("</rebindMap>\n")
			f.write("</connectionInfo>\n")
			f.write("</importParams>")
			#print(connection)
	except IOError:
		print("Could not open file! Please close Excel!")
	except:
		print("No application objects in the list")




