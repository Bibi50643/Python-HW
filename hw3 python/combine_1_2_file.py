with open('file_1.txt') as file_1, open('file_2.txt') as file_2: 
    for d1, d2 in zip(file_1, file_2):  
        result = d1+ d2 
 
with open('file_3.txt', 'w') as file_3: 
    file_3.write(result)