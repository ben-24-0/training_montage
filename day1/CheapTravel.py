rides, special_ticket, single_price, group_price = map(int, input().split())
# n, m, a, b = map(int,input().split())
groups = rides // special_ticket
cost_groups = groups * group_price
remainder = rides % special_ticket
cost_remainder = min(remainder * single_price, group_price)

total_using_groups = cost_groups + cost_remainder
cost_all_singles = rides * single_price

if total_using_groups < cost_all_singles:
    print(total_using_groups)
else:
    print(cost_all_singles)




if((n//m)*b < n * a):
    print( ((n//m)*b) + min((n%m * a),b))
else:
    print(n*a)

   


