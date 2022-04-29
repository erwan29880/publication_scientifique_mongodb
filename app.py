from pymongo import MongoClient
import time


def main():

    # connexion Mongo
    client = MongoClient(
        host = 'mongodb3:27017', 
        serverSelectionTimeoutMS = 3000, 
        username="root",
        password="pa",
    )
    db = client['DBLP']
    col = db['publis']

    #-------
    #nombre de documents
    print('Nombre de documents dans la collection : ')
    time.sleep(0.5)
    print(f'Nombre de documents : {col.count_documents({})}')

    #--------
    #lister les livres
    print('\n\nListe des livres : ')
    time.sleep(1.5)
    [print(x) for x in col.find({'type':'Book'})]

    #--------
    # lister les livres après 2014
    print('\n\nListe des livres après 2014 : ')
    time.sleep(1.5)
    [print(x) for x in col.find({'type':'Book', 'year':{"$gte":2014}})]

    #--------
    # Lister les publications de l’auteur Toru Ishida
    print('\n\nListe des publications de Toru Ishida : ')
    time.sleep(1.5)
    [print(x) for x in col.find({'authors':"Toru Ishida"})]

    #-------
    # Lister les auteurs distincts
    print('\n\nListe des auteurs distincts : ')
    time.sleep(1.5)
    [print(x) for x in col.distinct('authors')]

    #-------
    # Lister les publications de l’auteur Toru Ishida triés par titre
    print('\n\nListe des publications de Toru Ishida classés par titre : ')
    time.sleep(1.5)
    [print(x) for x in col.find(filter={"authors": 'Toru Ishida'}, sort=[( "title", 1 )])]

    #-------
    #Compter le nombre de ses publications
    print('\n\nNombre de publications de Toru Ishida : ')
    time.sleep(1.5)
    print(col.count_documents({'authors':"Toru Ishida"}))


    #-------
    # groupement de ses publications par type depuis 2011
    print('\n\nListe des publications de Toru Ishida classés par type depuis 2011 : ')
    time.sleep(1.5)
    [print(x) for x in col.find(filter={"authors": 'Toru Ishida', 'year':{"$gte":2011}}, sort=[( "type", 1 )])]


    #-------
    # Compter le nombre de publications par auteur et trier le résultat par ordre croissant ;
    print('\n\nNombre de publications par auteur par ordre croissant : ')
    time.sleep(2)
    [print(x) for x in col.aggregate([{'$unwind': '$authors'},{'$group': {'_id': '$authors', 'sum': { '$sum': 1}}}, {'$sort' : {'sum' : 1 } }])]


main()