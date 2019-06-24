# counting the number of stations in each district
counts = joined.groupby('district_name').size()
counts.head()