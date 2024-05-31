#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#单位是万
totalAmount = 1201.67

tumorSampleTotal = 1787
sampleTotal = 56645

tumorCaseTotal = 1765
caseTotal = 30622

manpowerCost = 13
manpowerCostAmount = 262.8

computingCost = 210
computingCostAmount = 331.5

storageCost = 19566
storageCostAmount = 607.37

def calcCost(tsampleTotal, sampleTotal, total):
    return tsampleTotal / sampleTotal * total

def calcPerCost(totalCost, total):
    return totalCost / total




print("样本----》")

cost = calcCost(tumorSampleTotal, sampleTotal, totalAmount)
print("肿瘤 %s 个样本用到的成本= %.5f 万元" % (tumorSampleTotal, cost))
print("肿瘤一个样本用到的成本= %.5f 万元" % (calcPerCost(cost, tumorSampleTotal)))

print("")

cost = calcCost(tumorSampleTotal, sampleTotal, manpowerCost)
print("肿瘤 %s 个样本用到的人力= %.5f 人" % (tumorSampleTotal, cost))
print("肿瘤一个样本用到的人力= %.5f 人" % (calcPerCost(cost, tumorSampleTotal)))
costAmount = calcCost(tumorSampleTotal, sampleTotal, manpowerCostAmount)
print("肿瘤一个样本用到的人力的成本= %.5f 万元" % (calcPerCost(costAmount, tumorSampleTotal)))

print("")

cost = calcCost(tumorSampleTotal, sampleTotal, computingCost)
print("肿瘤 %s 个样本用到的算力= %.5f 台" % (tumorSampleTotal, cost))
print("肿瘤一个样本用到的算力= %.5f 台" % (calcPerCost(cost, tumorSampleTotal)))
costAmount = calcCost(tumorSampleTotal, sampleTotal, computingCostAmount)
print("肿瘤一个样本用到算力的成本= %.5f 万元" % (calcPerCost(costAmount, tumorSampleTotal)))

print("")

cost = calcCost(tumorSampleTotal, sampleTotal, storageCost)
print("肿瘤 %s 个样本用到的存储= %.5f TB" % (tumorSampleTotal, cost))
print("肿瘤一个样本用到的存储= %.5f TB" % (calcPerCost(cost, tumorSampleTotal)))
costAmount = calcCost(tumorSampleTotal, sampleTotal, storageCostAmount)
print("肿瘤一个样本用到存储的成本= %.5f 万元" % (calcPerCost(costAmount, tumorSampleTotal)))

#print("1787=的成本", 1787*0.00464 + 1787*0.00585 + 1787*0.01072)


print("""
""")

print("总成本：%s 万元" % (totalAmount))
print("肿瘤样本总数：%s 个" % (tumorSampleTotal))
print("样本总数：%s 个" % (sampleTotal))
print("肿瘤案例总数：%s 例" % (tumorCaseTotal))
print("案例总数：%s 例" % (caseTotal))
print("用到的人力：%s 人" % (manpowerCost))
print("用到的人力成本：%s 万元" % (manpowerCostAmount))
print("用到的算力：%s 台" % (computingCost))
print("用到的算力成本：%s 万元" % (computingCostAmount))
print("用到的存储：%s TB" % (storageCost))
print("用到的存储成本：%s 万元" % (storageCostAmount))

print("案例----------》")

cost = calcCost(tumorCaseTotal, caseTotal, totalAmount)
print("肿瘤 %s 个案例用到的成本= %.5f 万元" % (tumorCaseTotal, cost))
print("肿瘤一个案例用到的成本= %.5f 万元" % (calcPerCost(cost, tumorCaseTotal)))


print("")

cost = calcCost(tumorCaseTotal, caseTotal, manpowerCost)
print("肿瘤 %s 个案例用到的人力= %.5f 人" % (tumorCaseTotal, cost))
print("肿瘤一个案例用到的人力= %.5f 人" % (calcPerCost(cost, tumorCaseTotal)))
costAmount = calcCost(tumorCaseTotal, caseTotal, manpowerCostAmount)
print("肿瘤一个案例用到的人力的成本= %.5f 万元" % (calcPerCost(costAmount, tumorCaseTotal)))


print("")

cost = calcCost(tumorCaseTotal, caseTotal, computingCost)
print("肿瘤 %s 个案例用到的算力= %.5f 台" % (tumorCaseTotal, cost))
print("肿瘤一个案例用到的算力= %.5f 台" % (calcPerCost(cost, tumorCaseTotal)))
costAmount = calcCost(tumorCaseTotal, caseTotal, computingCostAmount)
print("肿瘤一个案例用到的算力的成本= %.5f 万元" % (calcPerCost(costAmount, tumorCaseTotal)))


print("")

cost = calcCost(tumorCaseTotal, caseTotal, storageCost)
print("肿瘤 %s 个案例用到的存储= %.5f TB" % (tumorCaseTotal, cost))
print("肿瘤一个案例用到的存储= %.5f TB" % (calcPerCost(cost, tumorCaseTotal)))
costAmount = calcCost(tumorCaseTotal, caseTotal, storageCostAmount)
print("肿瘤一个案例用到的存储的成本= %.5f 万元" % (calcPerCost(costAmount, tumorCaseTotal)))


#print("1765=的成本", 1765*0.00858 + 1765*0.01083 + 1765*0.01983)












