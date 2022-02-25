metn="Data integration is a precursor to data analysis, and data analysis is closely linked to data visualization and data dissemination"
list=metn.split()
print(list)
say=0
for i in list:
    if len(i)<5:
        say+=1
print(say)
