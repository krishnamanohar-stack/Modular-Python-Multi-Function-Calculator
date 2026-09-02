from calculator_modules import basic
from calculator_modules import scientific
from calculator_modules import history
from calculator_modules import validators
from calculator_modules import finance
from calculator_modules import number_theory
while True:
    # MAIN MENU
    print("\n========== CALCULATOR ==========")

    print("\n1. Basic")
    print("2. Scientific")
    print("3. Number Theory")
    print("4. Finance")
    print("5. History")
    print("6. Clear History")
    print("7. Exit")

    choice = validators.validate_positive_integer(input("Enter your choice: "))
    if choice is None:
        print("please enter a only integer values")
        continue
    if choice > 7:
        print("please enter a valid number from 1 to 7")
        continue

    #BASIC CALCULATOR
    if choice == 1:
        # SUB MENU IN BASIC CALCULATOR
        

        print("\n--- Basic Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice1 = validators.validate_positive_integer(input("Enter your choice: "))

        if choice1 is None:
            print("please enter only integers")
            continue
        if choice1 > 6:
            print("please enter a valid numbers form 1 to 6")
            continue

        #1.ADDITION

        if choice1 == 1:

            first_number = validators.validate_number(input("enter a first number:-"))
            second_number = validators.validate_number(input("enter a second number:-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue
            result = basic.addition(first_number ,second_number)
            print("Result",result)

            calculation = f"{first_number} + {second_number} = {result}"
            history.save_history(calculation)

        #2.SUBTRACTION

        elif choice1 == 2:

            first_number = validators.validate_number(input("enter a first_number :-"))
            second_number = validators.validate_number(input("enter a second_number :-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue

            result = basic.subtraction(first_number,second_number)
            print("Result",result)

            calculation = f"{first_number} - {second_number} = {result}"
            history.save_history(calculation)

        #3.MULTIPLICATION

        elif choice1 == 3:

            first_number = validators.validate_number(input("enter a first_number :-"))
            second_number = validators.validate_number(input("enter a second_number :-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue

            result = basic.multiplication(first_number,second_number)
            print("Result",result)

            
            calculation =f"{first_number} x {second_number} = {result}"
            history.save_history(calculation)

        #4.DIVISION

        elif choice1 == 4:

            first_number = validators.validate_number(input("enter a first_number :-"))
            second_number = validators.validate_number(input("enter a second_number :-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue
            try:
                result = basic.division(first_number,second_number)
                print("Result",result)
            except ValueError as e:
                print(e)
                continue

            calculation =f"{first_number} / {second_number} = {result}"
            history.save_history(calculation)

        #5.MODULUS

        elif choice1 == 5:

            first_number = validators.validate_number(input("enter a first_number:-"))
            second_number = validators.validate_number(input("enter a second_number:-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue
            try:
                result = basic.modulus(first_number,second_number)
                print("Result",result)
            except ValueError as e:
                print(e)
                continue

            calculation =f"{first_number} % {second_number} = {result}"
            history.save_history(calculation)

        elif  choice1 == 6:
            print("thank you using basic calculator")
            continue
        

    #SCIENTIFIC CALCULATOR
    elif choice == 2:
        #SUB MENU IN SCIENTIFIC CALCULATOR


        print("\n--- Scientific Calculator ---")
        print("1. Power")
        print("2. Square Root")
        print("3. Percentage")
        print("4. Factorial")
        print("5. Absolute Value")
        print("6. Exponential")
        print("7. Natural Logarithm")
        print("8. Logarithm (Base 10)")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        print("12. Cube Root")
        print("13. Exit")

        choice2 = validators.validate_positive_integer(input("Enter your choice: "))
                
        if choice2 is None:
            print("please enter only integers")
            continue
        if choice2 > 12:
            print("please enter a valid number from 1 to 12")
            continue

        #1.POWER

        if choice2 == 1:

            base_number = validators.validate_number(input("enter a base_number:-"))
            exponent_number = validators.validate_number(input("enter a exponent_number:-"))

            if base_number is None or exponent_number is None:
                print("please enter a valid numbers.")
                continue

            result = scientific.power(base_number,exponent_number)
            print("Result",result)

            calculation =f"{base_number} ^ {exponent_number} = {result}"
            history.save_history(calculation)

        #2.SQUARE ROOT

        elif choice2 == 2:
            number = validators.validate_number(input("enter a number:-"))
            

            if number is None:
                print("please enter a valid number.")
                continue

            if number < 0:
                print("please enter a non-negative number")
                continue
        
            result = scientific.square_root(number)
            print("Result",result)

            calculation =f"sqrt{number}= {result}"
            history.save_history(calculation)

        #3.CUBE ROOT

        elif choice2 == 12:
            number = validators.validate_number(input("enter a number:-"))
            if number is None:
                print("please enter a valid number")
                continue
        
            result = scientific.cube_root(number)
            print("Result",result)

            calculation =f"cbrt{number}= {result}"
            history.save_history(calculation)

        #4.PERCENTAGE

        elif choice2 == 3:

            percentage_num = validators.validate_number(input("enter a percentage:-"))
            value = validators.validate_number(input("enter a value:-"))

            if percentage_num is None or value is None:
                print("please enter a valid numbers.")
                continue

            result = scientific.percentage(percentage_num,value)
            print("Result",result)

            calculation =f"{percentage_num}% of {value} = {result}"
            history.save_history(calculation)

        #5.FACTORIAL

        elif choice2 == 4:
            number = validators.validate_number(input("enter a factorial_number:-"))
            if number is None:
                print("Please enter a valid number")
                continue

            if number < 0 or number != int(number):
                print("factorial requires a non-negative integer")
                continue
        
            result = scientific.factorial(int(number))
            print("Result",result)

            calculation =f"{int(number)}! = {result}"
            history.save_history(calculation)

        #6.ABSOLUTE

        elif choice2 == 5:

            number = validators.validate_number(input("enter a number:-"))

            if number is None:
                print("please enter a valid number")
                continue
        
            result = scientific.absolute(number)
            print("Result",result)

            calculation =f"|{number}|= {result}"
            history.save_history(calculation)

        # 7.EXPONENTIAL

        elif choice2 == 6:

            number = validators.validate_number(input("enter a number:-"))
            
            if number is None:
                print("please enter a valid number")
                continue
        
            result = scientific.exponential(number)
            print("Result",result)

            calculation =f"e^{number}= {result}"
            history.save_history(calculation)

        #8.#NATURAL LOGARITHM

        elif choice2 == 7:

            number = validators.validate_number(input("enter a number:-"))
            
            if number is None:
                print("please enter a valid number")
                continue
            if number <=0:
                print("logarthirm requires the positive numbers")
                continue

        
            result = scientific.logarithm(number)
            print("Result",result)

            calculation =f"log{number}= {result}"
            history.save_history(calculation)

        #9.LOG BASE 10

        elif choice2 == 8:

            number = validators.validate_number(input("enter a number:-"))
            
            if number is None:
                print("please enter a valid number")
                continue
            if number <=0:
                print("logarthirm requires the positive numbers")
                continue
            
        
            result = scientific.log10(number)
            print("Result",result)

            calculation =f"log10{number}= {result}"
            history.save_history(calculation)

        #10.TRIGONOMETRIC SINE

        elif choice2 == 9:
            degrees = validators.validate_number(input("enter a number :-"))
            if degrees is None:
                print("please  enter valid degrees.")
                continue
            

            result = scientific.sin(degrees)
            print("Result",result)

            calculation = f"sin({degrees}) = {result}"
            history.save_history(calculation)

        #11.TRIGONOMETRIC COSINE

        elif choice2 == 10 :
    
            degrees = validators.validate_number(input("enter a number :-"))
            if degrees is None:
                print("please  enter valid degrees.")
                continue

            result = round(scientific.cos(degrees),10)
            print("Result",result)

            calculation = f"cos({degrees}) = {result}"
            history.save_history(calculation)

        #12.TRIGONOMETRIC TANGENT

        elif choice2 == 11:
            degrees = validators.validate_number(input("enter a number :-"))
            if degrees is None:
                print("please  enter valid degrees.")
                continue

            result = scientific.tan(degrees)
            print("Result",result)

            calculation = f"tan({degrees}) = {result}"
            history.save_history(calculation)

        elif choice2 == 13:
            print("thank you for choosing scientific calculator")
            continue


   #NUMBER THEORY CALCULATOR
    elif choice == 3:
        # SUB MENU IN NUMBER THEORY CALCULATOR

        print("\n--- Number Theory ---")
        print("1. GCD")
        print("2. HCF")
        print("3. LCM")
        print("4. Check Prime")
        print("5. Prime Factors")
        print("6. Fibonacci")
        print("7. Fibonacci Series")
        print("8. Perfect Number")
        print("9. Divisors")
        print("10. Sum of Divisors")
        print("11. Armstrong Number")
        print("12. Exit")

        choice3 = validators.validate_positive_integer(input("Enter your choice: "))
                
        if choice3 is None:
            print("please enter only integers")
            continue
        if choice3 > 11:
            print("please  enter a valid number from 1 to 11")
            continue

        #1.GCD

        if choice3 == 1:
            first_number = validators.validate_number(input("enter a first_number:-"))
            second_number = validators.validate_number(input("enter a second_number:-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue
            if first_number!=int(first_number) or second_number!=int(second_number):
                print("gcd requires the integers")
                continue

            first_number = int(first_number)
            second_number = int(second_number)

            result = number_theory.gcd(first_number,second_number)
            print('Result',result)

            calculation =f" gcd of {first_number},{second_number} ={result}"
            history.save_history(calculation)

        #2.HCF

        elif choice3 == 2:
            first_number = validators.validate_number(input("enter a first_number:-"))
            second_number = validators.validate_number(input("enter a second_number:-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue
            if first_number!=int(first_number) or second_number!=int(second_number):
                print("hcf requires the integers")
                continue

            first_number = int(first_number)
            second_number = int(second_number)
            
            result = number_theory.hcf(first_number,second_number)
            print('Result',result)

            calculation =f"hcf of {first_number},{second_number} ={result}"
            history.save_history(calculation)

        #3.LCM

        elif choice3 == 3:
            first_number = validators.validate_number(input("enter a first_number:-"))
            second_number = validators.validate_number(input("enter a second_number:-"))

            if first_number is None or second_number is None:
                print("please enter a valid numbers.")
                continue
            if first_number!=int(first_number) or second_number!=int(second_number):
                print("lcm requires the integers")
                continue

            first_number = int(first_number)
            second_number = int(second_number)
            
            result = number_theory.lcm(first_number,second_number)
            print('Result',result)

            calculation =f"lcm of {first_number},{second_number} ={result}"
            history.save_history(calculation)
    
        # 4. CHECK PRIME

        elif choice3 == 4:
        
            number = validators.validate_positive_integer(
                input("Enter a number: ")
            )


            if number is None or number < 2:
                print("Prime check requires an integer >= 2.")
                continue

            result = number_theory.is_prime(number)
            print("Result:", result)

            calculation = f"Is {number} prime? = {result}"
            history.save_history(calculation)


        # 5. PRIME FACTORS
        elif choice3 == 5:
        
            number = validators.validate_positive_integer(
                input("Enter a number: ")
            )

            if number is None:
                print("Prime factors require a positive integer.")
                continue

            
            result = number_theory.prime_factors(number)
            print("Prime Factors:", result)

            
            calculation = f"Prime factors of {number} = {result}"
            history.save_history(calculation)


        # 6. FIBONACCI
        elif choice3 == 6:
            
            number = validators.validate_non_negative_integer(
                input("Enter a number: ")
            )

            if number is None:
                print("Fibonacci requires a non-negative integer.")
                continue

            
            result = number_theory.fibonacci(number)
            print("Result:", result)

            
            calculation = f"Fibonacci({number}) = {result}"
            history.save_history(calculation)

        # 7. FIBONACCI SERIES

        elif choice3 == 7:
            
            number = validators.validate_non_negative_integer(
                input("Enter number of terms: ")
            )

            if number is None:
                print("Fibonacci series requires a non-negative integer.")
                continue

        
            result = number_theory.fibonacci_series(number)
            print("Fibonacci Series:", result)

            
            calculation = f"Fibonacci series ({number} terms) = {result}"
            history.save_history(calculation)


        
        # 8. PERFECT NUMBER
        
        elif choice3 == 8:

            number = validators.validate_positive_integer(
                input("Enter a number: ")
            )

            if number is None:
                print("Perfect number requires a positive integer.")
                continue

            result = number_theory.perfect_number(number)
            print("Result:", result)

            
            calculation = f"Is {number} a perfect number? = {result}"
            history.save_history(calculation)


        
        # 9. DIVISORS
        
        elif choice3 == 9:
            
            number = validators.validate_positive_integer(
                input("Enter a number: ")
            )

            if number is None:
                print("Divisors require a positive integer.")
                continue

            
            result = number_theory.divisors(number)
            print("Divisors:", result)

            
            calculation = f"Divisors of {number} = {result}"
            history.save_history(calculation)


        # 10. SUM OF DIVISORS
        
        elif choice3 == 10:
            
            number = validators.validate_positive_integer(
                input("Enter a number: ")
            )

            if number is None:
                print("Sum of divisors requires a positive integer.")
                continue

            result = number_theory.sum_of_divisors(number)
            print("Sum of Divisors:", result)

            calculation = f"Sum of divisors of {number} = {result}"
            history.save_history(calculation)

        
        # 11. ARMSTRONG NUMBER
        
        elif choice3 == 11:
        
            number = validators.validate_non_negative_integer(
                input("Enter a number: ")
            )

            if number is None:
                print("Armstrong number requires a non-negative integer.")
                continue

            
            result = number_theory.armstrong_numbers(number)
            print("Result:", result)

            calculation = f"Is {number} an Armstrong number? = {result}"
            history.save_history(calculation)    

        elif choice3 == 12:
            print("thank you for choosing number theory calculator")
            continue

 

    #FINANCE CALCULATOR
    elif choice == 4:
            
        # SUB MENU IN FINANCE CALCULATOR

        print("\n--- Finance Calculator ---")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Discount")
        print("4. Profit / Loss")
        print("5. Tax")
        print("6. EMI")
        print("7. Exit")

        choice4 = validators.validate_positive_integer(input("Enter your choice: "))
                    
        if choice4 is None:
            print("please enter only integers")
            continue

        if choice4 > 6:
            print("please enter a valid number from 1 to 6")
            continue

        # 1. Simple Interest
        if choice4 == 1:
            principal = validators.validate_number(input("Enter principal: "))
            rate = validators.validate_number(input("Enter rate of interest: "))
            time = validators.validate_number(input("Enter time: "))

            if principal is None or rate is None or time is None:
                print("Please enter valid numbers.")
                continue

            interest, final_amount = finance.simple_interest(
                principal, rate, time
            )

            print("Interest:", interest)
            print("Final Amount:", final_amount)

            calculation = (
                f"Simple Interest: P={principal}, R={rate}, T={time} "
                f"= Interest {interest}, Final Amount {final_amount}"
            )
            history.save_history(calculation)

        # 2. Compound Interest
        elif choice4 == 2:
            principal = validators.validate_number(input("Enter principal: "))
            rate = validators.validate_number(input("Enter rate of interest: "))
            time = validators.validate_number(input("Enter time: "))

            if principal is None or rate is None or time is None:
                print("Please enter valid numbers.")
                continue

            interest, final_amount = finance.compound_interest(
                principal, rate, time
            )
            interest = round(interest, 2)
            final_amount = round(final_amount, 2)

            print("Interest:", interest)
            print("Final Amount:", final_amount)

            calculation = (
                f"Compound Interest: P={principal}, R={rate}, T={time} "
                f"= Interest {interest}, Final Amount {final_amount}"
            )
            history.save_history(calculation)

        # 3. Discount
        elif choice4 == 3:
            price = validators.validate_number(input("Enter price: "))
            percentage = validators.validate_number(
                input("Enter discount percentage: ")
            )

            if price is None or percentage is None:
                print("Please enter valid numbers.")
                continue

            discount_amount, final_price = finance.discount(
                price, percentage
            )

            print("Discount:", discount_amount)
            print("Final Price:", final_price)

            calculation = (
                f"Discount: {percentage}% of {price} "
                f"= Discount {discount_amount}, Final Price {final_price}"
            )
            history.save_history(calculation)

        # 4. Profit / Loss
        elif choice4 == 4:
            cost_price = validators.validate_number(
                input("Enter cost price: ")
            )
            selling_price = validators.validate_number(
                input("Enter selling price: ")
            )

            if cost_price is None or selling_price is None:
                print("Please enter valid numbers.")
                continue

            result_type, amount, percentage = finance.profit_loss(
                cost_price, selling_price
            )

            print("Result:", result_type)
            print("Amount:", amount)

            if percentage is not None:
                print(f"Percentage: {(percentage)}%")

            calculation = (
                f"Profit/Loss: CP={cost_price}, SP={selling_price} "
                f"= {result_type}, Amount={amount}, Percentage={(percentage)}%"
            )
            history.save_history(calculation)

        # 5. Tax
        elif choice4 == 5:
            price = validators.validate_number(input("Enter price: "))
            tax_percentage = validators.validate_number(
                input("Enter tax percentage: ")
            )

            if price is None or tax_percentage is None:
                print("Please enter valid numbers.")
                continue

            tax_amount, final_price = finance.tax(
                price, tax_percentage
            )

            print("Tax:", tax_amount)
            print("Final Price:", final_price)

            calculation = (
                f"Tax: {tax_percentage}% of {price} "
                f"= Tax {tax_amount}, Final Price {final_price}"
            )
            history.save_history(calculation)

        # 6. EMI
        elif choice4 == 6:
            principal = validators.validate_number(input("Enter principal: "))
            annual_rate = validators.validate_number(input("Enter annual interest rate: "))
            years = validators.validate_number(input("Enter years: "))

            if principal is None or annual_rate is None or years is None:
                print("Please enter valid numbers.")
                continue
            if years <=0:
                print("please enter a valid number of years ")
                continue

            result = finance.emi(principal, annual_rate, years)
        

            print("Monthly EMI:",result)

            calculation = (
                f"EMI: P={principal}, Rate={annual_rate}, Years={years} "
                f"= {result} per month")
            history.save_history(calculation)

        elif choice4 == 7:
            print("thank you for choosing finance calculator")
            continue

    # 5. History
    elif choice == 5:
        result = history.read_history()

        if result is None or result.strip() == "":
            print("No history found.")
        else:
            print("\n========== HISTORY ==========")
            print(result)            
        

    # 6. Clear History
    elif choice == 6:
        history.clear_history()
        print("History cleared successfully.")

    #7.exit 
    elif choice == 7:
        print("thank you for using calculator")
        break









