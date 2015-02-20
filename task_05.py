#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


BP_STATUS = raw_input('Tell me a stWhat is your blood pressure? ')
BP_STATUS = int(BP_STATUS)

if BP_STATUS <= 89:
    BP_STATUS = 'Low'
elif BP_STATUS >= 90 and BP_STATUS <= 119:
    BP_STATUS = 'Ideal'
elif BP_STATUS >= 120 and BP_STATUS <= 139:
    BP_STATUS = 'Warning'
elif BP_STATUS >= 140 and BP_STATUS <= 159:
    BP_STATUS = 'High'
elif BP_STATUS >= 160:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {}'.format(BP_STATUS)
print OUTPUT
