import csv
from datetime import datetime
from operator import itemgetter

def get_top_ids():
	top_ids = set()
	for row in reader:
		#conditions to be a top post
		if(int(row['comments'])) > 10 and row['privacy'] == 'public' and len(row['title']) < 40 and int(row['views']) > 9000:
			top_ids.add(row['id'])
	return top_ids

def get_other_ids(top_ids):
	fin.seek(0) #always reset iterator to the beginning before re-reading the file
	other_ids = set()
	for row in reader:
		if not(row['id'] in top_ids):
			other_ids.add(row['id'])
	return other_ids

def get_top_daily():
	fin.seek(0) #always reset iterator to the beginning before re-reading the file
	#make a disposable copy
	temp_top = top_daily_ids = []
	for row in reader:
		#timestamp in copy should be a date
		if row['timestamp'] != 'timestamp': #kludge because reader was including the headers
			temp_row = row.copy()
			temp_row['timestamp'] = datetime.strptime(temp_row['timestamp'], '%a %b %d %H:%M:%S %Y').date()
			temp_top.append(temp_row)
	temp_top = sorted(temp_top, key=lambda k: (k['timestamp'], k['likes'])) #sort by dates ***THEN*** likes
	b = max(temp_top, key = lambda f: (max(f['likes']), f['timestamp']))
	print(b)
	return
	'''
	for key in keys:
		group=filter(lambda t: t[2]==key,tups)
	for row in temp_top:
		
	fout = open('bar.csv', 'w')
	writer = csv.DictWriter(fout, lineterminator='\n', fieldnames=reader.fieldnames)
	writer.writeheader()
	for thing in top:
		writer.writerow(thing)
	fout.close()
	return
	'''
	
def write_ids(name, id_list):
	#Instead of just outputting a string, we want our file to
	#be readable by a later version of the script so we use a csv.DictWriter with a heading
	fout = open(name, 'w')
	writer = csv.writer(fout, lineterminator='\n') #force the line terminator for compatibility
	for row in id_list:
		writer.writerow([row])
	fout.close()
	return

def write_details(name, id_list):
	fin.seek(0)
	fout = open(name, 'w')
	writer = csv.DictWriter(fout, lineterminator='\n', fieldnames=reader.fieldnames)
	writer.writeheader()
	for row in reader:
		if row['id'] in id_list:
			writer.writerow(row)
	fout.close()
	return
	
with open('posts.csv', 'r') as fin:
	reader=csv.DictReader(fin)
	top_ids = get_top_ids()
	other_ids = get_other_ids(top_ids)
	write_ids('top_posts.csv', top_ids)
	write_ids('other_posts.csv', other_ids)
	write_details('top_details.csv', top_ids)
	write_details('other_details.csv', other_ids)
	get_top_daily()