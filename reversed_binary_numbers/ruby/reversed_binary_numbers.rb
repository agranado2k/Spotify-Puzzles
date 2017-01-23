class ReversedBinaryNumbers
  def self.reverse(decimal)
    convert_binary_to_decimal(reverse_binary(convert_decimal_to_binary(decimal)))
  end

  def self.convert_decimal_to_binary(decimal)
    decimal.to_s(2).to_i
  end

  def self.convert_binary_to_decimal(binary)
    binary.to_s.to_i(base=2)
  end

  def self.reverse_binary(binary_number)
    binary_number.to_s.reverse.to_i
  end
end