#-------------------------------------------------------------------------
# Settings
#-------------------------------------------------------------------------
settings = {
    'acceptDelay'   : 0.50 ,    # how long to wait on idle before sending the code
    'sipThresh'     : 10 ,      # delta hPa, use to adjust sip sensitivty
    'puffThresh'    : 10 ,      # delta hPa, use to adjust puff sensitivity
}

#-------------------------------------------------------------------------
# Morse Code Mapping
#-------------------------------------------------------------------------
codes = { 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{} }

codes[2][0b10]      = 'a'
codes[4][0b0111]    = 'b'
codes[4][0b0001]    = 'c'
codes[3][0b011]     = 'd'
codes[1][0b1]       = 'e'
codes[4][0b1101]    = 'f'
codes[3][0b001]     = 'g'
codes[4][0b1111]    = 'h'
codes[2][0b11]      = 'i'
codes[4][0b1000]    = 'j'
codes[3][0b010]     = 'k'
codes[4][0b1011]    = 'l'
codes[4][0b0000]    = 'm'
codes[2][0b01]      = 'n'
codes[3][0b000]     = 'o'
codes[4][0b1001]    = 'p'
codes[4][0b0010]    = 'q'
codes[3][0b101]     = 'r'
codes[3][0b111]     = 's'
codes[1][0b0]       = 't'
codes[3][0b001]     = 'u'
codes[4][0b0001]    = 'v'
codes[3][0b100]     = 'w'
codes[4][0b0110]    = 'x'
codes[4][0b0100]    = 'y'
codes[4][0b0011]    = 'z'
