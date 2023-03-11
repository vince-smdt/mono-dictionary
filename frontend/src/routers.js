import {createRouter, createWebHistory} from 'vue-router'
import LookupComponent from './components/LookupComponent'

const routes = [
    {
        path: '/',
        name: 'lookupComponent',
        component: LookupComponent
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router