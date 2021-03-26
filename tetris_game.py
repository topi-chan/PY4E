import random

class Tetris:
    '''A simple game.'''

    def __init__(self):
        self.i_shape = [[1,1,1,1]]
        self.l_shape = [[1],[1],[1,1]]
        self.j_shape = [[0,1],[0,1],[1,1]]
        self.s_shape = [[0,1], [1,1], [1,0]]
        self.o_shape = [[1,1], [1,1]]
        self.boards=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
        self.boards.append([1].copy()*22)

    def board_screen(self):
        shape = random.choice([self.i_shape, self.l_shape, self.j_shape,
                self.s_shape, self.o_shape])
        position = random.randint(0,20)
        num_of_ones = sum(num.count(1) for num in self.boards)
        m = 0
        for i in range(len(shape)):
            sub_shape = shape[m]
            n = 0
            pos = position
            for i in range(len(sub_shape)):
                if sub_shape[n] == 1 and pos<=21:
                    self.boards[m][pos] = 1
                pos+=1
                n+=1
            m+=1
        print(num_of_ones)
        if num_of_ones+4 != (sum(num.count(1) for num in self.boards)):
          return board_screen()
        else:
            for board in self.boards:
                print(*["*" if elem==1 else " " for elem in board], sep='')




tetr=Tetris()
tetr.board_screen()
# n=0
# l = 0
# for i in range(len(i_shape)):
#     boards[n][position:len(i_shape)] = i_shape[l]
#     l = l+1
# for p in boards: print (p)

#print(len(boards))
#boards[0][7].insert(1, i_shape[0])
#print(i_shape[0])
#
# for board in boards:
#     print(*["*" if elem==1 else " " for elem in board], sep='')
#
# print(s_shape[1])

# print(*["*" if elem==1 else " " for elem in board], sep='')
#
# i_shape = [1,1,1,1]
# l_shape = [1],[1],[1,1]
# j_shape = [0,1],[0,1],[1,1]
# s_shape = [0,1], [1,1], [1]
# o_shape = [1,1], [1,1]
#
# boards = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
#         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],]
# for board in boards:
#     print(*["*" if elem==1 else " " for elem in board], sep='')
