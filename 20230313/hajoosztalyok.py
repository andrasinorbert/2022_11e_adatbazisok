osztaly=[
    "Bismark.",
    "Iowa",
    "Kongo",
    "North Carolina",
    "Renown",
    "Revenge",
    "Tennessee",
    "Yamato"
]
tipus=[
    "bb",
    "bb",
    "bc",
    "bb",
    "bc",
    "bb",
    "bb",
    "bb"
]
orszag=[
    "Németország",
    "USA",
    "Japán",
    "USA",
    "Nagy Britannia",
    "Nagy Britannia",
    "USA",
    "Japán"
]
agyukszama=[
    8,9,8,9,6,8,12,9
]
kaliber=[
    15,16,14,16,15,15,14,18
]
vizkiszoritas=[
    42000,
    46000,
    32000,
    37000,
    32000,
    29000,
    32000,
    65000
]

sql=""
for i in range(len(osztaly)):
    sql+="INSERT INTO `Hajoosztalyok`(`Osztály`, `típus`, `Ország`, `ágyúkSzáma`, `kaliber`, `vízkiszorítás`) VALUES ("
    sql+="'"+osztaly[i]+"',"
    sql+="'"+tipus[i]+"',"
    sql+="'"+orszag[i]+"',"
    sql+=str(agyukszama[i])+","
    sql+=str(kaliber[i])+","
    sql+=str(vizkiszoritas[i])+");"

print(sql)