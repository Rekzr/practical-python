principal = 500000
rate = 0.05
payment = 2684.11
extra_payment_start = int(input('Enter start month? '))
extra_payment_end = int(input('Enter end month? '))
extra_payment = float(input('Enter extra payment? '))
total_paid = 0.0
months = 1
extra_payment_live = 0.0

while principal > 0:

    if months >= extra_payment_start and months <= extra_payment_end:
        extra_payment_live = extra_payment
    else:
        extra_payment_live = 0.0

    principal = principal * (1+rate/12) - (payment + extra_payment_live)
    total_paid = total_paid + payment + extra_payment_live
    print(months, round(total_paid,2),round(principal,2))

    if principal > 0:
        months += 1

print(f' Total paid {round(total_paid,2)} \nover {months} months')