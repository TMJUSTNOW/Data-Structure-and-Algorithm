# -*- coding:utf-8 -*-
# implement kmp algorithm based on the theory:
#   http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

def inter_pre_suf(_str):
    prefixs, suffixs = set(), set()
    for i in range(1, len(_str)):
        prefixs.add(_str[:i])
        suffixs.add(_str[i:])
    inter = prefixs & suffixs
    if not inter:
        return 0
    else:
        return len(inter.pop())

def partial_match(_str):
    match_list = []
    for i in range(len(_str)):
        match_list.append(inter_pre_suf(_str[:(i + 1)]))
    return match_list

def is_sub(_str, _pat):
    match_list = partial_match(_pat)
    pat_idx = 0
    for str_idx in range(len(_str)):
        print 'start_idx:', str_idx
        if _pat[pat_idx] == _str[str_idx]:
            if pat_idx == (len(_pat) - 1):
                start_idx = str_idx - len(_pat) + 1
                print 'pattern matched, start at index: %s, %s' % \
                        (start_idx, _str[start_idx:(start_idx + len(_pat))])
                break
            else:
                pat_idx += 1
        else:
            if pat_idx == 0:
                continue
            else:
                match_idx = match_list[pat_idx - 1]
                pat_idx = match_idx

_str = 'bbc abcdab abcdabcdabde'
_pat = 'abcdabd'
is_sub(_str, _pat)
