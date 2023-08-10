from flask import Flask, jsonify, render_template
from bdqueries import BDQueries

app = Flask(__name__, template_folder='Templates')

@app.route('/api/run_ids', methods=['GET'])
def get_run_ids():
    bd_queries = BDQueries("mongodb://localhost:27017", "RegressionDetails", "tests")
    run_ids = bd_queries.get_run_ids()
    return jsonify({"run_ids": [{"run_name": run_id} for run_id in run_ids]})

@app.route('/api/test_names', methods=['GET'])
def get_test_names():
    bd_queries = BDQueries("mongodb://localhost:27017", "RegressionDetails", "tests")
    test_names = bd_queries.get_test_names()
    return jsonify({"test_names": [{"name": test_name} for test_name in test_names]})

@app.route('/api/test_details/<test_name>', methods=['GET'])
def get_test_details(test_name):
    bd_queries = BDQueries("mongodb://localhost:27017", "RegressionDetails", "tests")
    pass_rate = bd_queries.test_pass_rate(test_name)
    avg_run_time = bd_queries.test_avg_runtime(test_name)
    max_run_time = bd_queries.test_max_runtime(test_name)
    min_run_time = bd_queries.test_min_runtime(test_name)
    avg_sim_time = bd_queries.test_avg_simtime(test_name)

    if pass_rate is None or avg_run_time is None or max_run_time is None or min_run_time is None or avg_sim_time is None:
        return jsonify({"error": "Test details not found"}), 404

    test_details = {
        "pass_rate": pass_rate,
        "avg_run_time": avg_run_time,
        "max_run_time": max_run_time,
        "min_run_time": min_run_time,
        "avg_sim_time": avg_sim_time
    }

    return jsonify({"test_details": test_details})

@app.route('/api/execution_details/<run_id>/<test_name>', methods=['GET'])
def get_execution_details(run_id, test_name):
    bd_queries = BDQueries("mongodb://localhost:27017", "RegressionDetails", "tests")
    execution_details = bd_queries.execution_details(run_id, test_name)
    execution_status = bd_queries.execution_details_status(run_id, test_name)

    if not execution_details or not execution_status:
        return jsonify({"error": "Execution details not found"}), 404

    return jsonify({
        "execution_details": {
            "testname": test_name,
            "status": execution_status,
            "logline": execution_details
        }
    })

@app.route('/api/global_summary', methods=['GET'])
def get_global_summary():
    bd_queries = BDQueries("mongodb://localhost:27017", "RegressionDetails", "testruns")
    no_runs = bd_queries.file_no_runs()
    no_errors = bd_queries.file_no_errors()
    avg_runtime = bd_queries.file_avg_runtime()
    avg_sim_time = bd_queries.file_avg_simtime()
    max_run_time = bd_queries.file_max_runtime()

    if not all([no_runs, no_errors, avg_runtime, avg_sim_time, max_run_time]):
        return jsonify({"error": "Global summary not found"}), 404

    global_summary = {
        "no_runs": no_runs,
        "no_errors": no_errors,
        "avg_runtime": avg_runtime,
        "avg_sim_time": avg_sim_time,
        "max_run_time": max_run_time
    }

    return jsonify({"global_summary": global_summary})



@app.route('/')
def index():
        return render_template("index.html")

@app.route('/testdetails.html')
def testdetails():
        return render_template("testdetails.html")

@app.route('/executiondetails.html')
def executiondetails():
        return render_template("executiondetails.html")


if __name__ == '__main__':
    app.run(debug=True)
