def find_level( real_mA ):
    Max_level = 7.16
    Min_level = 2.16
    Max_mA = 20
    Min_mA = 4
    level = (((Max_level - Min_level) / ( Max_mA - Min_mA)) * ( real_mA - Min_mA)) + Min_level

    return level


def find_mA(level):
    Max_level = 7.16
    Min_level = 2.16
    Max_mA = 20
    Min_mA = 4
    mA = Min_mA + ((Max_mA - Min_mA) * ((level - Min_level) / (Max_level - Min_level)))
    
    return mA

print("mA @ 2.16Level: ", find_mA(2.16))
print("mA @ 7.16Level: ", find_mA(7.16))
print("mA @ 5.4Level: ", find_mA(5.4))

print("Level @ 20mA: ", find_level(20))
print("Level @ 4mA : ", find_level(4))
print("Level: ", find_level(find_mA(5.4))) #Should return 5.4
