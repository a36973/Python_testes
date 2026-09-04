frascos =[
{
    "id": "F001",
    "plantas": 12,
    "estado": "adequado"
},
{
    "id": "F002",
    "plantas": 8,
    "estado": "baixo"
},
{
    "id": "F003",
    "plantas": 18,
    "estado": "adequado"
}
]



for frasco in frascos:
    print("ID:", frasco["id"])
    print("Plantas:", frasco["plantas"])
    print("Estado:", frasco["estado"])
    print()