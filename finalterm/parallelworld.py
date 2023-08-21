"""[Extra]"""
def main():
    """Intermediate - Parallel World"""
    x_sec = int(input())
    s_par = int(input())
    m_par = int(input())
    h_par = int(input())
    hours = x_sec // (s_par * m_par)
    minute = (x_sec % (s_par * m_par)) // (s_par)
    secon = (x_sec % (s_par * m_par)) % (s_par)
    if hours >= h_par:
        hours -= h_par * (hours // h_par)
    output = "{:02d}:{:02d}:{:02d}".format(hours, minute, secon)
    print(output)
main()
