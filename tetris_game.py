import random

class Tetris:
    '''A simple game.'''

    def __init__(self):
        self.i_shape = [[1,1,1,1]]
        self.l_shape = [[1],[1],[1,1]]
        self.j_shape = [[0,1],[0,1],[1,1]]
        self.s_shape = [[0,1], [1,1], [1,0]]
        self.o_shape = [[1,1], [1,1]]
        self.current_shape = None
        self.board_line = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
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
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.prev_boards = []
        self.current_boards = []
        self.new_boards = []
        self.fixed_boards = []
        self.current_pos = []
        self.pos_dict = {}
        self.new_pos = []

    def board_screen(self):
        num_of_ones = sum(num.count(1) for num in self.boards)
        board_func=self.boards
        while True:
            shape = random.choice([self.i_shape, self.l_shape, self.j_shape,
                    self.s_shape, self.o_shape])
            position = random.randint(1,20)
            m = 0
            for i in range(len(shape)):
                sub_shape = shape[m]
                n = 0
                pos = position
                for i in range(len(sub_shape)):
                    if sub_shape[n] == 1 and pos<=21: board_func[m][pos] = 1
                    pos+=1
                    n+=1
                m+=1
            if (num_of_ones+4) == (sum(num.count(1) for num in board_func)):
                break
            else:
                board_func=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
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
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.boards=board_func
        self.current_shape=shape
        for board in self.boards:
            print(*["*" if elem==1 else " " for elem in board], sep='')
            self.current_pos.append([i for i, x in enumerate(board) if x == 1])
        for pos in self.current_pos:
            pos.remove(0)
            pos.remove(21)
        for i,pos in enumerate(self.current_pos[:-1]):
            if len(pos)>0:
                self.pos_dict[i] = pos

    def first_move(self):
        self.new_boards = self.boards[:-1]
        while True:
            move = input()
            if move == "d":
                for board in self.new_boards:
                    print(*["*" if elem==1 else " " for elem in board], sep='')
                print("**********////////////*********")
                for i, board in enumerate (self.boards[:-1]):
                    if board.count(1) > 2:
                        self.new_boards[i+1] = self.boards[i]
                for i, board in enumerate (self.new_boards):
                    if board.count(1) > 2:
                        self.new_boards[i] = self.board_line
                        break
                print(self.pos_dict)
                for k in self.pos_dict.keys():
                    single_list = self.new_boards[k]
                    for item in self.pos_dict.get(k):
                        self.new_boards[k][item]=0
                        print(k, item)
                for k in self.pos_dict.keys():
                    single_list = self.new_boards[k]
                    for item in self.pos_dict.get(k):
                        self.new_boards[k+1][item+1]=1
                        print(k, item)



                    # self.new_boards[k][v]=0
                    # self.new_boards[k][v+1]=1

                # for i, board in self.new_boards:
                #     if board.count(1) > 2:
                #         for i, num in enumerate (board):
                #             if num==1 and i !=0 and i != 21:
                #                 board[i]=0
                #                 board[i+1]=1
                #                 print(board)

                    # for i, b in enumerate (board):
                    #     if board[i] != 0 and board[i] != 21:
                    #         board[i] == 0
                    #         board[i+1] ==1
                self.new_boards.append([1].copy()*22)
                for board in self.new_boards:
                    print(*["*" if elem==1 else " " for elem in board], sep='')
                continue




            elif move == "s":
                for board in self.boards:
                    print(*["*" if elem==1 else " " for elem in board], sep='')
                continue
            elif move == "a":
                for board in self.boards:
                    print(*["*" if elem==1 else " " for elem in board], sep='')
                continue
            elif move =="w":
                for board in self.boards:
                    print(*["*" if elem==1 else " " for elem in board], sep='')
                continue
            elif move == "q":
                quit()
            else:
                for board in self.boards:
                    print(*["*" if elem==1 else " " for elem in board], sep='')
                continue

tetr=Tetris()
tetr.board_screen()
tetr.first_move()





                # m = 0
                # for i in range(len(self.current_shape)):
                #     sub_shape = self.current_shape[m]
                #     n = 0
                #     pos = position
                #     for i in range(len(sub_shape)):
                #         if sub_shape[n] == 1 and pos<=21:
                #             self.boards[m+1][pos] = 1
                #         pos+=1
                #         n+=1
                #     m+=1



                    # for i, item in enumerate (board):
                    #     if i != 0 and i != 21 and item == 1:
                    #         self.current_boards.append(i)



                # print(self.current_pos)
                # for pos in self.current_pos[:-1]:
                #     for p in pos:
                #         if p !=0 and p !=21:
                #             p+=1
                #             self.new_pos.append(p)
                #
                # print(self.new_pos)
#                print(self.current_pos)
                # for board in self.boards:
                #     for b in board:
                #         print(b)
                #         if b != 0 and b != 21:
                #             b += 1
