from random import randint
a = [randint(1, 100) for x in range (10)]
print(a)
q = 0
w = e = r = t = y = u = i = o = p = q
for x in a:
    if x>9:
        while x>0:
          a = x % 10
          if a == 1:
            q +=1
          if a == 2:
            w += 1
          if a == 3:
            e += 1
          if a == 4:
            r += 1
          if a == 5:
            t += 1
          if a == 6:
            y += 1
          if a == 7:
            u += 1
          if a == 8:
            i += 1
          if a == 9:
            o += 1
          if a == 0:
            p += 1   
          x = x // 10
print("1:",q,"2:", w,"3:", e,"4:", r,"5:", t,"6:", y,"7:", u,"8:", i,"9:", o,"0:", p, end='\t')
