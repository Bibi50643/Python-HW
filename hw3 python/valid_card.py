import re
card='4586215'
result=re.search(r'^([1-3]|[7-9])',card)
if re.search(r'([1-3]|[7-9])',card):
    print("YES")
else: print("NO")
