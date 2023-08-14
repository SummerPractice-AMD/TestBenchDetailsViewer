



  document.addEventListener("DOMContentLoaded", function() {
    const summaryContainer = document.getElementById('tableGlobalSummary');
 
fetch("/api/global_summary")
  .then((response) => response.json())
  .then(data => { const globalSummary = data.global_summary;

           let indexHtml = '';
           indexHtml =`
            <tr>
             <th scope="col"  colspan="3">Global Summary</th>
           </tr>
           <tr>
            <th scope="row">No. Run</th>
             <td>${globalSummary.no_runs}</td>
           <td>/</td>  
           </tr>
           <tr>
           <th scope="col">No. Errors</th>
             <td>${globalSummary.no_errors}</td>
             <td>s</td>
           </tr>
           <tr>
             <th scope="row">Avg Runtime</th>
             <td>${globalSummary.avg_runtime}</td>
             <td>s</td>
           </tr>
           <tr>
             <th scope="row">Avg Sim Time</th>
             <td>${globalSummary.avg_sim_time.toFixed(2)}</td>
             <td>s</td>
           </tr>
           <tr>
             <th scope="row">Max Run Time</th>
             <td>${globalSummary.max_run_time}</td>
             <td>s</td>
           </tr>`;

    summaryContainer.innerHTML = indexHtml;
  })
      .catch(error => {
        console.error('An error occurred:', error);
      });
  });