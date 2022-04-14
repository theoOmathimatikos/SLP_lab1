fstcompile --keep_isymbols --keep_osymbols -isymbols=chars.syms -osymbols=chars.syms L.fst L.binfst
fstcompile -isymbols=chars.syms -osymbols=chars.syms draw.fst draw.binfst
fstdraw --isymbols=chars.syms --osymbols=chars.syms draw.binfst binary.dot
dot -Tpng binary.dot > model_draw.png
