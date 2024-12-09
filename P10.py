"""
	n=3
	1	2	3
1	1	2	3	n-i+1
2	1	2	(3-2+1)
3	1	(3-3+1)
n=3
i(1,4) 1<4
   j= 0 < 3-1+1 = 3
   j= 1 <  3
   j= 2 <  3
   j= 3 < 3
==============
i(2<4)
     j= 0  (3-2+1) =2
     j= 1
     j= 2 <2 F
=====================
i(3<4)
     j=0 (3-3+1)
     j=1 <F
==========
i=4 4<4

1	2 	3
1	2
1

"""
"""n=3
for i in range(1,n+1):
    for j in range(n-i+1):
        print(j+1,end="\t")
    print()"""

n = 3
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j , end="\t")
    print()