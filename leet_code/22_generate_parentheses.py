# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class GenerateParentheses(object):
    def solution1(self, num):
        '''
        
        :param num: 
        :return: 
        '''
        result = set()
        if num < 1:
            return list(result)
        left, right = num, num
        self.recursive(left, right, '', result)
        result = list(result)
        return result

    def recursive(self, right, left, content, result):
        if left > 0:
            content += '('
            left -= 1
            self.recursive(right, left, content, result)
            content = content[0:len(content) - 1]
            left += 1
        if right > 0 and right > left:
            content += ')'
            right -= 1
            self.recursive(right, left, content, result)
        if right == 0 and left == 0:
            result.add(content)




if __name__ == '__main__':
    result = GenerateParentheses().solution1(3)
    print result
