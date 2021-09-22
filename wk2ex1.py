e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]   # [2, 7, 5, 9]
answer1 = e[1:3]             # [7, 1]
answer2 = pi[1:4:2] + e[:1]  # [1, 1, 2]
answer3 = pi[1:]             # [1, 4, 1, 5, 9]
answer4 = e[::-2] + pi[::2]  # [1, 2, 3, 4, 5]

print(f'1: {answer0}')
print(f'2: {answer1}')
print(f'3: {answer2}')
print(f'4: {answer3}')
print(f'5: {answer4}')


# Oefeningen met strings

h = "hanze"
s = "hogeschool"
g = "groningen"

answer5 = s[0:2] + g[4]      # hoi
answer6 = s[4:8] + 2 * g[-2:]  # schoenen
answer7 = h[1:] + s[1:]  # anzeogeschool
answer8 = g[0] + h[1:3][::-1] + g[0] + \
    h[1:3][::-1] + 5 * h[:2]  # gnagnahahahahaha
answer9 = s[-1] + s[1:4][::-1] + g[2:4][::-1] + s[1:4][::-1]  # legonoego
answer10 = s[3::6][::-1] + g[::6] + g[4:7] + s[4]  # leggings

print(f'1: {answer5}')
print(f'2: {answer6}')
print(f'3: {answer7}')
print(f'4: {answer8}')
print(f'5: {answer9}')
print(f'6: {answer10}')
