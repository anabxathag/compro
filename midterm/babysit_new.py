"""[Week 5]"""
def main():
    """Babysitter วิธีดีๆ"""
    lem, jup = input(), input()
    hr_lem, mn_lem = float(lem[: lem.find(":")]), float(lem[lem.find(":") + 1 :])
    hr_jup, mn_jup = float(jup[: jup.find(":")]), float(jup[jup.find(":") + 1 :])
    vela_lem, vela_jup = hr_lem + (mn_lem / 60), hr_jup + (mn_jup / 60)
    if vela_lem < 8:
        salaries = (((vela_jup - vela_lem) * 1.75) * (vela_jup <= 8 and vela_lem < vela_jup)) \
            + ((((8 - vela_lem) * 1.75) + ((vela_jup - 8) * 2.5)) * (8 < vela_jup <= 21)) \
            + ((((8 - vela_lem + vela_jup - 21) * 1.75) + 32.5) * (vela_jup > 21)) \
            + ((((8 - vela_lem + vela_jup + 3) * 1.75) + 32.5) \
            * (vela_jup < 8 and vela_lem >= vela_jup))
    elif 8 <= vela_lem < 21:
        salaries = (((vela_jup - vela_lem) * 2.5) * (8 < vela_jup <= 21 and vela_lem < vela_jup)) \
            + ((((21 - vela_lem) * 2.5) + ((vela_jup - 21) * 1.75)) * (vela_jup > 21)) \
            + ((((21 - vela_lem) * 2.5) + ((vela_jup + 3) * 1.75)) * (vela_jup < 8)) \
            + ((((21 - vela_lem + vela_jup - 8) * 2.5) + 19.25) \
            * (8 <= vela_jup < 21 and vela_lem >= vela_jup))
    elif vela_lem >= 21:
        salaries = (((vela_jup - vela_lem) * 1.75) * (vela_jup > 21 and vela_lem < vela_jup)) \
            + ((((24 - vela_lem + vela_jup) * 1.75)) * (vela_jup <= 8)) \
            + ((((32 - vela_lem) * 1.75) + ((vela_jup - 8) * 2.5)) * (8 < vela_jup < 21)) \
            + ((((32 - vela_lem + vela_jup - 21) * 1.75) + 32.5) \
            * (vela_jup >= 21 and vela_lem >= vela_jup))
    print("$%.2f" %salaries)
main()
