from pymongo import MongoClient
import sys


class BDQueries:
    def __init__(self, connection_string, db_name, collection_name):
        self.cluster = MongoClient(connection_string)
        self.db = self.cluster[db_name]
        self.collection = self.db[collection_name]

    def file_no_runs(self):
        return self.collection.count_documents({})

    def file_no_errors(self):
        documents = self.collection.aggregate(
            [{"$group": {"_id": "null", "errors_count": {"$sum": "$errors"}}}]
        )
        return list(documents)[0]["errors_count"]

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

    # ----------------------------------------------------------------------------------------------

    def test_avg_runtime(self, testname):
        sum_runtime = 0
        count_runtime = 0
        documents = self.collection.find({"test_name": testname})
        for document in documents:
            sum_runtime += document["run_time"]
            count_runtime += 1
        return sum_runtime / count_runtime

    def test_avg_simtime(self, testname):
        sum_simtime = 0
        count_simtime = 0
        documents = self.collection.find({"test_name": testname})
        for document in documents:
            sum_simtime += document["sim_time"]
            count_simtime += 1
        return sum_simtime / count_simtime

    def test_max_runtime(self, testname):
        max = 0
        documents = self.collection.find({"test_name": testname})
        for document in documents:
            if max < document["run_time"]:
                max = document["run_time"]
        return max

    def test_min_runtime(self, testname):
        min = sys.maxsize
        documents = self.collection.find({"test_name": testname})
        for document in documents:
            if min > document["run_time"]:
                min = document["run_time"]
        return min

    def test_pass_rate(self, testname):
        sum_status = 0
        sum_pass = 0
        documents = self.collection.find({"test_name": testname})
        for document in documents:
            sum_status += 1
            if document["status"].lower() == "pass":
                sum_pass += 1

        return (sum_pass / sum_status) * 100

    def test_sum_run_time(self, testname):
        sum_runtime = 0
        documents = self.collection.find({"test_name": testname})
        for document in documents:
            sum_runtime += document["run_time"]
        return sum_runtime

    def test_last_status(self, testname):
        document = self.collection.aggregate(
            [{"$sort": {"_id": -1}}, {"$match": {"test_name": testname}}, {"$limit": 1}]
        )
        return list(document)[0]["status"]

    # ----------------------------------------------------------------------------------

    def execution_details_status(self, filename, testname):
        documents = self.collection.find({"run_id": filename, "test_name": testname})
        return list(documents)[0]["status"]

    def execution_details(self, filename, testname):
        documents = self.collection.find({"run_id": filename, "test_name": testname})
        return list(documents)[0]["loglines"]

    def execution_details_run_id(self, testname):
        documents = self.collection.find({"test_name": testname})
        return list(documents)[0]["run_id"]

    def execution_details_status_run_id(self, testname):
        documents = self.collection.find({"test_name": testname})
        return list(documents)[0]["status"]

    def execution_details_logline_run_id(self, testname):
        documents = self.collection.find({"test_name": testname})
        return list(documents)[0]["loglines"]

    # ---------------------------------------------------------------------------------

    def get_run_ids(self):
        documents = self.collection.find({})
        run_ids = []
        for document in documents:
            if document["run_id"] not in run_ids:
                run_ids.append(document["run_id"])
        return run_ids

    def get_test_names(self):
        documents = self.collection.find({})
        test_names = []
        for document in documents:
            if document["test_name"] not in test_names:
                test_names.append(document["test_name"])
        return test_names


def main():
    query_testruns = BDQueries("mongodb://localhost:27017", "RegressionDetails", "testruns")
    print("file_no_runs:", query_testruns.file_no_runs())
    print("file_no_errors:", query_testruns.file_no_errors())
    print("file_avg_runtime:", query_testruns.file_avg_runtime())
    print("file_avg_simtime:", query_testruns.file_avg_simtime())
    print("file_max_runtime:", query_testruns.file_max_runtime())

    query_tests = BDQueries("mongodb://localhost:27017", "RegressionDetails", "tests")
    print("test_avg_runtime:", query_tests.test_avg_runtime("run_test_004"))
    print("test_avg_simtime:", query_tests.test_avg_simtime("run_test_004"))
    print("test_max_runtime:", query_tests.test_max_runtime("run_test_004"))
    print("test_min_runtime:", query_tests.test_min_runtime("run_test_004"))
    print("test_pass_rate:", query_tests.test_pass_rate("run_test_004"))
    print("execution_details_status:", query_tests.execution_details_status("1", "run_test_004"),)
    print("execution_details:", query_tests.execution_details("1", "run_test_004"))
    print("execution_details_run_id:", query_tests.execution_details_run_id("run_test_004"))
    print("get_run_ids:", query_tests.get_run_ids())
    print("get_test_names:", query_tests.get_test_names())
    print("test_sum_run_time:", query_tests.test_sum_run_time("run_test_004"))
    print("test_last_status:", query_tests.test_last_status("run_test_005"))


if __name__ == "__main__":
    main()
