

#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return  EXPECTED_BAKE_TIME - elapsed_bake_time
print(bake_time_remaining.__doc__)

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - Number of lasagna layers to prepare.
    :return: int - Total preparation time (in minutes), assuming 2 minutes per layer.
    """
    return number_of_layers * PREPARATION_TIME
print(preparation_time_in_minutes.__doc__)

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time spent cooking the lasagna.

    :param number_of_layers: int - Number of lasagna layers prepared.
    :param elapsed_bake_time: int - Time lasagna has already spent baking.
    :return: int - Total time (in minutes) including preparation and baking.
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time
print(elapsed_time_in_minutes.__doc__)

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
