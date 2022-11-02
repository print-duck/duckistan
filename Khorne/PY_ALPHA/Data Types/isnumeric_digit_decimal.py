#isdigit       : Decimal( int) , superscript, subscript
#isnumeric : Decimal( int) , superscript, subscript, Vulgar Fractions, Roman numerals
#isdecimal : Decimal (Only Integers) 

Decimal ='24' 
print(Decimal)
print(Decimal.isdigit())
print(Decimal.isnumeric())
print(Decimal.isdecimal())
print()
print('_________________________')

point_value ='2.4'
print(point_value)
print(point_value.isdigit())
print(point_value.isnumeric())
print(point_value.isdecimal())
print()
print('_________________________')

Subscript='5₀'
print(Subscript)
print(Subscript.isdigit())
print(Subscript.isnumeric())
print(Subscript.isdecimal())
print()
print('_________________________')

Superscript='8⁰'
print(Superscript)
print(Superscript.isdigit())
print(Superscript.isnumeric())
print(Superscript.isdecimal())
print()
print('_________________________')

Vulgar_Fractions='7¾'
print(Vulgar_Fractions)
print(Vulgar_Fractions.isdigit())
print(Vulgar_Fractions.isnumeric())
print(Vulgar_Fractions.isdecimal())
print()
print('_________________________')

Currency_Numerators='188$'
print(Currency_Numerators)
print(Currency_Numerators.isdigit())
print(Currency_Numerators.isnumeric())
print(Currency_Numerators.isdecimal())
print()
print('_________________________')

Roman_Numerals='ⅠⅢⅧⅰⅱⅲ'
print(Roman_Numerals)
print(Roman_Numerals.isdigit())
print(Roman_Numerals.isnumeric())
print(Roman_Numerals.isdecimal())
print()
print('_________________________')

'''
import sys
import unicodedata
from collections import defaultdict

d = defaultdict(list)
for i in range(sys.maxunicode + 1):
    s = chr(i)
    t = s.isnumeric(), s.isdecimal(), s.isdigit()
    if len(set(t)) == 2:
        try:
            name = unicodedata.name(s)
        except ValueError:
            name = f'codepoint{i}'
        print(s, name)
        d[t].append(s)
'''
