import os
import pytest

import handin2

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    pass
    
def teardown_module(module):
    '''Cleanup process'''
    pass

def test_python_ex1():
    '''Check read_data function'''
    global list_of_rows

    # Check that the function has a doc-string
    assert handin2.read_data.__doc__ !=  None

    # Call function
    list_of_rows = handin2.read_data('experimental_results.txt')

    # Check for number of lines
    assert len(list_of_rows) == 1000

    # Check that there are two values in last line
    assert len(list_of_rows[-1]) == 2
    
def test_python_ex2():
    '''Check calc_averages function'''

    # Check that the function has a doc-string
    assert handin2.calc_averages.__doc__ !=  None

    # Call function
    averages = handin2.calc_averages(list_of_rows)

    # Check that there are two return values
    assert len(averages) == 2

    # Check individual return values
    assert pytest.approx(averages[0], 1E-5) == 0.49505
    assert pytest.approx(averages[1], 1E-5) == 0.49895


def test_python_ex3():
    '''Check transpose_data function'''

    # Check that the function has a doc-string
    assert handin2.transpose_data.__doc__ !=  None

    # Call function
    list_of_columns = handin2.transpose_data(list_of_rows)

    # Check that there are two return values
    assert len(list_of_columns) == 2

    # Check that there are 1000 values in last line
    assert len(list_of_columns[-1]) == 1000
    
