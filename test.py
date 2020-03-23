'''
字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。
例如：
输入：19
输出：2
输入：258
输出：2
输入：0219
输出：3
'''


all={}


def add_a(digitarray, before_key):
    before_key = before_key + digitarray[0:2] + "_"
    all.update({before_key: digitarray[2:]})


def how_many_ways(digitarray, before_key=""):
    if digitarray == "":
        sums = 0
        print(all)
        for i in all.keys():
            if all[i] == "":
                sums += 1
        return sums
    if (digitarray[0] == '1' or digitarray[0] == '2') and len(digitarray)>=2:
        tmp_before_key = before_key + digitarray[0:2] + "_"
        all.update({tmp_before_key: digitarray[2:]})
        how_many_ways(digitarray[2:], tmp_before_key)
    before_key = before_key + digitarray[0:1] + "_"
    all.update({before_key: digitarray[1:]})
    print('bbbb',all)
    return how_many_ways(digitarray[1:], before_key)

print(how_many_ways('0219',""))

