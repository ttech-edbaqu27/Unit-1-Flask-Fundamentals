document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function() {
            const button = form.querySelector('button');
            button.textContent = 'Processing...';
            button.disabled = true;
        });
    }
});