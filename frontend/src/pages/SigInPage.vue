<template>
    <div class="siginpage">
            <Header_olimp/>
        <form @submit.prevent="handlerSubmit">
            <div class="table-sigin">
                <div class="logo-wrap">
                    <img 
                    src="../assets/academ.svg"
                    alt="" 
                    class="logo">
                </div>
                <div class="reg-Oauth">
                    <button class="yandex">
                        Войти через Яндекс 
                    </button>
                    <br>
                    <button class="google">
                        Войти через Google 
                    </button>
                </div>
                <p class="else">------ или ------</p>
                <div class="table-user-reg">
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="email"   v-model="user_data.username " placeholder="Почта">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input type="password" class="password"  v-model="user_data.password " placeholder="Пароль">
                    </div>
                    
                </div>
                <div class="button-res">
                    <button class="b-res" type="submit">Войти</button>
                </div>
                <p>Нет аккаунта ?</p>
                <div class="button-sigin">
                    <button class="b-res" @click="$router.push({ name: 'registration' })">Зарегистрироваться</button>
                </div>
            </div>
    </form>
    <Footer_olimp/>

</div>

</template>

<script>
import axios from 'axios';
import Header_olimp from '../components/Header_olimp.vue'
import Footer_olimp from '@/components/Footer_olimp.vue';

export default{
    components: {
        Header_olimp,
        Footer_olimp
    },

    data(){
        return{
            user_data:{
                username:'',
                password:'',
            }
        }
    }, 
    methods:{
        
        async handlerSubmit(){
            let axiosConfig = {
                withCredentials: true,
                headers: {
                    'Accept': '*/*'}
                }
            const params = new URLSearchParams()
            params.append('username', this.user_data.username,);
            params.append('password', this.user_data.password);
            const response = await axios.post('/lk/login',params,
                axiosConfig)
                console.log(response)
            this.$router.push({ name: 'cabinet' })
    }
    }
}

</script>


<style>
.siginpage{
    width: 100%;
    height: 100%;
    background-color: black;
}

/* .button-sigin{

} */
.table-sigin{
    background-color: rgb(219, 123, 13);

    justify-content: center;
    justify-items: baseline;
    align-content: center;
    flex-wrap: wrap;
    margin: 30%;
    border-radius: 3%;
    max-width: 27%

}
.reg-Oauth{
    display: grid;
    margin-top: 4.2%;
    align-content: stretch;
    justify-content: space-around;
    align-items: end;

}
.yandex{
    font-size: 20px;

}
.google{
    font-size: 20px;

}
.else{
    display: flex;
    margin-top: 4.2%;
    justify-content: center;
}
.table-user-reg{
    display: grid;
    margin-top: 4.2%;
    align-content: baseline;
    justify-content: center;
    align-items: flex-end;
}
.row-input{
    display: flex;
    align-items: stretch;
    flex-wrap: nowrap;
    margin-bottom: 10%;
    justify-content: center;
}
.svg-elem{
    width: 21px;
    height: 21px;
}
.button-res{
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
.b-res{
    height: 41px;
    width: 129px;
    color: #fafafa;
    background: linear-gradient(to top, #be8301, #ff4800);
    border: 2px solid #b43f11;
    background-color: #b43f11;
    border-radius: 5px;
}
</style>