import json
from pathlib import Path

path = Path('telecom.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
idx = 25

new_code = '''from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Define base path for saving outputs
base = Path('C:/dataset1')   # adjust if needed

# Experience Metrics
experience_cols = [
    'TCP_DL_Retrans_Vol_Bytes', 'TCP_UL_Retrans_Vol_Bytes',
    'Avg_RTT_DL_ms', 'Avg_RTT_UL_ms',
    'Avg_Bearer_TP_DL_kbps', 'Avg_Bearer_TP_UL_kbps',
    'Handset_Type'
]

required_cols = [
    'TCP_DL_Retrans_Vol_Bytes', 'Avg_RTT_DL_ms', 'Avg_Bearer_TP_DL_kbps', 'Handset_Type'
]
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    raise KeyError(f'Missing required columns for experience analysis: {missing_cols}')

experience_summary = df.groupby(user_id).agg(
    average_TCP_retransmission_bytes=('TCP_DL_Retrans_Vol_Bytes', 'mean'),
    average_RTT_ms=('Avg_RTT_DL_ms', 'mean'),
    average_throughput_kbps=('Avg_Bearer_TP_DL_kbps', 'mean'),
    handset_type=('Handset_Type', lambda x: x.mode().iloc[0] if not x.mode().empty else 'Unknown')
).reset_index()

# Cluster experience data
exp_features = experience_summary[['average_TCP_retransmission_bytes', 'average_RTT_ms', 'average_throughput_kbps']].fillna(0)
exp_norm = StandardScaler().fit_transform(exp_features)
kmeans_exp = KMeans(n_clusters=3, random_state=42, n_init=10)
experience_summary['experience_cluster'] = kmeans_exp.fit_predict(exp_norm)

experience_labels = experience_summary.groupby('experience_cluster')[[
    'average_TCP_retransmission_bytes',
    'average_RTT_ms',
    'average_throughput_kbps'
]].mean()

print("Experience cluster centroids:")
print(experience_labels)

# Satisfaction Metrics
eng_cols = ['session_frequency', 'total_duration_ms', 'total_traffic_bytes']

satisfaction_df = engagement_metrics.merge(experience_summary, on=user_id, how='left')
satisfaction_df = satisfaction_df.dropna(subset=['average_TCP_retransmission_bytes', 'average_RTT_ms', 'average_throughput_kbps'])

reference_engagement = engagement_metrics[eng_cols].min()
reference_experience = experience_summary[['average_TCP_retransmission_bytes', 'average_RTT_ms', 'average_throughput_kbps']].min()

def euclidean_distance(row, ref):
    return np.linalg.norm(row - ref)

satisfaction_df['engagement_score'] = satisfaction_df[eng_cols].apply(
    lambda row: euclidean_distance(row.values.astype(float), reference_engagement.values.astype(float)), axis=1
)
satisfaction_df['experience_score'] = satisfaction_df[['average_TCP_retransmission_bytes', 'average_RTT_ms', 'average_throughput_kbps']].apply(
    lambda row: euclidean_distance(row.values.astype(float), reference_experience.values.astype(float)), axis=1
)
satisfaction_df['satisfaction_score'] = (satisfaction_df['engagement_score'] + satisfaction_df['experience_score']) / 2

print('Top 10 satisfied customers:')
print(satisfaction_df.nlargest(10, 'satisfaction_score')[[user_id, 'engagement_score', 'experience_score', 'satisfaction_score']].to_string(index=False))

# Cluster satisfaction scores
satisfaction_norm = StandardScaler().fit_transform(satisfaction_df[['engagement_score', 'experience_score']])
kmeans_satisfaction = KMeans(n_clusters=2, random_state=42, n_init=10)
satisfaction_df['satisfaction_cluster'] = kmeans_satisfaction.fit_predict(satisfaction_norm)

summary_by_cluster = satisfaction_df.groupby('satisfaction_cluster')[['engagement_score', 'experience_score', 'satisfaction_score']].mean()
print('Satisfaction cluster averages:')
print(summary_by_cluster)

print('Cluster counts:')
print(satisfaction_df['satisfaction_cluster'].value_counts())

# Satisfaction graphs
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=satisfaction_df,
    x='engagement_score',
    y='experience_score',
    hue='satisfaction_cluster',
    palette='Set2',
    s=80
)
plt.title('Satisfaction Clusters: Engagement vs Experience')
plt.xlabel('Engagement Score')
plt.ylabel('Experience Score')
plt.legend(title='Satisfaction Cluster')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=summary_by_cluster.reset_index(),
    x='satisfaction_cluster',
    y='satisfaction_score',
    palette='viridis'
)
plt.title('Average Satisfaction Score by Cluster')
plt.xlabel('Satisfaction Cluster')
plt.ylabel('Mean Satisfaction Score')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(
    data=satisfaction_df,
    x='satisfaction_score',
    bins=30,
    kde=True,
    color='steelblue'
)
plt.title('Distribution of Satisfaction Scores')
plt.xlabel('Satisfaction Score')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Save Final Output
output_path = base / 'final_user_satisfaction.csv'
satisfaction_df.to_csv(output_path, index=False)
print('Saved final table to', output_path)
'''

cell = nb['cells'][idx]
cell['source'] = [line + '\n' for line in new_code.splitlines()]
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('updated cell', idx)
