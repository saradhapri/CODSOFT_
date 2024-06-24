document.getElementById('passwordForm').addEventListener('submit', function(event) {
    var length = document.getElementById('length').value;
    if (length < 1) {
        alert('Password length must be at least 1');
        event.preventDefault();
    }
});

function copyToClipboard() {
    var copyText = document.getElementById('generatedPassword').innerText;
    navigator.clipboard.writeText(copyText).then(function() {
        alert('Password copied to clipboard!');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}
