"""Module for Intrest calculations"""

def simple_intrest(prin,ny,roi):
    """
     Calculation si
    :param prin: principal amount
    :param ny: no.of year
    :param roi: rate of ratio
    :return: SI,Total amount
    """
    si=prin*ny*roi/100
    amount=prin+si
    return si,amount


def compound_intrest(prin,ny,roi):
    """
    Calculation Compound Intrest
    :param prin: principal amount
    :param ny: no.of year
    :param roi: rate of ratio
    :return:  amount
    """
    amount=prin*((1+(roi/ny)) ** (1*ny))
    return amount
