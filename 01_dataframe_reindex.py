# Reindexing DataFrame
# For each day, restarting the index

new_date = []
d = 0
current_camp_id = 0

for i in range(len(data_2)):

  #print(i, data_2['CampaignId'][i], data_2['Date'][i], data_2['spend'][i])

  if data_2['CampaignId'][i] == current_camp_id:
    d += 1
    new_date.append(d)
  else:
    d = 0
    new_date.append(d)
    current_camp_id = data_2['CampaignId'][i]
  
data_2['new_date'] = new_date

columns = ['CampaignId', 'new_date', 'spend']
data_3 = data_2[columns]

g = sns.FacetGrid(data_3, row="CampaignId", height=5)
g.map(sns.lineplot, "new_date", "spend")
