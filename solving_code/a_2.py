import sys
import FinanceDataReader as fdr

import matplotlib.pyplot as plt
#python a_2.py AAPL 2019 2020



def get_max_money(ary,low,high):
    if low == high:
        return ary[low],low,low
    mid = (low+high)//2
    left_sum,left_buy,left_sell = get_max_money(ary,low,mid)
    right_sum,right_buy,right_sell = get_max_money(ary,mid+1,high)

    find_left=0
    find_left_sum =0

    find_buy=mid
    find_sell =mid+1
    for i in reversed(range(low,mid+1)):
        find_left_sum += ary[i]
        if(find_left_sum > find_left):
            find_buy=i
            find_left=find_left_sum

    find_right =0
    find_right_sum = 0
    for i in range(mid+1,high):
        find_right_sum += ary[i]
        if(find_right_sum > find_right):
            find_sell=i
            find_right = find_right_sum


    middle_sum = find_left + find_right
    if left_sum > middle_sum and left_sum > right_sum:
        return left_sum,left_buy,left_sell
    elif right_sum > middle_sum and right_sum > left_sum:
        return right_sum,right_buy,right_sell

    return middle_sum, find_buy, find_sell



stock = sys.argv[1]
startYear = sys.argv[2]
endYear = sys.argv[3]

df = fdr.DataReader(stock, startYear, endYear)
df['Close'].plot()

price_list = df['Close'].tolist()
day_list = df.index.tolist()
price_diff_list=[0]

ary_len = len(price_list)


for i in range(1,ary_len):
    price_diff_list.append(price_list[i]-price_list[i-1])

profit,buy,sell = get_max_money(price_diff_list,0,ary_len-1)
print(f" 종목: {stock}, 매입날짜: {day_list[buy]}, 매도날짜: {day_list[sell]}, 총 수익:{profit}")

plt.axvline(x=day_list[buy], color='r')
plt.axvline(x=day_list[sell], color='r')
plt.show()