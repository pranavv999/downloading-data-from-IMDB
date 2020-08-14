# downloading-data-from-IMDB

There is a dataset available on IMDb. This dataset is free of charge and non-commercial use. It is really a huge dataset and distributed as a bunch of compressed "tab-seperated values(TSV)" file.
we often need some dummy data for practice, to check our code, check algorithms for large inputs, for SQL practice etc.
this dataset is available on "https://datasets.imdbws.com/" and we are particularly interested here for "name.basics.tsv.gz" file on the same page. This file contains the records of actors, directors, writers, and so on.
I particularly need this data to check some "searching algoritms" so from this "name.basics.tsv.gz" file I am extracting only "name" field.

So,There are two ways to download and extract this data. I am showing both ways :-

1. In first case we are writing a Python Script that will download and extract data for you(refere:"file_name")
2. If you have downloaded the "name.basics.tsv.gz" file manually(refer:"file_name")
