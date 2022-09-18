import sys
import re
import pytest
import os

import handin5

class TestPythonPart:

    def test_python_ex1(cls):
        '''Test wordfile_to_list function'''

        # Check that the function has a doc-string
        assert handin5.wordfile_to_list.__doc__ !=  None
        assert len(handin5.wordfile_to_list.__doc__) > 0

        word_list = handin5.wordfile_to_list('british-english')

        # Check for expected length of word file
        assert len(word_list) == 101825

        # Check that newlines have been removed
        for word in word_list:
            assert not word[-1].isspace()


    def test_python_ex2(cls):
        '''Test wordfile_differences_linear_search function'''

        # Check that the function has a doc-string
        assert handin5.wordfile_differences_linear_search.__doc__ !=  None
        assert len(handin5.wordfile_differences_linear_search.__doc__) > 0

        differences = handin5.wordfile_differences_linear_search('british-english-test', 'american-english-test')

        # Check for expected length of word file
        assert len(differences) == 1


    def test_python_ex3(cls):
        '''Test the handin5_test1 module'''

        # import test file
        import handin5_test1

        # Check for expected number of differences
        assert len(handin5_test1.differences) == 5357    

        # Check that it took at least a minute
        assert handin5_test1.time_spent > 30


    def test_python_ex4(cls):
        '''Test wordfile_differences_binary_search function'''

        # Check that the function has a doc-string
        assert handin5.wordfile_differences_binary_search.__doc__ !=  None
        assert len(handin5.wordfile_differences_binary_search.__doc__) > 0

        differences = handin5.wordfile_differences_binary_search('british-english-test', 'american-english-test')

        # Check for expected length of word file
        assert len(differences) == 1


    def test_python_ex5(cls):
        '''Test the handin5_test2 module'''

        # import test file
        import handin5_test2

        # Check for expected number of differences
        assert len(handin5_test2.differences) == 5357    

        # Check that it took at least a minute
        assert handin5_test2.time_spent < 30


    def test_python_ex6(cls):
        '''Test the wordfile_to_dict function'''

        # Check that the function has a doc-string
        assert handin5.wordfile_to_dict.__doc__ !=  None
        assert len(handin5.wordfile_to_dict.__doc__) > 0

        word_dict = handin5.wordfile_to_dict('british-english')

        # Check for expected length of word file
        assert len(word_dict) == 101825

        # Check that newlines have been removed
        for word in word_dict.keys():
            assert not word[-1].isspace()


    def test_python_ex7(cls):
        '''Test the wordfile_differences_dict_search function'''

        # Check that the function has a doc-string
        assert handin5.wordfile_differences_dict_search.__doc__ !=  None
        assert len(handin5.wordfile_differences_dict_search.__doc__) > 0

        differences = handin5.wordfile_differences_dict_search('british-english-test', 'american-english-test')

        # Check for expected length of word file
        assert len(differences) == 1


    def test_python_ex8(cls):
        '''Test the handin5_test3 module'''

        # import test file
        import handin5_test3

        # Check for expected number of differences
        assert len(handin5_test3.differences) == 5357    

        # Check that it took at least a minute
        assert handin5_test3.time_spent < 30


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
        cls.commands_list = cls.sh_pywrapper.parse('handin5.sh')
        cls.base_dir = os.path.abspath(cls.sh_pywrapper.get_cwd(cls.process)).strip()

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""

        pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
        pexpect = pytest.importorskip("pexpect")
        cls.sh_pywrapper.kill_process(cls.process)

    def test_unix_ex1(cls):
        '''Test for output of time command for handin5_test1'''
        lines = cls.sh_pywrapper.run(cls.process, cls.commands_list[0])[-1].strip().split('\n')
        for line in lines[-3:]:
            split_line = line.split()

            # Check that first column contains "real", "user", or "sys" values
            assert split_line[0] in ["real", "user", "sys"]

            if split_line[0] == "real":
                # Extract minute and second information and check values
                match = re.search('([0-9.]+)m([0-9.]+)s', split_line[1])
                assert match is not None
                minutes = float(match.group(1))
                seconds = float(match.group(2))
                assert minutes > 0 or seconds > 30

    def test_unix_ex2(cls):
        '''Test for output of time command for handin5_test2'''
        lines = cls.sh_pywrapper.run(cls.process, cls.commands_list[1])[-1].strip().split('\n')
        for line in lines[-3:]:
            split_line = line.split()

            # Check that first column contains "real", "user", or "sys" values
            assert split_line[0] in ["real", "user", "sys"]

            if split_line[0] == "real":
                # Extract minute and second information and check values
                match = re.search('([0-9.]+)m([0-9.]+)s', split_line[1])
                assert match is not None
                minutes = float(match.group(1))
                seconds = float(match.group(2))
                assert minutes == 0 and seconds < 30

    def test_unix_ex3(cls):
        '''Test for output of time command for handin5_test3'''
        lines = cls.sh_pywrapper.run(cls.process, cls.commands_list[2])[-1].strip().split('\n')
        for line in lines[-3:]:
            split_line = line.split()

            # Check that first column contains "real", "user", or "sys" values
            assert split_line[0] in ["real", "user", "sys"]

            if split_line[0] == "real":
                # Extract minute and second information and check values
                match = re.search('([0-9.]+)m([0-9.]+)s', split_line[1])
                assert match is not None
                minutes = float(match.group(1))
                seconds = float(match.group(2))
                assert minutes == 0 and seconds < 30
        
    def test_unix_ex4(cls):
        '''Test for output of time command for handin5_test3'''
        lines = cls.sh_pywrapper.run(cls.process, cls.commands_list[3])[-1].strip().split('\n')

        # Check that command outputs correct value
        output = lines[-1]
        assert int(output) == 5357


    def test_unix_ex5(cls):
        '''Test for output of time command for handin5_test3'''
        lines = cls.sh_pywrapper.run(cls.process, cls.commands_list[4])[-1].strip().split('\n')
        for line in lines[-3:]:
            split_line = line.split()

            # Check that first column contains "real", "user", or "sys" values
            assert split_line[0] in ["real", "user", "sys"]

            if split_line[0] == "real":
                match = re.search('([0-9.]+)m([0-9.]+)s', split_line[1])
                assert match is not None
                minutes = float(match.group(1))
                seconds = float(match.group(2))
                assert minutes == 0 and seconds < 30
        
    
