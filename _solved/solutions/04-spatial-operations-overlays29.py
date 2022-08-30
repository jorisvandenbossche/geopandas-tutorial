urban_green_area = urban_green.groupby("district_name")["area"].sum()
urban_green_area.head()