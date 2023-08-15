import pymongo


class DatabaseLoader:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        self.tests_collection = self.db["tests"]
        self.testruns_collection = self.db["testruns"]

# introducere in baza de date a unui singur file
    def load_from_json(self, json_data):
        data = json_data

        run_id = data["filename"]

        testruns_data = {
            "run_id": run_id,
            "run_time": data["realtimefile"],
            "sim_time": data["simtimefile"],
            "errors": data["errors"]
        }
        self.testruns_collection.insert_one(testruns_data)

        for test in data["tests"]:
            test_data = {
                "run_id": run_id,
                "test_name": test["testname"],
                "status": test["status"],
                "run_time": test["realtime"],
                "sim_time": test["simtime"],
                "loglines": test["logline"]
            }
            self.tests_collection.insert_one(test_data)

# introducere in baza de date a unei liste de file-uri
    def load_from_json_list(self, json_data):
        data_list = json_data       
        for data in data_list:
            run_id = data["filename"]

            testruns_data = {
                "run_id": run_id,
                "run_time": data["realtimefile"],
                "sim_time": data["simtimefile"],
                "errors": data["errors"]
                }
            self.testruns_collection.insert_one(testruns_data)

            for test in data["tests"]:
                test_data = {
                    "run_id": run_id,
                    "test_name": test["testname"],
                    "status": test["status"],
                    "run_time": test["realtime"],
                    "sim_time": test["simtime"],
                    "loglines": test["logline"]
                    }
                self.tests_collection.insert_one(test_data)
