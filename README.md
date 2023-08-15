# TestBenchDataColector
~Componenta DataColector

##Colectarea si incarcarea datelor in MongoDB

-Scriptul **DBCollector** se utilizeaza pentru a colecta datele si de a le incarca intr-o baza de date MongoDB. Acesta se foloseste de scripturile **generatejson.py** si **introducereDB.py** pentru a genera datele in format JSON si pentru a le incarca in baza de date.

###Functionare

-Se instaleaza MongoDB: https://www.mongodb.com/try/download/community si ne conectam (config.yml - fisier de configurare a bazei de date)

-Scriptul **DBCollector** primeste argumente de la linia de comanda pentru a specifica directorul care contine fisierele cu datele de intrare sau fisierul. Pentru a rula scriptul, se deschide terminalul si se navigheaza la directorul in care se afla acesta. Apoi se folosesc una din urmatoarele comenzi pentru a colecta si incarca datele in baza de date: 

             python DBCollector.py --dir=/calea_catre_director/
             
             python DBCollector.py --file=/calea_catre_fisier/

-Este necesara instalarea modulelor Python: pymongo, argparse, json si yaml

# TestBenchDetailsViewer


Pentru functionarea cu baza de date este nevoie de eliminarea primelor date din 'tests', adica "file_1.txt, tb1_test_name". campul testname din bd este modificat pentru fisierele date de Serban. Nu mai e testname ci test_name. 

--- Pentru a putea rula paginile web, trebuie accesat linkul primit de la apelul fisierului API_server.py.
