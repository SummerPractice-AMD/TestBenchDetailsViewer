var pass_ratesList
fetch('/api/pass_rates')
    .then(response => response.json())
    .then(data => {
        loadPassRatesTable(data.pass_rates);
        pass_ratesList = data.pass_rates;
    }
    );

function loadPassRatesTable(tests) {
    const tableBody = document.getElementById('passRatesTable');
    let dataHtml = '';

    for (let test of tests) {
        testname = test['testname']
        last_status = test['last_status']
        pass_rate = test['pass_rate']
        dataHtml += `<tr><td>${testname}</td><td>${last_status}</td><td>${pass_rate}</td></tr>`;
    }

    tableBody.innerHTML = dataHtml
}

let sortDirection = false;

function sortColumn(columnName) {

    const dataType = typeof pass_ratesList[0][columnName];
    sortDirection = !sortDirection;

    switch (dataType) {
        case 'number':
            sortNumberColumn(sortDirection, columnName);
            break;
    }

    loadPassRatesTable(pass_ratesList)
}

function sortNumberColumn(sort, columnName) {
    pass_ratesList = pass_ratesList.sort((p1, p2) => {
        return sort ? p1[columnName] - p2[columnName] : p2[columnName] - p1[columnName]
    });
}
