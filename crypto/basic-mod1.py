#!/usr/bin/python

msg = [202,137,390,235,114,369,198,110,350,396,390,383,225,258,38,291,75,324,401,142,288,397]

for m in msg:

     m = m % 37
     if (m < 26):
         # convert to uppercase
         print(chr(m+65),end="")
     elif (m < 36):
         # convert to decimal digits
         print(chr((m % 26) + 48),end="")
     else:
         # convert 36 to underscore
         print('_',end="")
print()

