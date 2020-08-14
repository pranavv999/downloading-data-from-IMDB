'''
parse people name from the "name.basics.tsv.gz" file
already downloaded to you system
'''

import csv
import gzip

def main():
	'''Script Entry point'''
	print("Creating names.txt.....\n")

	with open("names.txt", mode="w", encoding="utf-8") as destination:
		destination.writelines(names())

	print("Successfully created names.txt\n")
	print("Creating sorted_names.txt.....")

	with open("names.txt", encoding="utf-8") as source, open("sorted_names.txt", mode="w", encoding="utf-8") as destination:
		destination.writelines(sorted(source.readlines()))

	print("Successfully created sorted_names.txt\n")



def names():
	'''return a generator of names with trailing newline.'''
	with gzip.open("name.basics.tsv.gz", mode="rt", encoding="utf-8") as tsv_file:
		tsv = csv.reader(tsv_file, delimiter="\t")
		next(tsv) #skip the header
		for record in tsv:
			full_name = record[1]
			yield f"{full_name}\n"




if __name__ == '__main__':
	main()

