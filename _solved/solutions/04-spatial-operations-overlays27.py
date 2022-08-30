districts_area = combined.groupby("district_name")["area"].sum()
districts_area.head()