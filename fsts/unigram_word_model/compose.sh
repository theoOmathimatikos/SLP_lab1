# fstcompile -keep_isymbols --keep_osymbols --isymbols=words.syms --osymbols=words.syms negative_log_acceptor.txt W.fst

fstrmepsilon W.fst | fstdeterminize | fstminimize > W_min.fst
fstrmepsilon V.fst | fstdeterminize | fstminimize > V_min.fst

fstarcsort --sort_type=ilabel V_min.fst V_sorted.fst
fstcompose L.fst V_sorted.fst LV.fst

fstarcsort --sort_type=ilabel W_min.fst W_sorted.fst
fstcompose LV.fst W_sorted.fst LVW.fst
