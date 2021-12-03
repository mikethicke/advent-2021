import sys

def count_increases( data ) :
    increases = 0
    prev_item = data[0]
    for item in data[1:] :
        if item > prev_item :
            increases += 1
        prev_item = item
    return increases

def count_sliding_increases( data ) :
    increases = 0
    prev_sum = data[0] + data[1] + data[2]
    for i in range( 1, len( data ) - 2 ) :
        current_sum = data[i] + data[i+1] + data[i+2]
        if current_sum > prev_sum :
            increases += 1
        prev_sum = current_sum
    return increases

def parse_data_file( file_name ) :
    with open( file_name, 'r' ) as file :
        data = file.read().splitlines()
    data = list( map( int, data ) )
    return data


if __name__ == "__main__" :
    if ( len( sys.argv ) == 0 ) :
        exit
    data = parse_data_file( sys.argv[1] )
    increases = count_increases( data )
    print( f"Increases: {increases}\n" )
    slidng_increases = count_sliding_increases( data )
    print( f"Sliding increases: {slidng_increases}\n" )
