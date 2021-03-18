

# Check borders !!!!!!!!!!!!!
for i in row:
	for j in col:
		if word_a[i] == word_b[j]:
			cell[i][j] = cell[i-1][j-1] + 1
		else:
			cell[i][j] = max(cell[i-1,j], cell[i,j-1])