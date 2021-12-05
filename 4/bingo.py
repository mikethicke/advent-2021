import sys

class Board:
    def __init__( self, board_arr ) :
        new_board_list = []
        for line in board_arr :
            num_str = ''
            skip = False
            for i in range( len( line ) ) :
                if skip :
                    skip = False
                else :
                    num_str += line[i]
                if len( num_str ) == 2 :
                    new_board_list.append( int( num_str ) )
                    num_str = ''
                    skip = True
        self.the_board = new_board_list
        self.marked = []
        self.last_called = 0
    
    def is_bingo( self, called_numbers ) :
        '''
        0  1  2  3  4
        5  6  7  8  9
        10 11 12 13 14
        15 16 17 18 19
        20 21 22 23 24
        '''
        bingos = [
            [  0,  1,  2,  3 , 4 ],
            [  5,  6,  7,  8,  9 ],
            [ 10, 11, 12, 13, 14 ],
            [ 15, 16, 17, 18, 19 ],
            [ 20, 21, 22, 23, 24 ],
            [  0,  5, 10, 15, 20 ],
            [  1,  6, 11, 16, 21 ],
            [  2,  7, 12, 17, 22 ],
            [  3,  8, 13, 18, 23 ],
            [  4,  9, 14, 19, 24 ]
        ]
        
        self.marked = []
        for called in called_numbers :
            self.last_called = called
            try :
                index = self.the_board.index( called )
                self.marked.append( index )
            except ValueError :
                pass
        
        for bingo in bingos :
            intersection = list ( set( self.marked ) & set( bingo ) )
            if len( intersection ) == 5 :
                return True
        
        return False
    
    def total_board( self ) :
        sum_marked = 0
        for marked_num in self.marked :
            sum_marked += self.the_board[ marked_num ]
        sum_unmarked = sum( self.the_board ) - sum_marked
        return sum_unmarked * self.last_called

def parse_data_file( file_name ) :
    with open( file_name, 'r' ) as file :
        data = file.read().splitlines()
    
    called_numbers = data[0].split(',')
    called_numbers = list( map( int, called_numbers ) )

    boards = []
    line_buffer = []
    for line in data[2:] :
        if len( line ) < 5 :
            boards.append( Board( line_buffer ) )
            line_buffer = []
        else :
            line_buffer.append( line )
    
    return ( called_numbers, boards )

def play_bingo( called_numbers, boards ) :
    for i in range( len( called_numbers ) - 1) :
        for board in boards :
            if board.is_bingo( called_numbers[:i + 1 ] ) :
                return board.total_board()

def play_losing_bingo( called_numbers, boards ) :
    bingo_boards = []
    for i in range( len( called_numbers ) - 1) :
        for j in range( len( boards ) ) :
            if j in bingo_boards :
                continue
            if boards[j].is_bingo( called_numbers[:i + 1 ] ) :
                bingo_boards.append(j)
                if len( bingo_boards ) == len( boards ) :
                    return boards[j].total_board()


if __name__ == '__main__' :
    if ( len( sys.argv ) == 0 ) :
        exit
    ( called_numbers, boards ) = parse_data_file( sys.argv[1] )
    total = play_bingo( called_numbers, boards )
    print( f"Total: {total}" )
    losing_total = play_losing_bingo( called_numbers, boards )
    print( f"Losing total: {losing_total}")





