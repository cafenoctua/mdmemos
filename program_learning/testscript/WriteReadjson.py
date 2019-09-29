import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy "}
        ]
}

# 表示
print(j)
print("###############")
print(json.dumps(j))

# Write
with open('test.json', 'w') as f:
    json.dump(j, f)

# Read
print("############")
with open('test.json', 'r') as f:
    print(json.load(f))