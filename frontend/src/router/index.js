import { createRouter, createWebHistory } from "vue-router";

import HomePage from '../pages/HomePage'
import RegisterPage from '../pages/RegisterPage'
import SigInPage from '../pages/SigInPage'
import LCabinetPage from '../pages/LCabinetPage'
import TaskPage from '../pages/TaskPage'


const routes =  [ {path : '/',name:'start', component : HomePage },
                {path : '/registration', name:'registration', component : RegisterPage },
                {path : '/sign', name:'sign', component : SigInPage },
                {path : '/cabinet', name:'cabinet', component: LCabinetPage},
                {path:'/task', name:'olimpiad', component:TaskPage},
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router