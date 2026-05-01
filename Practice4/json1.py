import json
with open('sample-data.json') as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-" * 80)
for imdata in data["imdata"]:
    attributes = imdata['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<6}")