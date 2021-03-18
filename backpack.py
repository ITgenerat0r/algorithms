

for i in row:
	for j in col:
		cell[i][j] = max(cell[i-1][j], cell[i-1][j-volume_current_thing])