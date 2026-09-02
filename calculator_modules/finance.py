def simple_interest(principal,rate_of_interest,time):
    interest = (principal * rate_of_interest * time) / 100
    final_amount = principal + interest
    return round(interest,2),round(final_amount,2)

def compound_interest(principal, rate_of_interest, time):
    final_amount = principal*(1 + rate_of_interest/100)**time
    interest =  final_amount - principal
    return round(interest,2),round(final_amount,2)

def discount(price,percentage):
    discount_amount = price * (percentage/100)
    final_price = price - discount_amount
    return discount_amount,final_price

def profit_loss(cost_price, selling_price):

    if selling_price > cost_price:
        profit_amount = selling_price - cost_price

        if cost_price == 0:
            return "profit", profit_amount, None

        profit_percentage = (profit_amount / cost_price) * 100
        return "profit", profit_amount, profit_percentage

    elif cost_price == selling_price:
        return "no profit and no loss", 0, 0

    else:
        loss_amount = cost_price - selling_price
        loss_percentage = (loss_amount / cost_price) * 100
        return "loss", loss_amount,loss_percentage


def tax(price,tax_percentage):

    tax_amount = price *(tax_percentage /100)
    final_price = price + tax_amount

    return tax_amount,final_price

def emi(principal, annual_rate, years):

    monthly_rate = annual_rate / 12 / 100
    months = years * 12

    if monthly_rate == 0:
        return principal / months

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)

    return emi
