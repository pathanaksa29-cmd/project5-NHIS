import json
from pathlib import Path

path = Path('telecom.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
idx = 25
cell = nb['cells'][idx]
source = ''.join(cell['source'])
marker = '# Save Final Output'
insert = '''
# Top 10 customers by satisfaction score
plt.figure(figsize=(12, 6))
top10_satisfied = satisfaction_df.nlargest(10, 'satisfaction_score')
sns.barplot(
    data=top10_satisfied,
    x='satisfaction_score',
    y=user_id,
    palette='coolwarm'
)
plt.title('Top 10 Customers by Satisfaction Score')
plt.xlabel('Satisfaction Score')
plt.ylabel(user_id)
plt.tight_layout()
plt.show()
'''
if marker not in source:
    raise ValueError(f'Marker not found: {marker}')
source = source.replace(marker, insert + marker)
cell['source'] = [line + '\n' for line in source.splitlines()]
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('updated cell', idx)
