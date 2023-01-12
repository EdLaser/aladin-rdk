import { createRouter, createWebHistory } from 'vue-router'
import MainAppComponent from '../components/MainAppComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: MainAppComponent
    }
  ]
})

export default router
