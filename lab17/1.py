#	Напишите операторы защиты от дублирования для заголовочного файла Student.h.
from collections import OrderedDict
k=open("text.txt","w")
name=["Sarah","James","Bond"]
unique = list(OrderedDict.fromkeys(name))
for i in name:
    k.write(i)
private=0
if name==unique:
    private=1
else:
    private=0
if private==1:
    print(False)
else:
    for i in unique:
        k.write(i)
    private=0


