#Metnden sait silen proqram
metn ="Data integration is a precursor to data analysis, and data analysis is closely linked to data visualization and data dissemination"
saitler = ["a", "e", "i", "o", "u"]
for x in metn:
    if x in saitler:
        metn= metn.replace(x,"")

print(metn)

