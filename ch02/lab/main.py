import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
#addition
classes_per_week = 3

print("Classes per week:", classes_per_week)

cost_per_class = (cost_per_week / classes_per_week)

print("Cost of each class:", cost_per_class)



#Part B
majors = ("pre med","cs","business","bio","psycology")
assigned_major = random.choice(majors)
print("your assigned major:", assigned_major)