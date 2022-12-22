grossIncome = int(input('your gross income'))
dependents = int(input('number of dependents'))
taxableincome = round(grossIncome) - 10000 -dependents*3000
a =taxableincome *0.2
print('tax is:',a)
