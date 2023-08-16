document.addEventListener("DOMContentLoaded", function() {
    const summaryContainer = document.getElementById('tableGlobalSummary');
 
fetch("/api/global_summary")
  .then((response) => response.json())
  .then(data => { const globalSummary = data.global_summary;

           let indexHtml = '';
           indexHtml =`
           <tr>
            <th scope="row">Number of Runs</th>
             <td>${globalSummary.no_runs}</td>  
           </tr>
           <tr>
           <th scope="row">Number of Errors</th>
             <td>${globalSummary.no_errors}</td>
           </tr>
           <tr>
             <th scope="row">Average Run time</th>
             <td>${globalSummary.avg_runtime.toFixed(2)} s</td>
           </tr>
           <tr>
             <th scope="row">Average Sim Time</th>
             <td>${(globalSummary.avg_sim_time / 1000000000).toFixed(2)} s</td>
           </tr>
           <tr>
             <th scope="row">Maximum Run Time</th>
             <td>${globalSummary.max_run_time} s</td>
           </tr>`;

    summaryContainer.innerHTML = indexHtml;
  })
      .catch(error => {
        console.error('An error occurred:', error);
      });
  });

 