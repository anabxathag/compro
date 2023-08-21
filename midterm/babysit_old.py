"""[Week 5]"""
import datetime as dt
def case_1(st_rt, st_p, hour_jup, mn_jup):
    """เริ่มงานก่อน 8 โมง"""
    if st_p <= dt.datetime(2023, 2, 7, 8, 0) and st_p > st_rt:
        tm_wk_1 = str(st_p - st_rt)
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75)
    elif dt.datetime(2023, 2, 7, 8, 0) < st_p <= dt.datetime(2023, 2, 7, 21, 0):
        tm_wk_1 = str(dt.datetime(2023, 2, 7, 8, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 7, 8, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75) \
            + (wk_hour_2 * 2.5) + ((wk_min_2 / 60) * 2.5)
    elif st_p > dt.datetime(2023, 2, 7, 21, 0):
        tm_wk_1 = str(dt.datetime(2023, 2, 7, 8, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 7, 21, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75) \
            + (13 * 2.5) + (wk_hour_2 * 1.75) + ((wk_min_2 / 60) * 1.75)
    elif st_p < dt.datetime(2023, 2, 7, 8, 0) and st_p <= st_rt:
        st_p = dt.datetime(2023, 2, 8, hour_jup, mn_jup)
        tm_wk_1 = str(dt.datetime(2023, 2, 7, 8, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 7, 21, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75) \
            + (13 * 2.5) + (wk_hour_2 * 1.75) + ((wk_min_2 / 60) * 1.75)
    print("$%.2f" %salary)
def case_2(st_rt, st_p, hour_jup, mn_jup):
    """เริ่มงานระหว่าง 8 - 21 โมง"""
    if dt.datetime(2023, 2, 7, 8, 0) < st_p <= dt.datetime(2023, 2, 7, 21, 0) and st_p > st_rt:
        tm_wk_1 = str(st_p - st_rt)
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        salary = (wk_hour_1 * 2.5) + ((wk_min_1 / 60) * 2.5)
    elif st_p > dt.datetime(2023, 2, 7, 21, 0):
        tm_wk_1 = str(dt.datetime(2023, 2, 7, 21, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 7, 21, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 2.5) + ((wk_min_1 / 60) * 2.5) \
            + (wk_hour_2 * 1.75) + ((wk_min_2 / 60) * 1.75)
    elif st_p < dt.datetime(2023, 2, 7, 8, 0):
        st_p = dt.datetime(2023, 2, 8, hour_jup, mn_jup)
        tm_wk_1 = str(dt.datetime(2023, 2, 7, 21, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 7, 21, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 2.5) + ((wk_min_1 / 60) * 2.5) \
            + (wk_hour_2 * 1.75) + ((wk_min_2 / 60) * 1.75)
    if dt.datetime(2023, 2, 7, 8, 0) <= st_p < dt.datetime(2023, 2, 7, 21, 0) and st_p <= st_rt:
        st_p = dt.datetime(2023, 2, 8, hour_jup, mn_jup)
        tm_wk_1 = str(dt.datetime(2023, 2, 7, 21, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 8, 8, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 2.5) + ((wk_min_1 / 60) * 2.5) \
            + (11 * 1.75) + (wk_hour_2 * 2.5) + ((wk_min_2 / 60) * 2.5)
    print("$%.2f" %salary)
def case_3(st_rt, st_p, hour_jup, mn_jup):
    """เริ่มงานหลัง 21 โมง"""
    if st_p > dt.datetime(2023, 2, 7, 21, 0) and st_p > st_rt:
        tm_wk_1 = str(st_p - st_rt)
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75)
    elif st_p < dt.datetime(2023, 2, 7, 8, 0):
        st_p = dt.datetime(2023, 2, 8, hour_jup, mn_jup)
        tm_wk_1 = str(st_p - st_rt)
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75)
    elif dt.datetime(2023, 2, 7, 8, 0) <= st_p < dt.datetime(2023, 2, 7, 21, 0):
        st_p = dt.datetime(2023, 2, 8, hour_jup, mn_jup)
        tm_wk_1 = str(dt.datetime(2023, 2, 8, 8, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 8, 8, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75) \
            + (wk_hour_2 * 2.5) + ((wk_min_2 / 60) * 2.5)
    elif st_p >= dt.datetime(2023, 2, 7, 21, 0) and st_p <= st_rt:
        st_p = dt.datetime(2023, 2, 8, hour_jup, mn_jup)
        tm_wk_1 = str(dt.datetime(2023, 2, 8, 8, 0) - st_rt)
        tm_wk_2 = str(st_p - dt.datetime(2023, 2, 8, 21, 0))
        wk_hour_1 = int(tm_wk_1[:tm_wk_1.find(":")])
        wk_min_1 = int(tm_wk_1[tm_wk_1.find(":") + 1 : tm_wk_1.rfind(":")])
        wk_hour_2 = int(tm_wk_2[:tm_wk_2.find(":")])
        wk_min_2 = int(tm_wk_2[tm_wk_2.find(":") + 1 : tm_wk_2.rfind(":")])
        salary = (wk_hour_1 * 1.75) + ((wk_min_1 / 60) * 1.75) \
            + (13 * 2.5) + (wk_hour_2 * 1.75) + ((wk_min_2 / 60) * 1.75)
    print("$%.2f" %salary)
def main():
    """Babysitter วิธีพิสดาร"""
    lem = input()
    jup = input()
    hour_lem = int(lem[: lem.find(":")])
    mn_lem = int(lem[lem.find(":") + 1 :])
    hour_jup = int(jup[: jup.find(":")])
    mn_jup = int(jup[jup.find(":") + 1 :])
    if mn_lem == 60:
        mn_lem = 0
        hour_lem += 1
    if mn_jup == 60:
        mn_jup = 0
        hour_jup += 1
    if hour_lem == 24:
        hour_lem = 0
    if hour_jup == 24:
        hour_jup = 0
    if hour_lem > 24:
        hour_lem -= 24
    if hour_jup > 24:
        hour_jup -= 24
    tm_l = dt.datetime(2023, 2, 7, hour_lem, mn_lem)
    tm_jj = dt.datetime(2023, 2, 7, hour_jup, mn_jup)
    if tm_l < dt.datetime(2023, 2, 7, 8, 0):
        case_1(tm_l, tm_jj, hour_jup, mn_jup)
    if dt.datetime(2023, 2, 7, 8, 0) <= tm_l < dt.datetime(2023, 2, 7, 21, 0):
        case_2(tm_l, tm_jj, hour_jup, mn_jup)
    if tm_l >= dt.datetime(2023, 2, 7, 21, 0):
        case_3(tm_l, tm_jj, hour_jup, mn_jup)
main()
