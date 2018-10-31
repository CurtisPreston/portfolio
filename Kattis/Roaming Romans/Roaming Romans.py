# Roaming Romans
# https://open.kattis.com/problems/romans



miles = float(input())


Roman=((5280/4854)*miles)*1000
Roman=round(Roman)
print(Roman)

    