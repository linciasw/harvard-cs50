def main():

    principal = int(input("Enter loan amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    term = int(input("Enter loan term (years): "))


    number_of_payments = term * 12
    monthly_interest_rate = rate / 12 / 100


    monthly_installment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    total_payment = monthly_installment * number_of_payments
    total_interest = total_payment - principal


    print(f"Loan amount: ${principal}")
    print(f"Interest rate: {rate}%")
    print(f"Loan Term: {term} years")


    print(f"Monthly payment: ${monthly_installment:0.02f}")
    print(f"Total payment: ${total_payment:0.02f}")
    print(f"Total interest: {total_interest:0.2f}")



    # create functions for monthly installment 
    # separate the numerator and denominator 
    # optional: learn the tkinter module to create a tiny program




main()