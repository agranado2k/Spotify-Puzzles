#!/usr/bin/env ruby
# encoding: utf-8
gem 'minitest', '>= 5.0.0'
require 'minitest/autorun'
require_relative 'reversed_binary_numbers'


# Reversed Binary Numbers (Difficulty Level: Easy)
# ProblemID: Reversebinary

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

class ReversedBinaryNumbersTest < Minitest::Test

  def test_convert_decimal_to_binary_number
    input = 13
    output = 1101
    assert_equal output, ReversedBinaryNumbers.convert_decimal_to_binary(input)
  end

  def test_reverse_binary_number_exemplto_1
    input = 1101
    output = 1011
    assert_equal output, ReversedBinaryNumbers.reverse_binary(input)
  end

  def test_reverse_binary_number_exemplto_2
    input = 1011
    output = 1101
    assert_equal output, ReversedBinaryNumbers.reverse_binary(input)
  end

  def test_convert_binary_to_decimal_number_example_1
    input = 1101
    output = 13
    assert_equal output, ReversedBinaryNumbers.convert_binary_to_decimal(input)
  end

  def test_convert_binary_to_decimal_number_example_2
    input = 1011
    output = 11
    assert_equal output, ReversedBinaryNumbers.convert_binary_to_decimal(input)
  end

  def test_reverse_binary_number_exemplo_1
    input = 13
    output = 11
    assert_equal output, ReversedBinaryNumbers.reverse(input)
  end

  def test_reverse_binary_number_exemplo_2
    input = 47
    output = 61
    assert_equal output, ReversedBinaryNumbers.reverse(input)
  end

end