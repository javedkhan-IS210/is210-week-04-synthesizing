#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function that converts farenheit to celsius"""

import decimal

def fahrenheit_to_celsius(degrees):
    """ Converts a degree farenheit to celsius.

    Args:
        degrees(mixed): The degree amount in farenheit.

    Returns:
        decimal: The degree amount in celsius.

    Examples:
         >>>> fahrenheit_to_celsius(212)
         Decimal('100')

    """

degrees = decimal.Decimal(degrees)
degrees = (degrees - 32) * 5  / 9
return degrees
