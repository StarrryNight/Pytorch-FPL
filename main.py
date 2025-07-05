import predict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cleanup
import seaborn as sns
from sklearn.metrics import r2_score
using_week = 15
target_week = 25

#clean up duplicates and in/outs
cleaned = cleanup.handleCleanup(using_week,target_week)

evaluationMetric = ['xP',  
                    #'bps',
                    #'influence', 
                    #'minutes', 
                    'total_points', 
                    'opponent_index',
                    #"assists",
                    #"clean_sheets", 
                    #"creativity", 
                    #"expected_goal_involvements",
                    #"expected_goals",
                    "expected_goals_conceded",
                    "starts"
]
#
predictions = predict.guess(cleaned[0], cleaned[1], cleaned[2], cleaned[3], evaluationMetric)
#results = result.getResults(target_week, names)

df = pd.DataFrame([predictions[0],predictions[1], predictions[2]], index= ['predictions', 'results', 'label'])
Tdf =df.transpose()

sns.set_style("whitegrid")
plot = sns.scatterplot(data=Tdf, x="predictions", y="results")
idx = Tdf["predictions"]>5
for i, row in Tdf.loc[idx].iterrows():
    plot.text(row['predictions'] + 0.1, row['results'] + 0.1, row['label'], ha='left', va='bottom')
print(r2_score(predictions[1], predictions[0]))

plt.show()