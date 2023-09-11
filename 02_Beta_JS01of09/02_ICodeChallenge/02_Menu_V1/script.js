document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector('.menu-button');
  const submenu = document.querySelector('.submenu');
  const tabs = document.querySelectorAll('.tab');

  // Initially hide the submenu
  submenu.style.display = 'none';

  menuButton.addEventListener('click', () => {
    // Toggle the visibility of the submenu
    if (submenu.style.display === 'none' || submenu.style.display === '') {
      submenu.style.display = 'block';
    } else {
      submenu.style.display = 'none';
    }

    // Toggle the 'hidden' class on tabs
    tabs.forEach(tab => {
      tab.classList.toggle('hidden');
    });
  });
});


