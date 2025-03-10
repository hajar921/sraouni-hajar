from typing import Union

# Définition du type Temperature pour les annotations de type
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convertit une température de Celsius en Fahrenheit.

    Formula: F = C × 9/5 + 32

    Args:
        celsius: Température en degrés Celsius.

    Returns:
        Température en degrés Fahrenheit (arrondie à 2 décimales).
    """
    return round(celsius * 9/5 + 32, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Convertit une température de Fahrenheit en Celsius.

    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit: Température en degrés Fahrenheit.

    Returns:
        Température en degrés Celsius (arrondie à 2 décimales).
    """
    return round((fahrenheit - 32) * 5/9, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Convertit une température de Celsius en Kelvin.

    Formula: K = C + 273.15

    Args:
        celsius: Température en degrés Celsius.

    Returns:
        Température en Kelvin (arrondie à 2 décimales).
    """
    return round(celsius + 273.15, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Convertit une température de Kelvin en Celsius.

    Formula: C = K - 273.15

    Args:
        kelvin: Température en Kelvin.

    Returns:
        Température en degrés Celsius (arrondie à 2 décimales).

    Raises:
        ValueError: Si kelvin est inférieur à 0 (température en dessous du zéro absolu).
    """
    if kelvin < 0:
        raise ValueError("La température en Kelvin ne peut pas être inférieure à 0.")
    return round(kelvin - 273.15, 2)
