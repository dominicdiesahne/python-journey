# Tower of Hanoi Algorithm from FreeCodeCamp.org
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = [f'{rods[0]} {rods[1]} {rods[2]}']

    def move(disks, source, auxiliary, target):
        if disks == 0:
            return
        move(disks - 1, source, target, auxiliary)
        rods[target].append(rods[source].pop())
        states.append(f'{rods[0]} {rods[1]} {rods[2]}')
        move(disks - 1, auxiliary, source, target)

    move(n, 0, 1, 2)
    return '\n'.join(states)