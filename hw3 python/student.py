with open('students.txt','r') as students, open('students2.txt','w') as students2:
             s=students.readlines()
             for i in s:
                each=i.split()
                each[0]=each[0].title()
                each[1]=each[1].title()
                each[3]="305-"+each[3]
                # print(each)
                each = " ".join(each)
                students2.write(each + "\n")