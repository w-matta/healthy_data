def get_hdi_vals(row, hdi_years):
  hdi_values = []
  for year in hdi_years:
    hdi_values.append(row[year])
  return hdi_values

def get_le_vals(row, le_years):
  pop_values = []
  for year in le_years:
    pop_values.append(row[year])
  return pop_values

def cols_to_list(row, cols):
  values = []
  for col in cols:
    values.append(row[col])
  return values

def get_hdi_pop_pairs(row, hdi_years, le_years):

  hdi_vals = get_hdi_vals(row, hdi_years)
  pop_vals = get_le_vals(row, le_years)

  pairs = []
  for i in range(len(hdi_vals)):
    pairs.append({
      'hdi': hdi_vals[i],
      'le': pop_vals[i],
      'year': int(1990 + i)
    })
  return pairs