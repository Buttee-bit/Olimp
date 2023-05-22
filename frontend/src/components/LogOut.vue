<template>
    <div class="logout-button">
        <button class="log-out"
        @click="LogOutClick()">
            Выйти
            
        </button>

    </div>

</template>

<script>
import axios from 'axios';
export default{
    name: 'LogOut',
    methods:{
        async LogOutClick(){
            let axiosConfig = {
                withCredentials: true,
                headers: {
                    'Accept': '*/*'}
                }
            const params = new URLSearchParams()
            const response = await axios.post('/lk/logout',params,
                axiosConfig)
                console.log(response)
            this.$router.push({ name: 'start' })
    }
    }
}

</script>

<style>
.log-out{
    height: 35px;
    width: 95px;
    color: #fafafa;
    background: linear-gradient(to top, #be8301, #ff4800);
    border: 2px solid #b43f11;
    background-color: #b43f11;
    border-radius: 7px;
}
</style>