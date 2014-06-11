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
    pat_idx, str_idx = 0, 0
    while str_idx < len(_str):
        if _pat[pat_idx] == _str[str_idx]:
            if pat_idx == (len(_pat) - 1):
                start_idx = str_idx - len(_pat) + 1
                end_idx = str_idx + 1
                print 'pattern "%s" matched, "%s(%s)%s"' % (_pat,
                        _str[:start_idx], _str[start_idx:end_idx], _str[end_idx:])
                break
            else:
                str_idx += 1
                pat_idx += 1
        else:
            if pat_idx == 0:
                str_idx += 1
            else:
                pat_idx = match_list[pat_idx - 1]
    if pat_idx != (len(_pat) - 1):
        print 'pattern %s not found!' % _pat

_str = '@abcd\taaaaaaaabcdeadfasdf'
_pat = 'abcde'
is_sub(_str, _pat)
