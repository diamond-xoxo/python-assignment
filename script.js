document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    
    // Check if the user previously saved a theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        toggleBtn.textContent = '☀️ Switch to Light Mode';
    }

    // Toggle button click logic
    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        
        if (isDark) {
            localStorage.setItem('theme', 'dark');
            toggleBtn.textContent = '☀️ Switch to Light Mode';
        } else {
            localStorage.setItem('theme', 'light');
            toggleBtn.textContent = '🌙 Switch to Dark Mode';
        }
    });
});
