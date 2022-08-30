# Calculate the number of trees in each district
trees_by_district = joined.groupby('district_name').size()