def safe_divide(numerator, denominator):

#handle the error
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        
        return f"The result is {result}: "

    except ZeroDivisionError:
        return "Error: Cannot divide by Zero"

    except ValueError:
        return "Error: Please Enter Numeric Value Only"


    