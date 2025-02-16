def invest(amount, rate, years):
    for year in range(1, years+1):
        amount *= (1+rate)
        rounded_amount= round(amount, 2)
        print(f"year {year}: ${rounded_amount},")
invest(1200,0.05,4)
