import montydb

client = montydb.MontyClient('cafe')

db = client.ingrediente

db.ingrediente.insert_one({'nome':'café'},{'$set': {'unidade_medida':'kg'}})

for documento in db.ingrediente.find({'nome':'café'}):
    print(documento)

print(documento['nome'])


