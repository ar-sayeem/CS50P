with open("languages.csv") as file:
    for line in file:
                 #row = line.rstrip().split(",")
                 #print(f"{row[0]} is {row[1]}")
                 name, level = line.rstrip().split(",")
                 print(f"{name} is {level}")

# split(",") --> confirms that row is end
# in 1 row there maybe many info which is separeated in file with coma(,)