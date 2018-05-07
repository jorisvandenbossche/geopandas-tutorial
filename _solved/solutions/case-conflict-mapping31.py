def closest_protected_area(mine, protected_areas):
    dist = protected_areas.distance(mine)
    idx = dist.idxmin()
    closest_area = protected_areas.loc[idx, 'NAME_AP']
    return closest_area