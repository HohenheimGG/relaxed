#!/usr/bin/python
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output "Fizz" instead of the number
# and for the multiples of five output "Buzz".
# For numbers which are multiples of both three and five output "FizzBuzz".
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
#
class Solution(object):


    def printFizzBuzz(self):
        num = int(raw_input("need num"));
        self.fizzBuzz2(num);

    def fizzBuzz(self, n):
        """
        :param n: 
        :return: List[str]
        """
        if(n <= 0):
            print "error";
            return [];
        list = [];
        fizzNum = 1;
        buzzNum = 1;
        for num in range(1, n + 1):
            if(fizzNum % 5 == 0 and buzzNum % 3 == 0 and (num % 3 == 0 or num % 5 == 0)):
                list.append("FizzBuzz");
                fizzNum = 1;
                buzzNum = 1;
            elif(num % 3 == 0):
                list.append("Fizz")
                fizzNum += 1;
            elif(num % 5 == 0):
                list.append("Buzz")
                buzzNum += 1;
            else:
                num = str(num);
                list.append(num);

        print(list)
        return list;

    def fizzBuzz2(self, n):
        """
        :param n: 
        :return: 
        """
        if(n <= 0):
            return [];
        list = [];
        fizzNum = 0;
        buzzNum = 0;
        for num in range(1, n + 1):
            fizzNum += 1;
            buzzNum += 1;
            if(fizzNum == 3 and buzzNum == 5):
                list.append("FizzBuzz")
                fizzNum = 0
                buzzNum = 0
            elif(fizzNum == 3):
                list.append("Fizz")
                fizzNum = 0
            elif(buzzNum == 5):
                list.append("Buzz")
                buzzNum = 0
            else:
                list.append(num)
        print list;
        return list;

def main():
    solution = Solution();
    solution.printFizzBuzz();

if __name__ == "__main__":
    main()