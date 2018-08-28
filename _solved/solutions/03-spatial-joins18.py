# merging those counts back into the districts dataset
districts2 = districts.merge(counts, on='district_name')
districts2.head()