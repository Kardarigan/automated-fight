with open('output.txt', 'r') as f:
    lines = f.readlines()



for line in lines:
    if line.startswith('@'):
        with open('errors.txt', 'a') as f:
            f.write(line)
