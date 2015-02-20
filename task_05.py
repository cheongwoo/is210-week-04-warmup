#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


BP_STATUS = raw_input('Tell me a stWhat is your blood pressure? ')
INT_BP = int(BP_STATUS)

if INT_BP <= 89:
    WORD_BP = 'Low'
elif INT_BP >= 90 and INT_BP <= 119:
    WORD_BP = 'Ideal'
elif INT_BP >= 120 and INT_BP <= 139:
    WORD_BP = 'Warning'
elif INT_BP >= 140 and INT_BP <= 159:
    WORD_BP = 'High'
elif INT_BP >= 160:
    WORD_BP = 'Emergency'

OUTPUT = 'Your status is currently: {}'.format(WORD_BP)
print OUTPUT
