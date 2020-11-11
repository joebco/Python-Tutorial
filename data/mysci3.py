# LESSON 2
# Initialize data variable
filename = 'wxobs20170821.txt'

columns = {'date':0,'time':1,'tempout':2}
types = {'tempout': float}
data={}
for column in columns:
    data[column]=[]
# Read the Data file

with open(filename,'r') as datafile:
    for _ in range(3):
        datafile.readline()

    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value = t(split_line[i])
            data[column].append(value)
# DEBUG
print(data['tempout'])


# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2}

# Data types for each column (only if non-string)
types = {'tempout': float}

# Initialize my data variable
data = {}
for column in columns:
   data[column] = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

   # Read the first three lines (header)
   for _ in range(3):
      datafile.readline()

   # Read and parse the rest of the file
   for line in datafile:
      split_line = line.split()
      for column in columns:
         i = columns[column]
         t = types.get(column, str)
         value = t(split_line[i])
         data[column].append(value)

# DEBUG
print(data['tempout'])
