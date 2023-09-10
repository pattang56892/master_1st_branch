document.addEventListener('DOMContentLoaded', () => {
  const accept = document.querySelector('.accept');
  const decline = document.querySelector('.decline');
  const content1 = document.querySelector('.content-1');
  const list = document.querySelector('.list');
  const mark = document.querySelector('.mark');
  const close = document.querySelector('.close');
  const section = document.querySelector('section');

  accept.addEventListener('click', () => {
    const message = document.createElement('p');
    message.textContent = "You accepted the post. Check your timeline. 🚀";
    message.classList.add('text-sm', 'text-green-500', 'mt-4');
    content1.appendChild(message);

    const buttons = content1.querySelectorAll('button');
    buttons.forEach((button) => button.classList.add('hidden'));

    setTimeout(() => {
      message.remove();
    }, 2000);
  });

  decline.addEventListener('click', () => {
    const message = document.createElement('p');
    message.textContent = "You declined the post. 😔";
    message.classList.add('text-sm', 'text-red-500', 'mt-4');
    content1.appendChild(message);

    const buttons = content1.querySelectorAll('button');
    buttons.forEach((button) => button.classList.add('hidden'));

    setTimeout(() => {
      message.remove();
    }, 2000);
  });

  function newNotifications() {
    const notification = document.createElement('div');
    notification.classList.add('notification');

    const title = document.createElement('h2');
    title.textContent = 'New Notification';
    const message = document.createElement('p');
    message.textContent = 'This is a sample notification message.';

    notification.appendChild(title);
    notification.appendChild(message);

    list.appendChild(notification);

    setTimeout(() => {
      notification.remove();
    }, 5000);
  }

  setTimeout(newNotifications, 4000);

  mark.addEventListener('click', () => {
    list.innerHTML = '';
  });

  close.addEventListener('click', () => {
    section.classList.toggle('h-[0rem]');
    section.classList.toggle('py-10');
    section.classList.toggle('px-6');
  });
});
