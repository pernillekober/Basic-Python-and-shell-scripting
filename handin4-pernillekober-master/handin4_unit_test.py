import glob
import os
import sys
import pytest

import handin4
import handin4_test


@pytest.mark.skipif(sys.platform == "win32", reason="Tests cannot be executed on windows")
class TestUnixPart:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""

        pexpect = pytest.importorskip("pexpect")
        # Import pywrapper (complication due to dot in directory name)
        import importlib
        spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
        cls.sh_pywrapper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.sh_pywrapper)

        cls.process = cls.sh_pywrapper.create_process()
        cls.commands_list = cls.sh_pywrapper.parse('handin4.sh')
        cls.base_dir = os.path.abspath(cls.sh_pywrapper.get_cwd(cls.process)).strip()

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""

        pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
        pexpect = pytest.importorskip("pexpect")
        cls.sh_pywrapper.kill_process(cls.process)

    def test_ex1(cls):
        '''Test for existence of files'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[0])[-1].strip()
        assert os.path.exists("british-english")
        assert os.path.exists("british-english-subset")

    def test_ex2(cls):
        '''Test for identification of omitted letters'''
        output = [line.strip() for line in cls.sh_pywrapper.run(cls.process, cls.commands_list[1])[-1].strip().split('\n')]
        expected_output = ['X','Y','Z'] 
        assert output == expected_output

    def test_ex3(cls):
        '''Test that subset file was correctly reproduced'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[2])[-1].strip()

        # Check the subset2 file exists
        assert os.path.exists("british-english-subset2")

        # Read contents of original subset file
        subset1_file = open("british-english-subset")
        subset1 = subset1_file.read()
        subset1_file.close()

        # Read contents of new subset file
        subset2_file = open("british-english-subset2")
        subset2 = subset2_file.read()
        subset2_file.close()

        # Compare new subset file to original
        assert subset1 == subset2
        
        

class TestPythonPart:

    def test_python_ex1(cls):
        '''Test read_fasta function'''

        # Check that the function has a doc-string
        assert handin4.read_fasta.__doc__ !=  None

        global data
        data = handin4.read_fasta('Ecoli.prot.fasta')

        # Check that function returns something
        assert data is not None

        # Check that it has keys
        assert len(data.keys()) > 0

        # Check that keys do not contain '>' character
        for key in data.keys():
            assert key[0] != '>'


    def test_python_ex2(cls):
        '''Test the test of the read_data function'''
        # Check that variable exists
        assert hasattr(handin4_test, 'fasta_dict')

        # Check for number of keys in dictionary
        assert len(handin4_test.fasta_dict.keys()) == 4183


    def test_python_ex3(cls):
        '''Test find_prot function'''

        # Check that the function has a doc-string
        assert handin4.find_prot.__doc__ !=  None

        # Test that function returns something
        assert handin4.find_prot(data, 'YHCN_ECOLI') is not None


    def test_python_ex4(cls):
        '''Test the test of the find_prot function'''    

        # Check that variable exists
        assert hasattr(handin4_test, 'yhcn')

        # Check that test program produces same result as calling
        # function directly
        assert handin4_test.yhcn == handin4.find_prot(data, 'YHCN_ECOLI')


    def test_python_ex5(cls):
        '''Test the test of the find_prot function'''    

        # Check that variable exists
        assert hasattr(handin4_test, 'boom')

        # Check that the boom variable is None as expected
        assert handin4_test.boom is None


    def test_python_ex6(cls):
        '''Test find_prot2 function'''

        # Check that the function has a doc-string
        assert handin4.find_prot2.__doc__ !=  None

        # Test that function returns all keys when given appropriate regexp
        assert len(handin4.find_prot2(data, '.*')) == len(data)


    def test_python_ex7(cls):
        '''Test the test of the find_prot2 function'''

        # Check that variable exists
        assert hasattr(handin4_test, 'matches')

        # Check that matches is a list
        assert isinstance(handin4_test.matches, list)

        # Test number of matches
        assert len(handin4_test.matches) == 233
    
        
        


    
