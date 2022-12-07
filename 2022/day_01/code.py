elves = list()
# convert our elves to a list of lists
with open("./input") as fh:
    elves = [sum(map(int, elf_data.splitlines())) for elf_data in fh.read().split('\n\n')]
   
        
q1 = "Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?"
print("%s: %s" % (q1, max(elves)))

q2 = "Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?"
print("%s: %s" % (q2, sum(sorted(elves, reverse=True)[:3])))
