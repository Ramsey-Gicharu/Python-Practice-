"""
Functions used in preparing Guido's gorgeous lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time based on the EXPECTED_BAKE_TIME."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return preparation time, assuming each layer takes PREPARATION_TIME minutes."""
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total time spent (prep time + bake time elapsed)."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
