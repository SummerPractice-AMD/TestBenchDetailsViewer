const dropArea = document.getElementById('drop-area');
const uploadBtn = document.getElementById('upload-btn');

dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.classList.add('dragover');
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('dragover');
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.classList.remove('dragover');

    const file = e.dataTransfer.files[0];
    uploadFile(file);
});

uploadBtn.addEventListener('click', () => {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.json';
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        uploadFile(file);
    });
    fileInput.click();
});

function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://localhost:5000/api/ingest', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
