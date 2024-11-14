text=input("Введите ваш текст:")
count=0
if (")" not in text) and ("(" not in text):
    print("Скобки отсутствуют!")
else:
    for i in text:
        if i=="(":
            count+=1
        if i==")":
            count-=1
        if count<0:
            break
    if count!=0:
        print("Скобки в вашем тексте не сбалансированы!")
    else:
        print("Скобки сбалансированы! Поздравляем!")