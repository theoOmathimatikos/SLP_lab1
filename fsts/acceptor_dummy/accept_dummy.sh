fstcompile --keep_isymbols --keep_osymbols -isymbols=chars.syms -osymbols=simple_words.syms V_dummy.fst V_dummy.binfst
# fstdraw --isymbols=chars.syms --osymbols=simple_words.syms V_dummy.binfst binary_dummy.dot
# dot -Tpng binary_dummy.dot > model_draw.png

fstrmepsilon V_dummy.binfst | fstdeterminize | fstminimize > V_dummy_min.fst
# fstdraw --isymbols=chars.syms --osymbols=simple_words.syms V_dummy_min.fst binary_dummy_min.dot
# dot -Tpng binary_dummy_min.dot > draw_dummy_min.png
