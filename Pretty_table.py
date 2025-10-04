from prettytable import PrettyTable

table=PrettyTable() 
table.add_column("City name",["dhaka","chittagong"])
table.add_column("Annual Rainfall",[12,56])
table.align="l"
print(table)