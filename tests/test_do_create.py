#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state(self, mock_stdout):
        self.console.onecmd('create State name="California"')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)  # Ensure it returns the object id

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place(self, mock_stdout):
        self.console.onecmd('create Place name="My_little_house" city_id="0001" user_id="0001" number_rooms=4')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)  # Ensure it returns the object id

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        self.console.onecmd('create InvalidClass name="Test"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_param(self, mock_stdout):
        self.console.onecmd('create State invalid_param=foo')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)  # Ensure no crash for invalid parameter
