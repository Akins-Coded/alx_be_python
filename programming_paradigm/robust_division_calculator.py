def safe_divide(numerator, denominator):

#handle the error
    try:
        numerator = float(input("Enter a Numerator: "))
        denominator = float(input("Enter a Denominator: "))
        result = numerator / denominator
        
        return f"The result is {result}: "

    except ZeroDivisionError:
        return "Not divisible by Zero"

    except ValueError:
        return "Kindly input a Numeric Value"


    