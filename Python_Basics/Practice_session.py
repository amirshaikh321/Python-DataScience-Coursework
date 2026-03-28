# Example 1:

print("\nExample 1:")
print('--'*50)
loan_account = {
    'L101':{'loan_amount': 200000, 'years': 3, 'rate': 10},
    'L102':{'loan_amount': 500000, 'years': 5, 'rate': 9},
    'L103':{'loan_amount': 1000000, 'years': 10, 'rate': 8.5},
    'L104':{'loan_amount': 300000, 'years': 4, 'rate': 11},
    'L105':{'loan_amount': 750000, 'years': 7, 'rate': 9.5}
}

result = {}
for acc in loan_account:
    acc_detail = loan_account[acc]
    p = acc_detail['loan_amount']
    r = acc_detail['rate']
    t = acc_detail['years']
    cp_interest = p*(1+r/100)**t

    result[acc] = f'{cp_interest:.2f}'

print(f" The Compound interest for loans are as follows: \n{result}") 


"""
Example 2: 
"""
print("\nExample 2:")
print('--'*50)
products = {
    'P101':{'price': 50000, 'category': 'Electronics', 'stock': 60},    
    'P102':{'price': 1500, 'category': 'Clothing', 'stock': 120},
    'P103':{'price': 200, 'category': 'Grocery', 'stock': 300},
    'P104':{'price': 30000, 'category': 'Electronics', 'stock': 30},
    'P105':{'price': 2500, 'category': 'Clothing', 'stock': 80}    
}

for p_name, p_details in products.items():
    cat = p_details['category']
    price = p_details['price']
    stock = p_details['stock']
    if cat == 'Electronics':
        if stock >= 50 :
            dis = 20/100
            dis_price = price - (price*dis)
        else:
            dis = 10/100
            dis_price = price - (price*dis)
    elif cat == 'Clothing':
        if stock >= 50 :
            dis = 30/100
            dis_price = price - (price*dis)
        else:
            dis = 15/100
            dis_price = price - (price*dis)
    elif cat == 'Grocery':
        dis = 5/100
        dis_price = price - (price*dis)
    else:
        pass 
    products[p_name]['price'] = dis_price


print(products)

# Example 3: 
print("Example 3:")
print('--'*50)
products = {
    'P101': {'sales': 600, 'rating': 4.7, 'stock': 40, 'category': 'Electronics'},
    'P102': {'sales': 250, 'rating': 4.0, 'stock': 70, 'category': 'Clothing'},
    'P103': {'sales': 320, 'rating': 3.5, 'stock': 30, 'category': 'Grocery'},
    'P104': {'sales': 100, 'rating': 2.8, 'stock': 20, 'category': 'Electronics'},
    'P105': {'sales': 450, 'rating': 4.6, 'stock': 80, 'category': 'Clothing'}
}
per ={}

for pid, details in products.items():
    sales = details['sales']
    rating = details['rating']
    stock = details['stock']
    cat = details['category']

    if rating >= 4.5:
        if sales >= 500:
            performance = 'Excellent'
        else:
            performance = 'Good'
    elif rating >= 3 and rating<=4.4:
        if sales >= 300:
            performance = 'Average'
        else:
            performance = 'Below Average'
    elif rating < 3:
        performance = 'Poor'
    
    else:
        pass

    if stock<=50:
        if sales >= 300:
            restock = "Restock urgently"
        else:
            restock = "Restock"
    elif stock > 50:
        restock = 'Sufficient stock'
    else:
        pass
    per[pid]= {}
    per[pid]['restock']=restock
    per[pid]['Performance']=performance

print(per)

