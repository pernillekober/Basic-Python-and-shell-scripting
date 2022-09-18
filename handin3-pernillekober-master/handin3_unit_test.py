import glob
import os
import sys
import pytest

import handin3


class TestUnixPart:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""

        # Import pywrapper (complication due to dot in directory name)
        import importlib
        pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
        pexpect = pytest.importorskip("pexpect")
        spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
        cls.sh_pywrapper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.sh_pywrapper)

        cls.process = cls.sh_pywrapper.create_process()
        cls.commands_list = cls.sh_pywrapper.parse('handin3.sh')
        cls.base_dir = os.path.abspath(cls.sh_pywrapper.get_cwd(cls.process)).strip()

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""

        pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
        pexpect = pytest.importorskip("pexpect")
        cls.sh_pywrapper.kill_process(cls.process)

    def test_ex1(cls):
        '''Test whether handin3 directory exists'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[0])
        assert(os.path.exists(os.path.join(cls.base_dir, "handin3")))
        assert(os.path.isdir(os.path.join(cls.base_dir, "handin3")))

    def test_ex2(cls):
        '''Test whether handin3/test1 directory exists'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[1])
        assert(os.path.exists(os.path.join(cls.base_dir, "handin3/test1")))
        assert(os.path.isdir(os.path.join(cls.base_dir, "handin3/test1")))
        # full_dir_name = cls.sh_pywrapper.get_cwd(cls.process)
        # base_name = os.path.basename(full_dir_name)
        # assert(base_name == 'handin3')

    def test_ex3(cls):
        '''Test whether m_scrambled has been correctly downloaded'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[2])
        assert(os.path.exists(os.path.join(cls.base_dir, "handin3/test1/m_scrambled.txt")))

    def test_ex4(cls):
        '''Test whether test1 was correctly copied into test2'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[3])
        dir1 = os.path.join(cls.base_dir, 'handin3/test1/')
        dir2 = os.path.join(cls.base_dir, 'handin3/test2/')
        assert(os.path.exists(dir2))
        assert(os.path.isdir(dir2))
        content_test1 = [os.path.relpath(f, dir1) for f in glob.glob(dir1+'**')]
        content_test2 = [os.path.relpath(f, dir2) for f in glob.glob(dir2+'**')]
        assert(content_test1 == content_test2)

    def test_ex5(cls):
        '''Test whether find command was executed correctly'''
        output = "".join(cls.sh_pywrapper.run(cls.process, cls.commands_list[4]))
        output = [f.strip() for f in output.split('\n') if f is not '']
        assert(output == ['.', './test1', './test1/m_scrambled.txt', './test2', './test2/m_scrambled.txt'])

    def test_ex6(cls):
        '''Test that the test2 directory was correctly removed'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[5])
        assert(not os.path.exists(os.path.join(cls.base_dir, "handin3/test2")))

    def test_ex7(cls):
        '''Test the cat command'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[6])
        # No assertion done here - correct output is checked at the end

    def test_ex8(cls):
        '''Check unscrambled image against correct one'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[7])

        assert(os.path.exists(os.path.join(cls.base_dir, "handin3/test1/m.txt")))
        output_filename = os.path.join(cls.base_dir, "handin3/test1/m.txt")
        output_file = open(output_filename)
        output = output_file.readlines()

        # Check that output has correct length
        newlines = len(output) == 150

        # Check that lines are unscrambled - i.e., in correct order (this is a hint! :)
        sh_outputs = cls.sh_pywrapper.run(cls.process, ["sort -nc " + output_filename])
        condition1 = (len(sh_outputs) == 1 and sh_outputs[0] == "")

        # Remove all whitespace and calculate checksum (for cases where first column was removed)
        import re
        import hashlib
        condition2 = (hashlib.md5(re.sub(r'\s+', '', ''.join(output)).encode('utf-8')).hexdigest() == "b89f40f9ca67d797c0808eee77a6820c")

        # Check that either condition is fulfilled
        assert condition1 or condition2

    def test_ex9(cls):
        '''Check one-liner'''

        # First remove the old version
        os.remove(os.path.join(cls.base_dir, "handin3/test1/m.txt"))

        # Verify that command is a one-liner
        effective_command_lines = [command for command in cls.commands_list[8] if command[0] != '#']
        assert(len(effective_command_lines) == 1)

        # Run command
        cls.sh_pywrapper.run(cls.process, cls.commands_list[8])

        output_filename = os.path.join(cls.base_dir, "handin3/test1/m.txt")
        output_file = open(output_filename)
        output = output_file.readlines()

        # Check that lines are unscrambled - i.e., in correct order (this is a hint! :)
        sh_outputs = cls.sh_pywrapper.run(cls.process, ["sort -nc " + output_filename])
        condition1 = (len(sh_outputs) == 1 and sh_outputs[0] == "")

        # Remove all whitespace and calculate checksum (for cases where first column was removed)
        import re
        import hashlib
        condition2 = (hashlib.md5(re.sub(r'\s+', '', ''.join(output)).encode('utf-8')).hexdigest() == "b89f40f9ca67d797c0808eee77a6820c")

        # Check that either condition is fulfilled
        assert condition1 or condition2

    def test_ex10(cls):
        '''Check cleanup'''
        cls.sh_pywrapper.run(cls.process, cls.commands_list[9])
        assert(not os.path.exists(os.path.join(cls.base_dir, "handin3")))
        

class TestPythonPart:

    def test_python_ex1(cls):
        '''Check for unscramble_attempt1 function'''

        # Check that the function has a doc-string
        assert handin3.unscramble_attempt1.__doc__ !=  None

        scrambled_file = open("m_scrambled.txt")
        scrambled_lines = scrambled_file.readlines()
        unscrambled_lines = handin3.unscramble_attempt1(scrambled_lines)
        scrambled_file.close()


    def test_python_ex2(cls):
        '''Check for unscramble_attempt2 function'''

        # Check that the function has a doc-string
        assert handin3.unscramble_attempt2.__doc__ !=  None
        
        scrambled_file = open("m_scrambled.txt")
        scrambled_lines = scrambled_file.readlines()
        unscrambled_lines = handin3.unscramble_attempt2(scrambled_lines)
        scrambled_file.close()
        
        unscrambled_reference = sorted(scrambled_lines, key=lambda line: int(line.split(" ")[0]))

        assert(unscrambled_lines == unscrambled_reference)
        
        


    
