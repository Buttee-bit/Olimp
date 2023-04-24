import { createRouter, createWebHistory } from "vue-router";

import RegisterPage from '../pages/RegisterPage'
import HomePage from '../pages/HomePage'

const routes =  [ {path : '/',name:'start', component : HomePage },
                {path : '/registration', name:'registration', component : RegisterPage },
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router