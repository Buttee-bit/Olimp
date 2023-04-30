import { createRouter, createWebHistory } from "vue-router";

import HomePage from '../pages/HomePage'
import RegisterPage from '../pages/RegisterPage'
import SigInPage from '../pages/SigInPage'
import LCabinetPage from '../pages/LCabinetPage'


const routes =  [ {path : '/',name:'start', component : HomePage },
                {path : '/registration', name:'registration', component : RegisterPage },
                {path : '/sign', name:'sign', component : SigInPage },
                {path : '/cabinet', name:'cabinet', component: LCabinetPage},
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router