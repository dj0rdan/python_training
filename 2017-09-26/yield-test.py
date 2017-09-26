# yield で値を返す関数を定義
def gen1to3():
    yield 1;
    yield 2;
    yield 3;

#イテレータオブジェクトを作る
it = gen1to3();
#for構文で繰り返し表示
for i in it:
    print(i)
