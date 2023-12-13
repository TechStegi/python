tel = {
    "work": {"Jack": "49", "Jill": "06", "James": "44"},
    "private": {"Kyle": "424733", "Karen": "511727"},
}

print("len(tel)", len(tel))  # 2
print("len(tel['work'])", len(tel["work"]))  # 3
print("len(tel['private'])", len(tel["private"]))  # 2
print("tel['work']['Jill']", tel["work"]["Jill"])  # 06
print("tel['work']. get('Jane')", tel["work"].get("Jane"))  # None
print("'06' in tel['work']", "06" in tel["work"])  # False
print("'Jack' in tel['work']", "Jack" in tel["work"])  # True
print("list(tel.keys ())", list(tel.keys()))  # ['work', 'private']
print(
    "list(tel['work']. keys ())", list(tel["work"].keys())
)  # ['Jack', 'Jill', 'James']
print(
    "list(tel['private']. values ())", list(tel["private"].values())
)  # ['424733', '511727']
print(
    "tel['private']. copy ()", tel["private"].copy()
)  # {'Kyle':'424733', 'Karen':'511727'}