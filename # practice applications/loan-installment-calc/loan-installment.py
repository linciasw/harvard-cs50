
    # create function for monthly installment [DONE]
    # separate the numerator and denominator, see below [DONE]
    # create functions for each calculation [DONE]
    # put in try-except block/conditional to handle input validation
    # optional: learn the tkinter module to create a tiny program



def calculate_monthly_installment(p, mir, nofp):

            numerator = p * mir * (1 + mir) ** nofp
            denominator = ((1 + mir) ** nofp -1)

            MI = numerator / denominator

            return float(MI)
            
            # principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / 
            # ((1 + monthly_interest_rate) ** number_of_payments - 1)




def calculate_monthly_interest(r):
        return r / 12 /100


def calculate_number_of_payments(t):
        return t * 12


def create_summary(p, r, t, mi, tp, ti):
    print(f"""
    === Loan Summary ===
    Loan amount: ${p:,}
    Interest rate: {r}%
    Loan term: {t} years


    Monthly payment: $${mi:.2f}
    Total payment: ${tp:,.2f}
    Total interest: ${ti:,.2f}

    ====================

    """
    )
        
        


def main():
    f"""
    === Loan Installment Calculator ===
    """

while True:
    try:
        principal = int(input("Enter loan amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        term = int(input("Enter loan term (years): "))

        if principal <= 0 or rate <= 0 or term <= 0:
            print("All values must be greater than zero")
            continue
            

    except (ValueError, NameError): # parentheses are necessary for multiple errors
        print("All values must be numerical")
        continue # clear indicator to restart the loop safely 
    else:
          break


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




## LOAN PAYMENT FORMULA
#
#             P × r × (1 + r)^n
# PMT = -----------------------------
#                 (1 + r)^n - 1
#
# Key:
# PMT = monthly loan payment
# P   = principal (original loan amount)
# r   = monthly interest rate (annual rate / 12)
# n   = total number of payments (years × 12)
#
# Example:
# P = 50,000
# Annual interest rate = 6.5% = 0.065
# r = 0.065 / 12
# n = 5 × 12 = 60
#
# The formula calculates the fixed monthly payment
# required to pay off the loan over the specified term.



# LOOP KEYWORDS
# pass: A do-nothing placeholder used when code is required by syntax rules, 
# but you want no action taken. 
# It lets the normal flow of code continue downward.

# continue: Stops the current loop run right away and jumps back to the top to 
# evaluate the while condition for the next round.

# break: Exits the loop entirely and moves on to the code right below the loop block.