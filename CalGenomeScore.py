#!/usr/bin/python

Pattern = "AAA"
Text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"

def PatternCount(Pattern,Text):
   count = 0
   for i in range(len(Text)-len(Pattern)+1):
       if Text[i : i+len(Pattern-1)] == Pattern:
            count += 1
   print(count)
    

