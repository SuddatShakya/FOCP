no_of_std = int(input("How many students? "))
grp_sz = int(input("Required group size? "))
no_of_grp = no_of_std // grp_sz
lftover = no_of_std % grp_sz

if(lftover > 1):
    print("There will be ", no_of_grp, " groups with ", lftover, " students left over")
else:
    print("There will be ", no_of_grp, " groups with ", lftover, " student left over")
    