def big_number_sum(big1: str, big2: str):
        q1 = len(big1) % 3
        q2 = len(big2) % 3
        lst1 = []
        lst2 = []
        if q1 == 1:
            lst = ['0', '0']
            lst.append(big1[0])
        if q1 == 2:
            lst = ['0']
            lst.append(big1[0])
            lst.append(big1[1])
        lst1.append(lst)
        if q2 == 1:
            lst = ['0', '0']
            lst.append(big2[0])
        if q2 == 2:
            lst = ['0']
            lst.append(big2[0])
            lst.append(big2[1])
        lst2.append(lst)
        i = q1
        while i < len(big1):
           count = 3
           num = []
           while (count > 0) and (i < len(big1)):
              num.append(int(big1[i]))
              count -= 1
              i += 1
           lst1.append(num)
        ii = q2
        while ii < len(big2):
           count = 3
           num = []
           while (count > 0) and (ii < len(big2)):
              num.append(int(big2[ii]))
              count -= 1 
              ii += 1
           lst2.append(num)
        if len(lst1) < len(lst2):
            res = []
            rem = 0
            for j in range(len(lst1) - 1, -1, -1):
                for jj in range(len(lst1[j]) - 1, -1, -1):
                      _sum = int(lst1[j][jj]) + int(lst2[j][jj]) + rem
                      rem = _sum // 10
                      _sum %= 10 
                      res.append(_sum) 
            length = len(lst2) - len(lst1)
            for k in range(length, -1, -1):
                for kk in range(len(lst2[k]) - 1, -1, -1):
                    _sum = int(lst2[k][kk]) + rem
                    rem = _sum // 10
                    _sum %= 10 
                    res.append(_sum) 
            if rem != 0:
                 res.append(rem)
        elif len(lst1) > len(lst2):
            res = []
            rem = 0
            for j in range(len(lst2) - 1, -1, -1):
                for jj in range(len(lst2[j]) - 1, -1, -1):
                      _sum = int(lst1[j][jj]) + int(lst2[j][jj]) + rem
                      if _sum > 9:
                         rem = 1 
                         _sum %= 10 
                      else:
                         rem = 0
                      res.append(_sum) 
            length = len(lst1) - len(lst2)
            for k in range(length, -1, -1):
                for kk in range(len(lst1[k]) - 1, -1, -1):
                    _sum = int(lst1[k][kk]) + rem
                    if  _sum > 9:
                        rem = 1
                        _sum %= 10 
                    else:
                        rem = 0 
                    res.append(_sum)
            if rem != 0:
                res.append(rem)
        else:
            res = []
            rem = 0
            for j in range(len(lst2) - 1, -1, -1):
                for jj in range(len(lst2[j]) - 1, -1, -1):
                      _sum = int(lst1[j][jj]) + int(lst2[j][jj]) + rem
                      if _sum > 9:
                         rem = 1 
                         _sum %= 10 
                      else:
                         rem = 0
                      res.append(_sum) 
            if rem != 0:
                res.append(rem)
        ij = 0
        new_res = []
        while ij < len(res):
             count = 3
             num = []
             while (count > 0) and (ij < len(res)):
                 num.append(res[ij])
                 ij += 1
                 count -= 1
             num = num[::-1]
             new_res.append(num)
        res = new_res[::-1]
        if res[0][0] == 0:
             for num in res:
                num.remove(num[0])
                break
        return res 
print(big_number_sum('1374748282984393923', '892783892929292929029036'))
