class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_digits = 0

            while num > 0:
                digit = num % 10
                sum_digits += digit
                num //= 10

            num = sum_digits

        return num
