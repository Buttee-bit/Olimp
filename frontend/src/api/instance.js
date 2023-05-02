import axios from 'axios'

const instance = axios.create({
    baseURL:'http://localhost:8000/' // вставьте свой url
})
export default instance