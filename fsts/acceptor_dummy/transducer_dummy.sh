fstarcsort --sort_type=ilabel V_dummy_min.fst V_dummy_sorted.fst
# fstdraw --isymbols=chars.syms --osymbols=simple_words.syms V_dummy_min.fst arc_binary.dot
# dot -Tpng arc_binary.dot > arc_convert_dummy.png

fstcompose L.binfst V_dummy_sorted.fst converter_dummy.fst
# fstdraw --isymbols=chars.syms --osymbols=simple_words.syms converter_dummy.fst convert_binary_dummy.dot
# dot -Tpng convert_binary_dummy.dot > convert_dummy.png
