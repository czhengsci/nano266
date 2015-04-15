import os, fnmatch,csv,re

pjoin = os.path.join
matches = {}
csvfile_name = 'data_test_record.csv'

def file_proc(filepath):
	match_line=[]
	with open(filepath,'r') as datafile: 
		for line in datafile:
			line = line.rstrip()
			if re.search('Total DFT energy',line):
				match_line = line

	return match_line

def csv_write(csvfile,datatowrite):
	with open(csvfile,'wb') as csvfile:
		datawriter = csv.writer(csvfile, delimiter=' ')
		datawriter.writerow(datatowrite)


for root, dirnames, filenames in os.walk('.'):
  for filename in fnmatch.filter(filenames, '*.nwout'):
  		print filename
  		# filepath = pjoin(root,filename)
  		# Energy_line = file_proc(filepath)
  		# datatorecord = [dirnames,Energy_line,filepath]
  		# print datatorecord
  		# csv_write(csvfile_name,datatorecord)


  	# data_element_type = dirnames
    # matches.append(os.path.join(root, filename))