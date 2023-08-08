from pymongo import MongoClient


class BDQueries:
    def __init__(self, connection_string, db_name, collection_name):
        self.cluster = MongoClient(connection_string)
        self.db = self.cluster[db_name]
        self.collection = self.db[collection_name]

    def file_no_runs(self):
        return self.collection.count_documents({})

    def file_no_errors(self):
        documents = self.collection.aggregate(
            [{"$group": {"_id": "null", "fails_count": {"$sum": "$fail_count"}}}]
        )
        return list(documents)[0]["fails_count"]

    def file_max_runtime(self):
        max = 0
        documents = self.collection.find({})
        for document in documents:
            if max < document["run_time"]:
                max = document["run_time"]
        return max

    def file_avg_runtime(self):
        sum_runtime = 0
        count_runtime = 0
        documents = self.collection.find({})
        for document in documents:
            sum_runtime += document["run_time"]
            count_runtime += 1
        return sum_runtime / count_runtime

    def file_avg_simtime(self):
        sum_simtime = 0
        count_simtime = 0
        documents = self.collection.find({})
        for document in documents:
            sum_simtime += document["sim_time"]
            count_simtime += 1
        return sum_simtime / count_simtime


def main():
    query = BDQueries("mongodb://localhost:27017", "RegressionDetails", "testruns")
    print("file_no_runs:", query.file_no_runs())
    print("file_no_errors:", query.file_no_errors())
    print("file_avg_runtime:", query.file_avg_runtime())
    print("file_avg_simtime:", query.file_avg_simtime())
    print("file_max_runtime:", query.file_max_runtime())


if __name__ == "__main__":
    main()
