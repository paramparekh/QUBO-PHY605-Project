import pandas as pd
import numpy as np

# slack df: 10 variables
slack_cols = [f"x_{i}" for i in range(10)] + ["energy", "num_occurrences"]
df_slack = pd.DataFrame([np.zeros(12)], columns=slack_cols)
df_slack.to_json("QUBO/dwave_results_slack.json")

# unbalanced df: 5 variables
unb_cols = [f"x_{i}" for i in range(5)] + ["energy", "num_occurrences"]
df_unb = pd.DataFrame([np.zeros(7)], columns=unb_cols)
df_unb.to_json("QUBO/dwave_results_unbalanced.json")
