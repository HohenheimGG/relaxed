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
        self.recursive1(left, right, '', result)
        result = list(result)
        return result

    def recursive1(self, right, left, content, result):
        if left > 0:
            content += '('
            self.recursive1(right, left - 1, content, result)
            content = content[0:len(content) - 1]
        if right > 0 and right > left:
            content += ')'
            right -= 1
            self.recursive1(right, left, content, result)
        if right == 0 and left == 0:
            result.add(content)

    def solution2(self, num):
        result = []
        if num < 1:
            return result
        left, right = num, num
        self.recursive2(left, right, '', result)
        return result

    def recursive2(self, left, right, content, result):
        if left == 0 and right == 0:
            result.append(content)
            return
        if left > 0:
            content += '('
            self.recursive2(left - 1, right, content, result)
            content = content[:len(content) - 1]
        if right > left:
            content += ')'
            self.recursive2(left, right - 1, content, result)

if __name__ == '__main__':
    result = GenerateParentheses().solution1(3)
    print result
