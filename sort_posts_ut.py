import csv

def test_top():
	fin = open('top_details.csv', 'r')
	reader=csv.DictReader(fin)
	error_count = 0
	for row in reader:
		if not ((int(row['comments'])) > 10 and row['privacy'] == 'public' and len(row['title']) < 40 and int(row['views']) > 9000):
			print(row['id'], " is not a top post and does not belong here. \n")
			error_count += 1
	print (error_count, " errors found. \n")
	return
	
def test_other():
		fin = open('top_details.csv', 'r')
	reader=csv.DictReader(fin)
	error_count = 0
	for row in reader:
		if (int(row['comments'])) > 10 and row['privacy'] == 'public' and len(row['title']) < 40 and int(row['views']) > 9000:
			print(row['id'], " is a top post and does not belong here. \n")
			error_count += 1
	print (error_count, " errors found. \n")
	return
	
def test_td():
	print ("\n A unit test for top daily posts would take n^2 and isn't worth it. \n")
	return
	
print("Unit tests for sort_posts.py. These tests operate on the details version of each file.")
test_top()
test_other()
test_td()