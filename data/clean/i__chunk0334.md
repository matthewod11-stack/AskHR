# Explore numerical data

First we identify numerical data columns

numerical= attrition_data.select_dtypes(include = 'int64').columns