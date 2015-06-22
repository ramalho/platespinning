import sys
import shutil

BASE_CODE = 0x24B6 - 1  # U+24B6 = Ⓐ CIRCLED LATIN CAPITAL LETTER A
BASE_CODE_BLACK = 0x1F150 - 1  # U+1F150 = 🅐 NEGATIVE CIRCLED LATIN CAPITAL LETTER A

filename = sys.argv[1]

with open(filename, encoding='utf8') as fp:
    src = fp.read()

shutil.copyfile(filename, filename + '.bkp')

callout_number = 1

while True:
    ascii_callout = '<%d>' % callout_number
    white_callout = chr(BASE_CODE + callout_number)
    black_callout = chr(BASE_CODE_BLACK + callout_number)
    if ascii_callout in src:
        src = src.replace(ascii_callout, white_callout)
    elif black_callout in src:
        src = src.replace(black_callout, white_callout)
    elif white_callout in src:
        src = src.replace(white_callout, black_callout)
    else:
        break
    callout_number += 1

print('%s callouts replaced' % (callout_number-1))

with open(filename, 'wt', encoding='utf8') as fp:
    fp.write(src)
