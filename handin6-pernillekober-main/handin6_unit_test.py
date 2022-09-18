import sys
import re
import pytest
import os

import handin6

class TestPythonPart:

    
    @classmethod
    def setup_class(cls):
        TestPythonPart.data = None

        
    def test_python_ex1(self):
        '''Test read_mnist_csv function'''

        # Check that the function has a doc-string
        assert handin6.read_mnist_csv.__doc__ !=  None
        assert len(handin6.read_mnist_csv.__doc__) > 0

        TestPythonPart.data = handin6.read_mnist_csv('mnist_test_200.csv')

        # Check for expected length of word file
        assert self.data.shape == (200, 785)

        
    def test_python_ex2(self):
        '''Test group_by_label function'''

        # Check that the function has a doc-string
        assert handin6.group_by_label.__doc__ !=  None
        assert len(handin6.group_by_label.__doc__) > 0

        TestPythonPart.groups = handin6.group_by_label(TestPythonPart.data)

        # Check that there are 10 groups
        assert len(TestPythonPart.groups) == 10

        # Check dimensions of group members
        for group in TestPythonPart.groups:
            assert group.shape[0] > 0
            assert group.shape[1] == 785

            
    def test_python_ex3(cls):
        '''Test the convert_to_images function'''

        # Check that the function has a doc-string
        assert handin6.convert_to_images.__doc__ !=  None
        assert len(handin6.convert_to_images.__doc__) > 0

        TestPythonPart.grouped_images = handin6.convert_to_images(TestPythonPart.groups)
        
        # Check that there are 10 groups
        assert len(TestPythonPart.grouped_images) == 10

        # Check dimensions of group members
        for group in TestPythonPart.grouped_images:
            assert len(group.shape) == 3
            assert group.shape[0] > 0
            assert group.shape[1] == 28
            assert group.shape[2] == 28

            
    def test_python_ex4(cls):
        '''Test the draw_image function'''

        # Check that the function has a doc-string
        assert handin6.draw_image.__doc__ !=  None
        assert len(handin6.draw_image.__doc__) > 0

        import matplotlib.pyplot as plt

        # Call drawing function
        handin6.draw_image(TestPythonPart.grouped_images[0][0])

        # Check how many images have been plotted
        assert len(plt.gcf().get_axes()) >= 1
        

    def test_python_ex5(cls):
        '''Test the draw_image_row function'''

        # Check that the function has a doc-string
        assert handin6.draw_image_row.__doc__ !=  None
        assert len(handin6.draw_image_row.__doc__) > 0

        import matplotlib.pyplot as plt

        # Call drawing function
        handin6.draw_image_row(TestPythonPart.grouped_images)

        # Check how many images have been plotted
        assert len(plt.gcf().get_axes()) == 10

        
    def test_python_ex6(cls):
        '''Test the calc_group_averages function'''

        # Check that the function has a doc-string
        assert handin6.calc_group_averages.__doc__ !=  None
        assert len(handin6.calc_group_averages.__doc__) > 0

        # Call function
        group_averages = handin6.calc_group_averages(TestPythonPart.grouped_images)

        # Check dimensions
        assert len(group_averages) == 10
        for group in group_averages:
            assert len(group.shape) == 3
            assert group.shape[0] == 1
            assert group.shape[1] == 28
            assert group.shape[2] == 28
        
        # Check that we can call draw_image_row
        handin6.draw_image_row(group_averages)


        
        
    
