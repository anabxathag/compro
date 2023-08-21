"""mongkul method""" 
def main():
    """Mapping Direction"""
    txt = input()
    axis_x = []
    axis_y = []
    axis = []
    val_x = 0
    val_y = 0
    axis_x.append(val_x)
    axis_y.append(val_y)
    for loop in txt:
        if loop == 'N':
            val_y -= 1
        elif loop == 'S':
            val_y += 1
        elif loop == 'W':
            val_x -= 1
        elif loop == 'E':
            val_x += 1
        axis_x.append(val_x)
        axis_y.append(val_y)
    val_x = abs(min(axis_x))
    val_y = abs(min(axis_y))
    for loop in range(len(axis_x)):
        axis_x[loop] += val_x
        axis_y[loop] += val_y
        axis.append([axis_x[loop], axis_y[loop]])
    val_x = abs(max(axis_x))
    val_y = abs(max(axis_y))
    start = axis.pop(0)
    stop = axis.pop(len(axis) - 1)
    for loop_y in range(val_y + 1):
        for loop_x in range(val_x + 1):
            ans = []
            ans.append(loop_x)
            ans.append(loop_y)
            if ans == start:
                print('B', end=' ')
            elif ans == stop:
                print('E', end=' ')
            elif ans in axis:
                print('O', end=' ')
            else:
                print('-', end=' ')
        print('')
main()