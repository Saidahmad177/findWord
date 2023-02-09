from words import words as w

import random
#
x = random.choice(w)

res = ''
for i in range(len(x)):
    res += '-'

print(f"Men {len(x)}xonali son o'yladim . Topaolasizmi?", '\n', res)

allW = ''
count = 0

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', "g'", "'"]

while True:
    count += 1

    top = input(f"harf kiriting: ")
    if top not in alpha:
        print('bu harf emas')
        continue

    if 1 < len(top):
        print('iltimos 1ta ', end='')
        continue
    if top in allW:
        print(f"siz {top} harfini oldinroq kiritdingiz.Boshqa ", end='')
        continue

    allW += top
    for i in range(len(x)):
        if top == x[i]:
            res = res[:i] + top + res[i + 1:]
    print(res)

    if top in x:
        print(f"{top} harfi to'g'ri")

    if top not in x:
        print(f"{top} harfi men o'ylagan so'z ichida yo'q")

    if res == x:
        print(f"tabriklayman {x} so'zini {count}ta urinishda topdingiz")
    print(f"hozirgacha kiritgan harflaringiz {allW}")
