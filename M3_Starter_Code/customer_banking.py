
# for me the new variables that I am creating (decoder ring)
# savings_account - this is the account balance baseline
# sets it as the new_balance (balance + interest_earned)
# interest_earned - this is the interest on the balance
# new_balance - the total balance + interest


# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account 
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter your savings balance: "))
    savings_interest = float(input("Enter your savings interest rate: "))
    savings_maturity = int(input("Enter the number of months: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, updated_interest_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("Savings account summary: ")
    print("Interest earned: ${:,.2f}".format(updated_interest_savings)) 
    print('Updated Saving Account Balance: ${:,.2f}'.format(updated_savings_balance))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter your CD balance: "))
    cd_interest = float(input("Enter your CD interest rate: "))
    cd_maturity = int(input("Enter the number of months: "))   

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("CD account summary: ")
    print("Interest earned: ${:,.2f}".format(interest_earned_cd)) 
    print("Updated CD Account Balance: ${:,.2f}".format(updated_cd_balance))

if __name__ == "__main__":
    main()
