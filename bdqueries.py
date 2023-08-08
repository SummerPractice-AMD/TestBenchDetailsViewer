from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["RegressionDetails"]
collection = db["testruns"]


def find_file():
    results = collection.find({"run_id": "file_2"})
    for result in results:
        print(result)


def file_no_runs():
    return collection.count_documents({})


def file_no_errors():
    documents = collection.aggregate(
        [{"$group": {"_id": "null", "fails_count": {"$sum": "$fail_count"}}}]
    )
    for document in documents:
        return document["fails_count"]
    
def file_max_runtime():
    max = 0 
    documents = collection.find({})
    for document in documents:
        if max < document["run_time"]:
            max = document["run_time"]
    return max

def file_avg_runtime():
    sum_runtime = 0 
    count_runtime = 0
    documents = collection.find({})
    for document in documents:
        sum_runtime += document["run_time"]
        count_runtime += 1
    return sum_runtime/count_runtime

def file_avg_simtime():
    sum_simtime = 0 
    count_simtime = 0
    documents = collection.find({})
    for document in documents:
        sum_simtime += document["sim_time"]
        count_simtime += 1
    return sum_simtime/count_simtime



def main():
    print("file_no_runs:", file_no_runs())
    print("file_no_errors:", file_no_errors())
    print("file_avg_runtime:", file_avg_runtime())
    print("file_avg_simtime:", file_avg_simtime())
    print("file_max_runtime:", file_max_runtime())

if __name__ == "__main__":
    main()
