document.getElementById('toggle-password').addEventListener('click', function () {
    const passwordInput = document.getElementById('password-input');
    const icon = document.getElementById('toggle-icon');

    const isPassword = passwordInput.type === 'password';
    passwordInput.type = isPassword ? 'text' : 'password';

    // Fix icon toggle manually
    if (isPassword) {
        icon.classList.remove('fa-lock');
        icon.classList.add('fa-lock-open');
    } else {
        icon.classList.remove('fa-lock-open');
        icon.classList.add('fa-lock');
    }
});
