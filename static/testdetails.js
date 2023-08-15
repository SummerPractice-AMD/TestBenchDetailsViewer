  document.addEventListener('DOMContentLoaded', () => {
   
    
  fetch('/api/test_names')
  .then(response => response.json())
  .then(data => {
    const testNameSelect = document.getElementById('comboBox');
      const test = data.test_names
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


     const testNameSelectItem = document.getElementById('comboBox');
     const testDetailsDiv = document.getElementById('testDetails');

    testNameSelectItem.addEventListener('change', () => {
    const selectedTestName = testNameSelectItem.value;

      fetch(`/api/test_details/${selectedTestName}`)
      .then(response => response.json())
      .then(data => { 
          if (data.error) {
              testDetailsDiv.textContent = 'Test details not found';
          } else {
              const testDetails = data.test_details;
              testDetailsDiv.innerHTML =`
              <tr>
              <th scope="row">Pass Rate</th>
              <td>${testDetails.pass_rate.toFixed(2)} %</td>
              </tr>
              <tr>
              <th scope="col">Average Run Time</th>
              <td>${testDetails.avg_run_time.toFixed(2)} s</td>
              </tr>
              <tr>
              <th scope="row">Max Run Time</th>
              <td>${testDetails.max_run_time.toFixed(2)} s</td>
              </tr>
              <tr>
              <th scope="row">Min Run Time</th>
              <td>${testDetails.min_run_time.toFixed(2)} s</td>
              </tr>
              <tr>
              <th scope="row">Average Sim Time</th>
              <td>${testDetails.avg_sim_time.toFixed(2)} s</td>
              </tr>
              <tr>
              <th scope="row">Summation run time</th>
              <td>${testDetails.sum_run_time.toFixed(2)} s</td>
              </tr>
              `;
          }
      })
      .catch(error => console.error('Error fetching test details:', error));
   });

  });