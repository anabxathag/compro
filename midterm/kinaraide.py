"""devlab"""
def main():
    """what u want to eat?"""
    dad = input().capitalize()
    mom = input().capitalize()
    bigbro = input().capitalize()
    younsis = input().capitalize()
    fod_vote = [dad, mom, bigbro, younsis]
    uni_set = []
    for i in fod_vote:
        if i not in uni_set:
            uni_set.append(i)
    num = []
    for i in uni_set:
        coe = 0
        coe += fod_vote.count(i)
        num.append(coe)
    vod_ax = num.index(max(num))
    vod_in = num.index(min(num))
    if vod_in != vod_ax:
        print(uni_set[vod_ax])
    else:
        print(younsis)
main()
