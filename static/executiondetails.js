fetch('/api/run_ids')
    .then(response => response.json())
    .then(data => {
        const runIdSelect = document.getElementById('comboBoxRunId');

        // Sort the run_ids numerically by run_name
        const sortedRunIds = data.run_ids.slice().sort((a, b) => a.run_name - b.run_name);

        sortedRunIds.forEach(run => {
            const option = document.createElement('option');
            option.value = run.run_name;
            option.textContent = run.run_name;
            runIdSelect.appendChild(option);
        });
    })
    .catch(error => {
        console.error('Error fetching or parsing JSON:', error);
    });


fetch('/api/test_names')
    .then(response => response.json())
    .then(data => {
        const testNameSelect = document.getElementById('comboBoxTestNames');

        data.test_names.forEach(test => {
            const option = document.createElement('option');
            option.value = test.name;
            option.textContent = test.name;
            testNameSelect.appendChild(option);
        });
    })
    .catch(error => {
        console.error('Error fetching or parsing JSON:', error);
    });


document.addEventListener('DOMContentLoaded', () => {
    const runIdSelect = document.getElementById('comboBoxRunId');
    const testNameSelect = document.getElementById('comboBoxTestNames');
    const executionDetailsDiv = document.getElementById('log_lineItem');
    const inputPassOrFail = document.getElementById('statusInput');
    inputPassOrFail.background="";
    inputPassOrFail.value="";

    function changeColor() {
        const inputPassOrFail = document.getElementById('statusInput');

        if (inputPassOrFail.value === "PASS") {
            inputPassOrFail.style.background = "green";
            inputPassOrFail.style.color = "white";
        } else if (inputPassOrFail.value === "FAIL") {
            inputPassOrFail.style.background = "red";
            inputPassOrFail.style.color = "black";
        } else {
            inputPassOrFail.style.background = ""; // Reset color
        }
    }

    testNameSelect.addEventListener('change', () => {
        const selectedRunId = runIdSelect.value;
        const selectedTestName = testNameSelect.value;
        if (selectedRunId == null || selectedRunId == "Select run_id" ||
            selectedTestName == null || selectedTestName == "Select test name") {
            console.log('Items not selected!')
        }
        else {
            fetch(`/api/execution_details/${selectedRunId}/${selectedTestName}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        executionDetailsDiv.textContent = 'Execution details not found';
                    } else {
                        const executionDetails = data.execution_details;
                        inputPassOrFail.value = executionDetails.status;
                        // Change the color based on the value
                        changeColor();
                        const logLines = executionDetails.logline.split('\n');
                        executionDetailsDiv.innerHTML = logLines
                            .map(line => `<p>${line}</p>`)
                            .join('');
                    }
                })
                .catch(error => console.error('Error fetching execution details:', error));
        }
    });

    runIdSelect.addEventListener('change', () => {
        const selectedRunId = runIdSelect.value;
        const selectedTestName = testNameSelect.value;
        if (selectedRunId == null || selectedRunId == "Select run_id" ||
            selectedTestName == null || selectedTestName == "Select test name") {
            console.log('Items not selected!')
        }
        else {
            fetch(`/api/execution_details/${selectedRunId}/${selectedTestName}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        executionDetailsDiv.textContent = 'Execution details not found';
                    } else {
                        const executionDetails = data.execution_details;
                        inputPassOrFail.value = executionDetails.status;
                        // Change the color based on the value
                        changeColor();
                        const logLines = executionDetails.logline.split('\n');
                        executionDetailsDiv.innerHTML = logLines
                            .map(line => `<p>${line}</p>`)
                            .join('');
                    }
                })
                .catch(error => console.error('Error fetching execution details:', error));
        }
    });
});




