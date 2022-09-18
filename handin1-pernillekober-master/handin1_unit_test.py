import os

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()
    module.python_line_block_list = sh_pywrapper.parse('handin1.py')
    module.base_dir = os.path.abspath(sh_pywrapper.get_cwd(process)).strip()
    
def teardown_module(module):
    """Make sure process is dead"""
    sh_pywrapper.kill_process(module.process)
    
def test_python_ex1():
    '''Test reading of content into list'''
    sh_pywrapper.exec_python(python_line_block_list[0])
    # Check for book_file variable name
    assert('lines' in vars(sh_pywrapper))
    # Check that book_file is of type list
    assert(isinstance(sh_pywrapper.lines, list))

def test_python_ex2():
    '''Test counting lines'''
    output = sh_pywrapper.exec_python(python_line_block_list[1])[1].strip()
    correct_length = "3736"
    assert(output == correct_length)

def test_python_ex3():
    '''Test printing of 41st line'''
    output = sh_pywrapper.exec_python(python_line_block_list[2])[1].strip()
    correct_line = "CHAPTER I. Down the Rabbit-Hole"
    assert(output == correct_line)

def test_python_ex4():
    '''Test counting words in of 43rd line'''
    output = sh_pywrapper.exec_python(python_line_block_list[3])[1].strip()
    correct_count = "14"
    assert(correct_count == output)
    
def test_python_ex5():
    '''Test for correct lines in junk output file'''
    sh_pywrapper.exec_python(python_line_block_list[4])
    assert(os.path.exists("junk.txt"))
    with open("junk.txt") as junk_file:
        junk_content = junk_file.readlines()
    assert(junk_content == ["Title: Alice's Adventures in Wonderland\n", "\n", "Author: Lewis Carroll\n"])
