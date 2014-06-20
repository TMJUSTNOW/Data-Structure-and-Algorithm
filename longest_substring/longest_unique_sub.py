s = 'abcaacdeabacdefg'
print 'original string:', s

# O(n)
d = {}
for idx, val in enumerate(s):
    d.setdefault(val, []).append(idx)
print 'occurence dict:', d

def seg(split_char, start_idx, end_idx, _str, occ_dict):
    vals = occ_dict[split_char]
    vals = [val for val in vals if (val >= start_idx) and (val <= end_idx)]
    if len(vals) <= 1:
        return [(start_idx, end_idx)]
    else:
        res = []
        fir_pair = (start_idx, vals[1] - 1)
        las_pair = (vals[-2] + 1, end_idx)
        res.append(fir_pair)
        if len(vals) > 2:
            for idx in range(len(vals) - 2):
                cur_pair = (vals[idx] + 1, vals[idx + 2] - 1)
                res.append(cur_pair)
        res.append(las_pair)
        return res

seg_char = d.keys()[0]
res = seg(seg_char, 0, len(s)-1, s, d)
for key, vals in d.items():
    if (key == seg_char) or (len(vals) <= 1):
        continue
    new_res = []
    for idx, (_start, _end) in enumerate(res):
        tmp_res = seg(key, _start, _end, s, d)
        for new_pair in tmp_res:
            new_res.append(new_pair)
    res = new_res
print 'result:'
for idx, (_start, _end) in enumerate(res):
    print "%s. %s(%s)%s" % (idx, s[:_start], s[_start:(_end + 1)], s[(_end + 1):])

max_pair = max(res, key=lambda vals: vals[1] - vals[0] + 1)
_start, _end = max_pair
print "longest: %s(%s)%s" % (s[:_start], s[_start:(_end + 1)], s[(_end + 1):])
