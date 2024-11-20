text=input('Введите ваш текст:').split()
alpeng="eyuioaEYUIOA"
alprus="аеёиоуыэюяАЕЁИОУЫЭЮЯ"
count=0

for i in text:
    if i[0] in alpeng or i[0] in alprus:
        count+=1

print("Кол-во слов, начинающихся с гласной:", count, sep=" ")