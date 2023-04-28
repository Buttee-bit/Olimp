import { createRouter, createWebHistory } from "vue-router";

import HomePage from '../pages/HomePage'
import RegisterPage from '../pages/RegisterPage'
import SigInPage from '../pages/SigInPage'

const routes =  [ {path : '/',name:'start', component : HomePage },
                {path : '/registration', name:'registration', component : RegisterPage },
                {path : '/registration', name:'sign', component : SigInPage }
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router