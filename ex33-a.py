i = 0
numbers = []
varr = 6

def numy(ii,jio):
    print(f"My top is ii {ii}")
    numbers.append(ii)
    print(f"Numbers now {numbers}")
    ii = ii+jio

    if ii < varr:
        numy(ii,jio)

numy(i,2)
