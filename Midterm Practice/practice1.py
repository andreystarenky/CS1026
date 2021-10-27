x = ["Today", "is", "Wednesday", "Tomorrow", "Is", "Thursday"]

for i in range(len(x)):
    if i < len(x):
        if(len(x[i])<6):
            x.pop(i)

print(x)