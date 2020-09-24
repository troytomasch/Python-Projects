# Troy Tomasch
#
# Use it or Lose it HW
#
# I pledge my honor that I have abided by the Stevens Honor System

def makeChange(amount, coins):
    '''Determine the least amount of coins to add up to the total amount
    and show which coins it takes'''
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"), []]
    if coins[0] > amount:
        return makeChange(amount, coins[1:])
    useIt = makeChange(amount - coins[0], coins)
    loseIt = makeChange(amount, coins[1:])
    return min([useIt[0]+1, [coins[0]]+useIt[1]], loseIt)


def LCS(a, b):
    '''Return the string of the longest common substring'''
    if not (a and b):
        return ''
    if a[0] == b[0]:
        return a[0] + LCS(a[1:], b[1:])
    if len(LCS(a[1:],b)) > len(LCS(a, b[1:])):
        return LCS(a[1:], b)
    else:
        return LCS(a, b[1:])

def PLCS(a,b):
    s = LCS(a,b)
    if not s:
        return [[-1], [-1]]
    def help(tring, subtring, final, count):
        if not tring or subtring:
            return []
        if tring[0] == subring[0]:
            [final] + [count]
            subtring = subtring[1:]
        return help(tring[1:], subtring, final, count+1)
    return [help(a, s, [], 0), help(b, s, [], 0)]
