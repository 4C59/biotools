# -*- coding: utf-8 -*-
__metaclass__=type
'''
after run mummer,get the result xxx.mum,then split to forward and reverse
forward
query:Cxxxx
database:picr_xxx:aaa bbb ccc   ==> database:aaa~aaa+ccc,query:bbb~bbb+ccc

reverse
query:Cxxxx Reverse
database:picr_xxx:aaa bbb ccc   ==> database:aaa+ccc~aaa,query:bbb-ccc~bbb
                                ==> database:aaa~aaa+ccc,query:bbb-ccc~bbb

'''
# split mum to forward and reverse
out_forward = "x"
out_reverse = "y"
forward_file = open("x_file", "w")
reverse_file = open("y_file", "w")
mumname = "~/data/PICR.mums"
file = open(mumname, "r")
temp = ""
i = 0
line_len = 15275868 # use "wc -l PICR.mums" get linecount
while (i < line_len):
    if temp == "":
        line = file.readline()
        if line.find("Reverse") == -1:  # if no "reverse",add to forward_s
            #forward_s += line
            forward_file.write(line)
            while (i<line_len):
                i += 1
                line = file.readline()
                if line.find(">")>= 0 or line == "\r\n":  # if read ">",break
                    temp = line
                    break
                else:  # if no ">",add to reverse_s
                    #forward_s += line
                    forward_file.write(line)
        else:  # if "reverse",add to reverse_s
            #reverse_s += line
            reverse_file.write(line)
            while (i<line_len):
                i += 1
                line = file.readline()
                if line.find(">") >= 0:  # if read ">",break
                    temp = line
                    break
                else:  # if no ">",add to reverse_s
                    #reverse_s += line
                    reverse_file.write(line)

    else:
        if temp.find("Reverse") == -1:  # if no "reverse",add to forward_s
            #forward_s += temp
            forward_file.write(temp)
            temp = ""
            while (i<line_len):
                i+=1
                line = file.readline()
                if line.find(">") >= 0 or line == "\r\n":  # if read ">",break
                    temp = line
                    break
                else:  # if no ">",add to reverse_s
                    #forward_s += line
                    forward_file.write(line)
        else:
            #reverse_s += temp
            reverse_file.write(temp)
            temp = ""
            while (i<line_len):
                i+=1
                line = file.readline()
                if line.find(">") >= 0:  # if read ">",break
                    temp = line
                    break
                else:  # if no ">",add to reverse_s
                    #reverse_s += line
                    reverse_file.write(line)

if temp.find("Reverse") >= 0:
    #reverse_s += temp
    reverse_file.write(line)
else:
    #forward_s += temp
    forward_file.write(line)

forward_file.close()
reverse_file.close()
file.close()
