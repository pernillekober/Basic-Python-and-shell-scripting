#Part1: Ex1 - get lines that match with country values and place in new list
grep -E "^[A-Z]{3}[,]" owid-covid-data.csv > owid-covid-data-filtered.csv

#Part1: Ex2 - country codes in file | get unique values | count lines
cut -c 1-3 < owid-covid-data-filtered.csv | uniq | wc -l

#Part1: Ex3 - extract all values in date column | year and mont | sort | uniqe values
cut -d ',' -f 4 owid-covid-data-filtered.csv | cut -c 1-7 | sort -s | uniq

# part1: Ex4 - lines that matches with date | take country and total_deaths column | sort numerically by total_deaths | ten first | country values
grep -E "[0-9]{4}[-][1][0][-][1][0]" owid-covid-data-filtered.csv | cut -d ',' -f 3,8 | sort -k 2 -t ',' -n -r | head | cut -d ',' -f 1

#part1: Ex5 - lines that matches with date | take country and total_deaths_per_million column | sort numerically by total_deaths | ten first | country values 
grep -E "[0-9]{4}[-][1][0][-][1][0]" owid-covid-data-filtered.csv | cut -d ',' -f 3,14 | sort -k 2 -t ',' -n -r | head | cut -d ',' -f 1
