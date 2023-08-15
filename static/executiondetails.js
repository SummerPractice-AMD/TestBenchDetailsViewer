



fetch('/api/run_ids')
   .then(response => response.json())
   .then(data => {
       const runIdSelect = document.getElementById('comboBoxRunId');


       
       data.run_ids.forEach(run => {
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
        const testNameSelectAlone = document.getElementById('comboBoxTestNames');
        const executionDetailsDiv = document.getElementById('log_lineItem');
        const inputPassOrFail = document.getElementById('statusInput');
      
        
      function changeColor() {
        const inputPassOrFail = document.getElementById('statusInput');
        
        if (inputPassOrFail.value === "PASS") {
            inputPassOrFail.style.background="green";
        } else if (inputPassOrFail.value === "FAIL") {
            inputPassOrFail.style.background = "red";
        } else {
            inputPassOrFail.style.background = ""; // Reset color
        }
    }
    changeColor();
testNameSelect.addEventListener('change', () => {
    const selectedRunId = runIdSelect.value;
    const selectedTestName = testNameSelect.value;
    if(selectedRunId == null){
     console.log('Run id not selected!')}
    else{
     fetch(`/api/execution_details/${selectedRunId}/${selectedTestName}`)
       .then(response => response.json())
       .then(data => {
           if (data.error) {
               executionDetailsDiv.textContent = 'Execution details not found';
           } else {
               const executionDetails = data.execution_details;
               inputPassOrFail.value = executionDetails.status;
               changeColor();
               executionDetailsDiv.innerHTML = `
                   <p> ${executionDetails.logline}</p>
    
               `;
           }
       })
       .catch(error => console.error('Error fetching execution details:', error));
    }
    
    
    });
    
    testNameSelectAlone.addEventListener('change', () => {
    const selectedTestNameAlone = testNameSelectAlone.value;
    
     fetch(`/api/execution_details/${selectedTestNameAlone}`)
       .then(response => response.json())
       .then(data => {
           if (data.error) {
               executionDetailsDiv.textContent = 'Execution details not found';
           } else {
               const executionDetails = data.execution_details;
               inputPassOrFail.value = executionDetails.status;
               runIdSelect.value = executionDetails.run_id;
               executionDetailsDiv.innerHTML = `
                   <p> ${executionDetails.logline}</p>
               changeColor();
               `;
           }
       })
       .catch(error => console.error('Error fetching execution details:', error));
    
    
    
    });
    
      }); 



