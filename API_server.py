from flask import Flask, jsonify
from bdqueries import BDQueries
import yaml

app = Flask(__name__)


@app.route("/api/run_ids", methods=["GET"])
def get_run_ids():
    run_ids = bd_queries_tests.get_run_ids()
    return jsonify({"run_ids": [{"run_name": run_id} for run_id in run_ids]})


@app.route("/api/test_names", methods=["GET"])
def get_test_names():
    test_names = bd_queries_tests.get_test_names()
    return jsonify({"test_names": [{"name": test_name} for test_name in test_names]})


@app.route("/api/test_details/<test_name>", methods=["GET"])
def get_test_details(test_name):
    pass_rate = bd_queries_tests.test_pass_rate(test_name)
    avg_run_time = bd_queries_tests.test_avg_runtime(test_name)
    max_run_time = bd_queries_tests.test_max_runtime(test_name)
    min_run_time = bd_queries_tests.test_min_runtime(test_name)
    avg_sim_time = bd_queries_tests.test_avg_simtime(test_name)

    if (
        pass_rate is None
        or avg_run_time is None
        or max_run_time is None
        or min_run_time is None
        or avg_sim_time is None
    ):
        return jsonify({"error": "Test details not found"}), 404

    test_details = {
        "pass_rate": pass_rate,
        "avg_run_time": avg_run_time,
        "max_run_time": max_run_time,
        "min_run_time": min_run_time,
        "avg_sim_time": avg_sim_time,
    }

    return jsonify({"test_details": test_details})


@app.route("/api/execution_details/<run_id>/<test_name>", methods=["GET"])
def get_execution_details(run_id, test_name):
    execution_details = bd_queries_tests.execution_details(run_id, test_name)
    execution_status = bd_queries_tests.execution_details_status(run_id, test_name)

    if not execution_details or not execution_status:
        return jsonify({"error": "Execution details not found"}), 404

    return jsonify(
        {
            "execution_details": {
                "testname": test_name,
                "status": execution_status,
                "logline": execution_details,
            }
        }
    )


@app.route("/api/global_summary", methods=["GET"])
def get_global_summary():
    no_runs = bd_queries_testruns.file_no_runs()
    no_errors = bd_queries_testruns.file_no_errors()
    avg_runtime = bd_queries_testruns.file_avg_runtime()
    avg_sim_time = bd_queries_testruns.file_avg_simtime()
    max_run_time = bd_queries_testruns.file_max_runtime()

    if not all([no_runs, no_errors, avg_runtime, avg_sim_time, max_run_time]):
        return jsonify({"error": "Global summary not found"}), 404

    global_summary = {
        "no_runs": no_runs,
        "no_errors": no_errors,
        "avg_runtime": avg_runtime,
        "avg_sim_time": avg_sim_time,
        "max_run_time": max_run_time,
    }

    return jsonify({"global_summary": global_summary})


if __name__ == "__main__":
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)

    database_host = config["regression_details"]["database_host"]
    database_port = config["regression_details"]["database_port"]
    database_name = config["regression_details"]["database_name"]

    connection_string = "mongodb://" + database_host + ":" + str(database_port)

    tests_table_name = "tests"
    testruns_table_name = "testruns"

    bd_queries_tests = BDQueries(connection_string, database_name, tests_table_name)
    bd_queries_testruns = BDQueries(connection_string, database_name, testruns_table_name)

    app.run(debug=True)
