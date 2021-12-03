import sys

def parse_data_file( file_name ) :
    with open( file_name, 'r' ) as file :
        data = file.read().splitlines()
    return data

def move( data ) :
    horizontal_position = 0
    depth = 0
    for step in data :
        [ direction, amount ] = step.split()
        match direction:
            case 'forward' :
                horizontal_position += int( amount )
            case 'down' :
                depth += int( amount )
            case 'up' :
                depth -= int( amount )
                if depth < 0 :
                    depth = 0
    return horizontal_position * depth

def move_and_aim( data ) :
    horizontal_position = 0
    depth = 0
    aim = 0
    for step in data :
        [ direction, amount ] = step.split()
        match direction:
            case 'forward' :
                horizontal_position += int( amount )
                depth += int( amount ) * aim
            case 'down' :
                aim += int( amount )
            case 'up' :
                aim -= int( amount )
    return horizontal_position * depth
    

if __name__ == '__main__' :
    if ( len( sys.argv ) == 0 ) :
        exit
    data = parse_data_file( sys.argv[1] )
    final_position = move( data )
    print( f"Final position: {final_position}" )
    final_position_with_aim = move_and_aim( data )
    print( f"Final position with aim: {final_position_with_aim}")
   
