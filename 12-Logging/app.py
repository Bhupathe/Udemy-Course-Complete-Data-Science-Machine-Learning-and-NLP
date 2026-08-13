import logging

## logging setting

## configuring logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%d-%m-%y %H:%M:%S ',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticApp')

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} =  {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
if __name__ == "__main__":
    add(10, 15)
    multiply(15, 10)
    multiply(10, 2)
    divide(20, 10)