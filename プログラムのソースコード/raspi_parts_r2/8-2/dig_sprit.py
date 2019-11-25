def dig_sprit( number, digit ):
    buf = [ int(x) for x in list(str(number) ) ]
    
    output = []
    
    i = 0
    while ( i < digit ):
        output.append( 0 )
        i = i + 1
    
    i = len ( buf ) - 1
    dig = 0
    while ( dig < digit ):
        if ( i < 0 ):
            output[ dig ] = 0
        else:
            output[ dig ] = buf[ i ]
            i = i - 1
        dig = dig + 1
    
    return ( output )


