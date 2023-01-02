employees=['dhanasekhar']
defaults={"designation":"Developer","salary":96000}

##data=dict()
##for i in employees:
##    data[i]=defaults
##print(data)




data=dict.fromkeys(employees,defaults)
print(data)
