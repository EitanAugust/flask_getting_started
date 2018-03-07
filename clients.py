import requests
r = requests.get("http://vcm-3592.vm.duke.edu:5000/name")
name = r.json()
print(name)

r1 = requests.get("http://vcm-3592.vm.duke.edu:5000/hello/Eitan")
name1 = r1.json()
print(name1)

r2 = requests.post("http://vcm-3592.vm.duke.edu:5000/distance", json={"a": (1,2), "b": (1,4)})
dist_result = r2.json()
print(dist_result)
