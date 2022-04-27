from unittest import TestCase
import pathlib
from src.model.parameter import Parameter
from src.common.exceptions.parameter_exception import ParameterException


class TestParameter(TestCase):
    #def setUp(self):
    #    self.test_folder = pathlib.Path(__file__).parent.parent.absolute()
    #    self.java_file = pathlib.Path.joinpath(self.test_folder, 'resource/test.java')
    #    self.java_file_invalid = pathlib.Path.joinpath(self.test_folder, 'resource/invalid.java')
    #    self.invalid_folder = 'd:/at16invalidFolder'

    @classmethod
    def setUpClass(cls):
        cls.test_folder = pathlib.Path(__file__).parent.parent.absolute()
        cls.java_file = pathlib.Path.joinpath(cls.test_folder, 'resource/test.java')
        cls.java_file_invalid = pathlib.Path.joinpath(cls.test_folder, 'resource/invalid.java')
        cls.invalid_folder = 'd:/at16invalidFolder'

    def test_validate(self):
        param = Parameter(self.java_file, self.test_folder, self.test_folder)
        param.validate()

    def test_empty_java_file_path(self):
        with self.assertRaises(ParameterException):
            param = Parameter('', self.test_folder, self.test_folder)
            param.validate()

    def test_invalid_java_file(self):
        with self.assertRaises(ParameterException):
            param = Parameter(self.java_file_invalid, self.test_folder, self.test_folder)
            param.validate()

    def test_empty_java_folder_path(self):
        with self.assertRaises(ParameterException):
            param = Parameter(self.java_file, '', self.test_folder)
            param.validate()

    def test_invalid_java_folder_path(self):
        with self.assertRaises(ParameterException):
            param = Parameter(self.java_file, self.invalid_folder, self.test_folder)
            param.validate()
