#for構文でenumerate()を使う
fruits = ["Apple", "Orange", "Banana"]
for i, v in enumerate(fruits):
    print(i, v)

#enumerateの動作確認
list(enumerate(fruits))
