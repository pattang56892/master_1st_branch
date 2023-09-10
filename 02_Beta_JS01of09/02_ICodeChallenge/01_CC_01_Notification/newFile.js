accept.addEventListener('click', () => {
  // Display a message to the user
  const message = document.createElement('p');
  message.textContent = "You accepted the post. Check your timeline. 🚀";
  message.classList.add('text-sm', 'text-green-500', 'mt-4');
  content1.appendChild(message);

  // Remove the "Accept" and "Decline" buttons
  const buttons = content1.querySelectorAll('button');
  buttons.forEach(button => button.classList.add('hidden'));

  // Automatically remove the message after 2 seconds
  setTimeout(() => {
    message.remove();
  }, 2000);
});
