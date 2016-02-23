import csv
import sys

def DOBgen(filename):
    with open (filename,"r") as fi:
        reader = csv.DictReader(fi)
        for row in reader:
            if row['birth_year']!='':
                age = 2016-(int(row['birth_year']))
            yield age

def get_med(count):
    nth_value = ((sum(count.values()))+1)/2
    for age in count.keys():
        nth_value -= count[age]
        if nth_value<=0:
            return age


if __name__=='__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)

    age = DOBgen(sys.argv[1])
    count = {}
    for rider in age:
		count[rider] = count.get(rider,0)+1

    median = get_med(count)
    print median