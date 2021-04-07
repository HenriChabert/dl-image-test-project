# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Recipe input

folder = dataiku.Folder("3ep5yCky")
paths = folder.list_paths_in_partition()

# Core recipe

LABEL_0 = "lion"
LABEL_1 = "tiger"

df = pd.DataFrame(columns=['path', 'label'])
for i,j in enumerate(paths):
    if LABEL_0 in j:
        df.loc[i] = [j[1:], LABEL_0]
    if LABEL_1 in j:
        df.loc[i] = [j[1:], LABEL_1]

# Recipe output

output = dataiku.Dataset("labels")
output.write_with_schema(df)
