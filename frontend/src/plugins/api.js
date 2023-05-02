import api from '../api/instance.js'
export default {
    install(Vue){
        Vue.prototype.$api = api
    }
}