import time, emoji
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('{} Feliz ano novo! {}'.format(emoji.emojize(':fireworks:', use_aliases=True), emoji.emojize(':fireworks:', use_aliases=True)))
