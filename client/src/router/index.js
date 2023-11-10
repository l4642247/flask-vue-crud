import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
  ]
})

export default router