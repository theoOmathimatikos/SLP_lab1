#!/bin bash

# Run spell corrector for an input word

# Usage:
#   bash scripts/predict.sh MY_SPELL_CHECKER tst
# Output:
#   test

# Command line args
SPELL_CHECKER_COMPILED=${1}
WORD=${2}


# Constants.
CURRENT_DIRECTORY=$(dirname $0)

###
# Make sure these files exist
CHARSYMS=./chars.syms
WORDSYMS=./words.syms
###

# Make input fst for the misspelled word
python mkfstinput.py ${WORD} |   # pairnei leksh thn pernaei apodoxea
    # Compile and compose with the spell checker
    fstcompile --isymbols=${CHARSYMS} --osymbols=${CHARSYMS} |    
    fstcompose - ${SPELL_CHECKER_COMPILED} |  
    # Get shortest path and sort arcs
    fstshortestpath |
    fstrmepsilon |
    fsttopsort |  
    # fere tis pio fthnes metavaseis
    # print output fst using simple_words.syms
    fstprint -osymbols=${WORDSYMS} | 
    # Get destination word (corrected)
    cut -f4 |   # pairnei thn 4h sthlh, sorted. Dhladh tis pio fthnes metavaseis me vash ton spell checker pou eftiaksa.  
    # Ignore epsilon outputs
    grep -v "<epsilon>" |
    # Ignore accepting state line
    head -n -1 |    # pare thn pio fthnh. 
    # Remove trailing new line
    tr -d '\n'
