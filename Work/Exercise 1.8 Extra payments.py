principal = 500000
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
months = 1

while principal > 0:
    principal = principal * (1+rate/12) - (payment + extra_payment)
    total_paid = total_paid + payment + extra_payment

    if months >= 12:
        extra_payment = 0
    if principal > 0:
        months += 1

print('Total paid', round(total_paid,2), months)