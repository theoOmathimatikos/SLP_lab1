fstcompile --keep_isymbols --keep_osymbols --isymbols=chars.syms --osymbols=words.syms V.fst V.binfst
# fstdraw --isymbols=chars.syms --osymbols=words.syms V.binfst binary.dot
# dot -Tpng binary.dot > model_draw.png

fstrmepsilon V.binfst | fstdeterminize | fstminimize > V_min.fst
# fstdraw --isymbols=chars.syms --osymbols=words.syms accept_min.fst min_binary.dot
# dot -Tpng min_binary.dot > model_draw_min.png
