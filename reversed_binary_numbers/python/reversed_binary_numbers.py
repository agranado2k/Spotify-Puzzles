#!/usr/local/bin/python

class ReversedBinaryNumbers:
  @staticmethod
  def convert_decimal_to_binary(decimal):
    return int(bin(decimal)[2:])

  @staticmethod
  def reverse_binary(binary):
    return int(str(binary)[::-1])

  @staticmethod
  def convert_binary_to_decimal(binary):
    return int(str(binary), 2)

  @staticmethod
  def reverse(decimal):
    return ReversedBinaryNumbers.convert_binary_to_decimal(ReversedBinaryNumbers.reverse_binary(ReversedBinaryNumbers.convert_decimal_to_binary(decimal)))

def main():
  number = input()
  print(ReversedBinaryNumbers.reverse(number))

main()