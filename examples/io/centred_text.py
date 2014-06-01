

A_LIST_OF_WORDS = ['installation',
                   'Chamicuro',
                   'foliiferous',
                   'spermatic',
                   'intemperately',
                   'pederastically',
                   'proctosigmoidectomy',
                   'begar']

# Does not work!
print environ.get('COLS')
width, height = console.getTerminalSize()

for word in A_LIST_OF_WORDS:
    print "{word:^{width}}".format(
        word=word, width=width)
