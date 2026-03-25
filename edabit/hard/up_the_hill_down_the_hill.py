"""
If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their average speed traveled was 30mph.

Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.

Examples
ave_spd(18, 20, 60) ➞ 30

ave_spd(30, 10, 30) ➞ 15

ave_spd(30, 8, 24) ➞ 12
"""

def ave_spd(up_time, up_rate, down_rate):
    distance = (up_time) * up_rate
    down_time = distance / down_rate
    ret = (distance * 2) / (up_time + down_time)
    return ret

print(ave_spd(18, 20, 60))
print(ave_spd(30, 10, 30))
print(ave_spd(30, 8, 24))
