import { createRouter, createWebHistory } from 'vue-router'
import Search from '@/components/Search.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Search,
    },
  ],
})

export default router
