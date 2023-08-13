# TestBenchDetailsViewer


Pentru functionarea cu baza de date este nevoie de eliminarea primelor date din 'tests', adica "file_1.txt, tb1_test_name". campul testname din bd este modificat pentru fisierele date de Serban. Nu mai e testname ci test_name. 

Daca o sa aveti ceva de genul 

File "c:\Users\Asus\workspace\PracticaAMD\webapp\TestBenchDetailsViewer\bdqueries.py", line 164, in main
    print("get_test_names:", query_tests.get_test_names())
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Asus\workspace\PracticaAMD\webapp\TestBenchDetailsViewer\bdqueries.py", line 141, in get_test_names
    if document["test_name"] not in test_names:
       ~~~~~~~~^^^^^^^^^^^^^
KeyError: 'test_name'

Stergeti acele fisiere din bd, tests. xdd