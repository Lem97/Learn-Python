import sys

# Google summer of code, Qualification Round Africa, 2010
# https://code.google.com/codejam/contest/351101/dashboard#s=p1

# Step 1: Read input file
# define filename
infile = sys.argv[1]

# read into python
file_id = open(infile, 'r')

# Step 2: Read the number of test cases
N = int(file_id.readline())

# Step 3: Define an output file
outfile = infile.replace('.in', '.out')
file_out = open(outfile, 'w')

# Step 4: Loop through the test cases
for line in range(N):

    # read the line
    words = file_id.readline()
    lst = words.rstrip('\n').split(' ')

    # find out how many words are in the list
    w = len(lst)

    # build the output string
    output = "Case #%d:" % (line+1)

    # loop through the words from back to front
    for wi in range(-1, -w-1, -1):
        output += " %s" % lst[wi]

    if (line < N-1):
        # go to the next line
        output += "\n"

    # write to the output file
    file_out.write(output)

# close the input and output files
file_id.close()
file_out.close()
