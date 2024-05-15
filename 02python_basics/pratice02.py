#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位")

lastYearScore = 72
thisYearSocre = 85
delta = thisYearSocre - lastYearScore
myPercent = (delta / lastYearScore ) * 100

print(f"小明成绩提升的百分点:{myPercent:.1f}")

