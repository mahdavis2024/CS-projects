from pathlib import Path

cur = Path.cwd()

for i in range(1,4):
	folder = Path('my serie', f'Season {i}')
	folder.mkdir(parents = True, exist_ok= True)
	for j in range(1,6):
		file = folder.joinpath(f'S0{i}E0{j}.srt')
		# file.touch()
		file.write_text(f'subtile episode {j}')




























# cur = Path.cwd() 

# folder = Path('reports')
# folder.mkdir(exist_ok= True)

# for f in cur.iterdir():
# 	if f.stem.startswith('weekly') and f.suffix == '.docx':
# 		dest = folder / f.name
# 		dest.write_bytes(f.read_bytes())

# for f in cur.glob('weekly*.pdf'):
# 	dest = folder / f.name
# 	dest.write_bytes(f.read_bytes())

# for f in cur.glob('weekly*'):
# 	if f.is_file():
# 		f.unlink()




# for i in range(1,4):
# 	folder = Path('tv show', f'Season {i}')
# 	folder.mkdir(parents=True)
# 	for j in range(1,6):
# 		file = Path(folder, f'S0{i}E0{j}.srt')
# 		file.write_text(f'subtile for episode {j} of season {i}')
