from logger import logging

def add(a, b):
    logging.debug("The addition Operation is taking place")
    return a+b

logging.debug("The Addition Function is Called")
add(10, 5)