tailwind.config = {
  theme: {
      extend: {
          colors: {
              primary: '',
              accent: 'hsl(var(--accent) / <alpha-value>)',
          },
          fontFamily: {
              sans: ['Roboto', 'sans-serif'],
              serif: ['Robot Slab', 'serif'],
          },
      },
  },
}

const $ = document.querySelector.bind(document)
const $$ = document.querySelectorAll.bind(document)

const readAll = $('#read-all')

const bell = $('#bell')
const ctr = $('#ctr')
const ctrArticles = $('#ctr-articles')

bell.parentNode.onclick = () => {
  ctr.classList.toggle('scale-0')
  bell.classList.toggle('animate-bell')
}

// Buttons
// HTMLCollections are live lists
const accepts = document.getElementsByClassName('accept')
const declines = document.getElementsByClassName('decline')

// 👆 They make this function work because they are updated live!
function addButtonEvents() {
  for (let i = 0; i < accepts.length; i++) {
      const decline = declines[i]
      const accept = accepts[i]

      accept.onclick = () => {
          decline.remove()
          accept.classList.add('w-full', 'bg-green-300', 'text-black')
          accept.textContent = 'Accepted'
          setTimeout(() => {
              accept.remove()
          }, 2000)
      }

      decline.onclick = () => {
          accept.remove()
          decline.classList.add('w-full', 'bg-red-300')
          decline.textContent = 'Declined'
          setTimeout(() => {
              decline.remove()
          }, 2000)
      }
  }
}
addButtonEvents()

setTimeout(() => {
  const article = ` 
<article class="py-6 flex gap-4 border-b-2">
      <img class="rounded-full w-16 h-16 object-cover"
        src="https://xsgames.co/randomusers/assets/avatars/male/23.jpg" alt="">
      <div>
        <p class="mb-4">
          <span class="font-bold ">Joseph Teloti</span> shared the file <span
            class="font-bold">UI Assets</span> with you.
        </p>
        <p class=" text-gray-500 text-lg">Just now</p>
        <div>

          <button
            class="decline mt-5 w-[124px] max-w-full py-4 border border-accent/90 rounded-lg font-medium text-accent mr-2">Decline</button>

          <button
            class="accept w-[124px] max-w-full py-4 border border-accent/90 rounded-lg bg-accent text-white">Accept</button>
        </div>

      </div>
    </article>
`

  const newMessage = ` 
  <div id="new-message" class="text-center p-4 border-x-2 border-b-2 cursor-pointer bg-green-50">
      <p class="animate-pulse">
        1 new message
      </p>
    </div>
`

  $('#ctr-articles').insertAdjacentHTML('afterbegin', newMessage)

  $('#new-message').onclick = () => {
      console.log('clicked')
      $('#ctr-articles').insertAdjacentHTML('afterbegin', article)
      addButtonEvents()

      $('#new-message').remove()
  }
}, 6000)
