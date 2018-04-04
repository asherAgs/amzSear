import sys

with open(sys.argv[1]) as f:
    for line in f:
        print(' '*8+ line.strip().replace('*','').replace(' #','').replace('#','').replace('`',''))
