def calculate_roi(purchase_price, rent, taxes, insurance, repair, vacancy):
    annual_income = rent * 12
    annual_expenses = taxes + insurance + repair + (vacancy / 100) * annual_income
    net_income = annual_income - annual_expenses
    return (net_income / purchase_price) * 100

property1_roi = calculate_roi(150000, 1000, 2000, 500, 900, 5)
print(f"roi : {property1_roi:.2f}%")


