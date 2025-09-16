---
source_path: i.md
pages: n/a-n/a
chunk_id: dfc9493b4de38771d75d3c8b5fcd3e635a9bfe33
title: i
---
# Explore numerical data

First we identify numerical data columns

numerical= attrition_data.select_dtypes(include = 'int64').columns
