
class insert_bit(object):
    def solution1(self, n, m, i, j):
        allOne = ~0

        left = allOne << (j + 1)
        right = (allOne << i) - 1

        mask = left | right

        cleanup = mask & n
        temp = m << i

        return cleanup | temp


if __name__ == '__main__':
    bit = insert_bit()
