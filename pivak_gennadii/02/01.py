#Variant 1

string_list = []
string_list_o = []
string_list_x = []
len_list_o = 0
len_list_x = 0

string_list = list(input('input string '))
#print(string_list)
for i in range(len(string_list)):
    if string_list[i] in ('o', 'O'):
        string_list_o.append(string_list[i])
    if string_list[i] in ('x', 'X'):
        string_list_x.append(string_list[i])
#print(string_list_o)
#print(string_list_x)
len_list_o = len(string_list_o)
len_list_x = len(string_list_x)

if (len_list_o == len_list_x) or (len_list_o == 0 and len_list_x == 0):
    print(True)
else:
    print(False)

#Variant 2

string_list = ()
count_o = 0
count_x = 0

string_list = input('input string ')

for i in range(len(string_list)):
    if string_list[i] in ('o', 'O'):
        count_o += 1
    if string_list[i] in ('x', 'X'):
        count_x += 1

if (count_o == count_x) or (count_o == 0 and count_x == 0):
    print(True)
else:
    print(False)

