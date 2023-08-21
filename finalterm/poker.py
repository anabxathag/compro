"""[Extra]"""
def turnliz(card):
    """return string to list"""
    hand = []
    pai = ""
    for i in card:
        if i.isalnum():
            pai += i
        else:
            if pai != "":
                hand.append(pai)
                pai = ""
    return hand
def calpoint(hand):
    """return score of hand"""
    sco_lek = [int(i[0].replace('T', '10').replace('J', '11').replace('Q', '12')\
            .replace('K', '13').replace('A', '14')) for i in hand]
    sco_lek.sort()
    sco_dok = [i[1] for i in hand]
    nub_lek = [sco_lek.count(i) for i in sco_lek]
    nub_dok = [sco_dok.count(i) for i in sco_dok]
    one_pair = (nub_lek.count(2) == 2)
    two_pair = (nub_lek.count(2) == 4)
    three_kind = (3 in nub_lek)
    reng = 0
    for i in sco_lek:
        if sco_lek[0] + reng == i:
            reng += 1
        else:
            break
    striaght = (reng == 5)
    flush = (5 in nub_dok)
    four_kind = (4 in nub_lek)
    ladub = [one_pair * 1, two_pair * 2, three_kind * 3, striaght * 4, flush * 5\
        , (one_pair and three_kind) * 6, four_kind * 7, (striaght and flush) * 8\
        , ((sco_lek == [10, 11, 12, 13, 14]) and flush) * 9]
    return max(ladub)
def main():
    """Hard - Poker"""
    card_1 = input().upper()
    card_2 = input().upper()
    hand_1 = turnliz(card_1)
    hand_2 = turnliz(card_2)
    score_1 = calpoint(hand_1)
    score_2 = calpoint(hand_2)
    if score_1 > score_2:
        print("Player 1")
    elif score_1 < score_2:
        print("Player 2")
main()
