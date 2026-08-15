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



    # create function for monthly installment 
    # separate the numerator and denominator, see below
    # put in try-except block
    # optional: learn the tkinter module to create a tiny program




main()


# FROM GOOGLE
# def calculate_monthly_installment(principal, monthly_interest_rate, number_of_payments):
#     """Calculates the fixed monthly installment for an amortizing loan.

#     Parameters:
#     principal (float): The total loan amount borrowed.
#     monthly_interest_rate (float): The interest rate per month (e.g., 5% annual = 0.05 / 12).
#     number_of_payments (int): Total number of monthly payments (tenure in months).
#     """
#     if monthly_interest_rate == 0:
#         return principal / number_of_payments

#     # Fixed syntax by adding multiplication (*) between rate terms and grouping denominator
#     numerator = (
#         principal
#         * monthly_interest_rate
#         * (1 + monthly_interest_rate) ** number_of_payments
#     )
#     denominator = (1 + monthly_interest_rate) ** number_of_payments - 1

#     return numerator / denominator


# # Example usage assuming a $100,000 principal, 0.5% monthly rate (6% annual), over 360 months (30 years)
# p = 100000.0
# r = 0.06 / 12  # monthly interest rate
# n = 360  # number of payments

# installment = calculate_monthly_installment(p, r, n)
# print(f"Monthly Installment: ${installment:.2f}")