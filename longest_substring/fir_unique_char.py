_str = 'adfasdfkjkjlkjafdkbe'
_dict = {}
for idx, c in enumerate(_str):
    _dict.setdefault(c, []).append(idx)

res = [(c, vals[0]) for c, vals in _dict.items() if len(vals) == 1]
print min(res, key=lambda val: val[1])

