import sys

def parse_data_file( file_name ) :
    with open( file_name, 'r' ) as file :
        data = file.read().splitlines()
    return data

def calc_bit_totals( data ) :
    bit_totals = [ 0 ] * len( data[0] )
    for bit_string in data :
        for i in range( len( bit_string ) ) :
            bit_totals[i] += int( bit_string[i] )
    return bit_totals

def omega_and_epsilon( data ) :
    bit_totals = calc_bit_totals( data )
    majority_of_data = len( data ) / 2
    omega_str = ''
    epsilon_str = ''
    for bit_sum in bit_totals:
        if bit_sum >= majority_of_data:
            omega_str += '1'
            epsilon_str += '0'
        else :
            omega_str += '0'
            epsilon_str += '1'
    return ( omega_str, epsilon_str )

def power_consumption( data ) :
    ( omega_str, epsilon_str ) = omega_and_epsilon( data )
    power_consumption = int( omega_str, 2 ) * int( epsilon_str, 2 )
    return power_consumption
    
def life_support( data ) :
    omega_data = data.copy()
    epsilon_data = data.copy()
    str_index = 0
    while len( omega_data ) > 1 :
        ( omega_str, epsilon_str ) = omega_and_epsilon( omega_data )
        omega_data = list ( 
            filter( 
                lambda x: x[str_index] == omega_str[str_index],
                omega_data 
            ) 
        )
        str_index += 1
    str_index = 0
    while len( epsilon_data ) > 1 :
        ( omega_str, epsilon_str ) = omega_and_epsilon( epsilon_data )
        epsilon_data = list ( 
            filter( 
                lambda x: x[str_index] == epsilon_str[str_index],
                epsilon_data 
            ) 
        )
        str_index += 1
    life_support_rating = int( omega_data[0], 2) * int( epsilon_data[0], 2 )
    return life_support_rating


if __name__ == '__main__' :
    if ( len( sys.argv ) == 0 ) :
        exit
    data = parse_data_file( sys.argv[1] )
    power = power_consumption( data )
    print( f"Power Consumption: {power}" )
    life = life_support( data )
    print ( f"Life Support: {life}" )