#花屋の支払金額を決める
#値段
rose_v = 500
sun_v = 400
tulip_v = 700
#個数
rose_c = 18
sun_c = 8 - 2
tulip_c = 21 - 5
#割引率
rate = 0.9
#計算
sum_v = (rose_v * rose_c) + (sun_v * sun_c) + (tulip_v * tulip_c)
payment = sum_v * rate
#結果の表示
print("買い物の合計は", sum_v, "円")
print("割引してもらうと", payment, "円")

print("to be or not to be that's the mothafuckin' question")
print('He told me "I ain\'t give a shit about it"')
print('He told me \n "I ain\'t give a shit about it"')
print('He told me \t "I ain\'t give a shit about it"')