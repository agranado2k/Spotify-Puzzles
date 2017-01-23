# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

from reversed_binary_numbers import ReversedBinaryNumbers

# Reversed Binary Numbers (Difficulty Level: Easy)
# Yi has moved to Sweden and now goes to school here. The first years of schooling she got in China, and the curricula do not match completely in the two countries. 
# Yi likes mathematics, but now… The teacher explains the algorithm for subtraction on the board, and Yi is bored. 
# Maybe it is possible to perform the same calculations on the numbers corresponding to the reversed binary representations of the numbers on the board?
# Yi dreams away and starts constructing a program that reverses the binary representation, in her mind. As soon as the lecture ends, she will go home and write it on her computer.


# Task
# Your task will be to write a program for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

# Input
# The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

# Output
# Output one line with one integer, the number we get by reversing the binary representation of N.

# Sample input 1
# 13
# Sample output 1
# 11
# Sample input 2
# 47
# Sample output 2
# 61

class ReversedBinaryNumbersTests(unittest.TestCase):

  def test_convert_decimal_to_binary_number(self):
    input = 13
    output = 1101
    self.assertEqual(
        output,
        ReversedBinaryNumbers.convert_decimal_to_binary(input)
    )

  def test_reverse_binary_number_exemplto_1(self):
    input = 1101
    output = 1011
    self.assertEqual(
        output,
        ReversedBinaryNumbers.reverse_binary(input)
    )

  def test_reverse_binary_number_exemplto_2(self):
    input = 1011
    output = 1101
    self.assertEqual(
        output,
        ReversedBinaryNumbers.reverse_binary(input)
    )

  def test_convert_binary_to_decimal_number_example_1(self):
    input = 1101
    output = 13
    self.assertEqual(
        output,
        ReversedBinaryNumbers.convert_binary_to_decimal(input)
    )

  def test_convert_binary_to_decimal_number_example_2(self):
    input = 1011
    output = 11
    self.assertEqual(
        output,
        ReversedBinaryNumbers.convert_binary_to_decimal(input)
    )

  def test_reverse_binary_number_exemplo_1(self):
    input = 13
    output = 11
    self.assertEqual(
        output,
        ReversedBinaryNumbers.reverse(input)
    )

  def test_reverse_binary_number_exemplo_2(self):
    input = 47
    output = 61
    self.assertEqual(
        output,
        ReversedBinaryNumbers.reverse(input)
    )


if __name__ == '__main__':
    unittest.main()
