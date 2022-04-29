import json
import matplotlib.pyplot as plt

path = "/Users/kaanakduman/Documents/GitHub/royal-family-mapper/output.json"
f = open(path)

data = json.load(f)

keys = data.keys()
x = []
y = []
z = []
names = []
arrows = []
for key in keys:
    if key == "Elizabeth II":
        print(str(data[key]['x']) + " " + str(data[key]['y']))
    person = data[key]
    x.append(person['x'])
    y.append(person['y'])
    z.append(person['z'])
    names.append(key)
    children = person['children']
    for i, child in enumerate(children):
        arrows.append([person['x'], person['y'], person['children'][i]['x']-person['x'], person['children'][i]['y']-person['y']])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')

ax.scatter(x, y, z, s=2, color="red")
plt.xlabel("DFS Topological Sort")
plt.ylabel("Kahn's Algorithm Topological Sort")
ax.set_zlabel("Inverse DFS Topological Sort")
plt.title("Royal Family Tree", fontsize=15)
#for i, label in enumerate(names):
#    plt.annotate(label, (x[i], y[i]), fontsize=5)
#for row in arrows:
#    plt.quiver(row[0], row[1], row[2], row[3], angles='xy', scale_units='xy', scale=1, width=0.001)
plt.show()
f.close()
