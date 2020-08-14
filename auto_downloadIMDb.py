"""
Fetch and parse people names from the IMDb.
Usage:
python download_imdb.py
"""
import csv
import gzip
import shutil
import tempfile
import urllib.request


def main():
	"""Script Entry Point"""

	print("Fetching data from IMDb....\n")
	print("Creating names.txt...\n")

	with open("names.txt", mode="w", encoding="utf-8") as destination:
		destination.writelines(names())

	print("Created names.txt successfully\n")
	print("Creating sorted_names.txt...\n")

	with open("names.txt", encoding="utf-8") as source, open("sorted_names.txt", mode="w", encoding="utf-8") as destination:
		destination.writelines(sorted(source.readlines()))


	print("Created sorted_names.txt successfully\n")


def names():
	"""Return a generator of names with a trailing newline."""
	url = "https://datasets.imdbws.com/name.basics.tsv.gz"
	with urllib.request.urlopen(url) as response:
		with tempfile.NamedTemporaryFile(mode="w+b") as archive:
			shutil.copyfileobj(response, archive)
			archive.seek(0)
			with gzip.open(archive, mode="rt", encoding="utf-8") as tsv_file:
				tsv = csv.reader(tsv_file, delimiter="\t")
				next(tsv) #skip the header
				for record in tsv:
					full_name = record[1]
					yield f"{full_name}\n"



if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print("Aborted")


