
import json


with open('input_day7.txt') as file:
    commands = file.read().splitlines()


children = {}	#Map of dirs to their children, containing file names in the directory
filesizes = {}	#Sizes of all files
dirsizes = {}	#Sizes of all dirs
wd = []	#direcorty/folder we are in
total = 0

for command in commands:
    if command[0] == '$':
        if command[2:4] == 'cd':
            dir = command.strip()[5:]
            if dir == '/':
                wd.append('')
            elif dir == '..':
                wd.pop()
            else:
                wd.append(dir)

    else:
       file_size, file_name = command.split(' ')
       if file_size != 'dir':
        filesizes['/'.join(list(wd))+'/'+file_name] = int(file_size)
       children.setdefault('/'.join(list(wd)), []).append(file_name) #setdefault lägger in värdet om det inte finns sedan innan. Om det finns, läggs det inte till.

def compute_dir_size(d: str):
	dchn = children.get(d)
	if dchn:
		s = sum(compute_dir_size(d+'/'+ch) for ch in dchn)
		dirsizes[d] = s
		return s
	else:
		return filesizes.get(d)
        
      

compute_dir_size('')

#=== PART 1===
# ===== source advc slack channel Kristoffer Hallqvist

print(f' The answer is: {sum(v for v in dirsizes.values() if v < 100000)}')


# === PART 2 ===
# ===== source advc slack channel

print('Part 2: Answer is: ', min(v for v in dirsizes.values() if v > (dirsizes[''] - 40000000)))