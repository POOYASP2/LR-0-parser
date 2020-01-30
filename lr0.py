# open table File 
f = open("table.txt", "r")
if f.mode == 'r':
    string =f.read()
string =string.replace(" ", "")
string =string.replace(']','').replace('[','')
string =string.replace("'",'').split(",")
string = string[::2]
lr_table = {
    0:{
        "if":['s',2]
    }
}
print(string)

