def safe_divide(numerator, denominator):

#handle the error
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        
        return f"The result is {result}: "

    except ZeroDivisionError:
        return "Not divisible by Zero"

    except ValueError:
        return "Kindly input a Numeric Value"


    