import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN                                      Description           Speed    MTU")
print("-" * 80)

interfaces = data["imdata"]

for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<40} {description:<20} {speed:<8} {mtu}")