import pytest

#Function to test square
def square(n):
    return n**2

#Function to test cube
def cube(n):
    return n**3

#Function to test fifth_power
def fifth_power(n):
    return n**5

# testing the square fun
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 shound be 4"
    assert square(3) == 9, "Test Failed: Square of 3 shound be 9"


# testing the cube fun
def test_cube():
    assert cube(2) == 8, "Test Failed: cube of 2 shound be 8"
    assert cube(3) == 27, "Test Failed: cube of 3 shound be 27"


# testing the fifth_power fun
def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: fifth_powe of 2 shound be 32"
    assert fifth_power(3) == 243, "Test Failed: fifth_powe of 3 shound be 243"

# test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")