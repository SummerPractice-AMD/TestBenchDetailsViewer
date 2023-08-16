const dropArea = document.getElementById('drop-area');
        const uploadButton = document.getElementById('upload-btn');

        dropArea.addEventListener('dragover', (event) => {
            event.preventDefault();
            dropArea.classList.add('dragover');
        });

        dropArea.addEventListener('dragleave', () => {
            dropArea.classList.remove('dragover');
        });

        dropArea.addEventListener('drop', (event) => {
            event.preventDefault();
            dropArea.classList.remove('dragover');
            
            const file = event.dataTransfer.files[0];
            uploadData(file);
        });

        uploadButton.addEventListener('click', () => {
            const fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.style.display = 'none';

            fileInput.addEventListener('change', (event) => {
                const file = event.target.files[0];
                uploadData(file);
            });

            document.body.appendChild(fileInput);
            fileInput.click();
            document.body.removeChild(fileInput);
        });

        function uploadData(file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('/api/ingest', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(result => {
                alert(result.message);
            })
            .catch(error => {
                alert('Error uploading and parsing data: ' + error);
            });
        }