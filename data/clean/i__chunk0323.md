# for col in attrition_data.columns:

uniques = len(attrition_data[col].unique())

if uniques == 1:

print("Dropping col: ", col)