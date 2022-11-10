import numpy as np 
lst1 = np.array([ 
[1, 2, 3, 6 ], 
[4, 5, 6, 15], 
[7, 8, 9, 24], 
[12,15,18,46] ])


def wrong_number(arr):
    p1=arr[:,:-1]
    sum_p1=p1.sum(axis=1)
    # print(sum_p1)
    p2=arr[:,-1]
    # print(p2)

    tr_arr=arr.T
    s1=tr_arr[:,:-1]
    sum_s1=s1.sum(axis=1)
    # print(sum_s1)
    s2=tr_arr[:,-1]
    # print(s2)
    pos_i = pos_j = None
    wrong=[]
    for i in range(len(arr)):
        if sum_p1[i] != p2[i]:
            # print(sum_p1[i], p2[i])
            # wrong.append(i)
            pos_i = i
            wrong.append(sum_p1[i])
            # wrong.append(sum_s1[i])
        if sum_s1[i] != s2[i]:
            # print(sum_s1[i], s2[i])
            pos_j = i
            # wrong.append(i)
        pass
    arr = arr.T
    # print(pos_i, pos_j)
    # for a in range(len(arr)):
    #     for b in range(len(arr)):
    arr[pos_i][pos_j] = wrong[0]
            
    print(arr)
    if wrong==0:
        return 'List is correct'
    else:
        return wrong
print(wrong_number(lst1))




