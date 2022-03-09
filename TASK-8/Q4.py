import numpy as np
import pandas as pd

comment = pd.Series(['have', 'a', 'good', 'day'])
Title = comment.str.title()
print(Title[0], Title[1], Title[2], Title[3])
