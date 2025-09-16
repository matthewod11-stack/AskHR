---
source_path: i.md
pages: n/a-n/a
chunk_id: 4703e54037fe9c3eb30980a25ae75774c2a77279
title: i
---
# for col in attrition_data.columns:

uniques = len(attrition_data[col].unique())

if uniques == 1:

print("Dropping col: ", col)
