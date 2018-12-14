






# 2. Special Pythagorean triplet

# def check_pathagorean(a, b, c):
#     return (a**2) + (b**2) == (c**2)

# SUM = 1000

# for i in range(1, SUM):
#     for j in range(i+1, SUM):
#         c = SUM - (i + j)
#         if(check_pathagorean(i, j, c)):
#             if i + j + c == SUM:
#                 print(i)
#                 print(j)
#                 print(c)
#                 break


# 3. Find the single different character between two strings
a='none of this makes sense'
b='none of this makes sense. nope'

if len(a)>len(b): 
    res=a.replace(b,'')             #get diff
else: 
    res=b.replace(a,'')             #get diff

print(res.strip())