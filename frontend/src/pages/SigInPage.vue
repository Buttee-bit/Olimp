<template>
    <div class="siginpage">
            <Header_olimp/>
        <form class='form-sigin' @submit.prevent="handlerSubmit">
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
                    <div class="row-input_top">
                        <div class="svg-elem">
                            <img src="../assets/email-svgrepo-com.svg" alt="" class="svg">
                        </div>
                        <input  type="text" class="user-input"   v-model="user_data.username " placeholder="Почта">
                    </div>
                    <div class="row-input_button">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input  type="password" class="user-input"  v-model="user_data.password " placeholder="Пароль">
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


<style scoped>
.siginpage{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}

/* .button-sigin{

} */
.table-sigin{
    background-color: #222327;
    justify-content: center;
    justify-items: baseline;
    align-content: center;
    flex-wrap: wrap;
    /* margin: 30%; */
    border-radius: 0.5rem!important;
    /* max-width: 50%; */
    padding: 40px;
    max-width: 310px;
    min-width: 310px;
}
.logo-wrap{
    margin: 0px;
}

.reg-Oauth{
    display: grid;
    margin-top: 4.2%;
    align-content: stretch;
    justify-content: space-around;
    align-items: end;

}
.form-sigin{
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-top: 5%;
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
    display: flex;
    margin-top: 4.2%;
    align-content: stretch;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
    /* width: 70%; */

}

.row-input_top{
    display: flex;
    /* margin-bottom: 10%; */
    background: rgb(39, 39, 42);
    padding: 5px;
    border-radius: 5px 5px 0px 0px;
    width: 80%;
    height: 20px;
    flex-direction: row;
    justify-content: flex-start;
    align-items: stretch;
    border-top-color:  rgb(63, 63, 70);
    border-top-style: solid;
    border-right-color:  rgb(63, 63, 70);
    border-right-style: solid;
    border-left-color:  rgb(63, 63, 70);
    border-left-style: solid;

    /* border-color: #008a77; */ 
    /* border-style: solid; */
}
.row-input_button{
    display: flex;
    /* margin-bottom: 10%; */
    background: rgb(39, 39, 42);
    padding: 5px;
    border-radius: 0px 0px 5px 5px;
    width: 80%;
    height: 20px;
    flex-direction: row;
    justify-content: flex-start;
    align-items: stretch;
    border-top-color:  rgb(63, 63, 70);
    border-top-style: solid;
    border-bottom-color:  rgb(63, 63, 70);
    border-bottom-style: solid;
    border-right-color:  rgb(63, 63, 70);
    border-right-style: solid;
    border-left-color:  rgb(63, 63, 70);
    border-left-style: solid;
}
.user-input{
    color: #efefef;
    background: rgb(39, 39, 42);
    padding: 0px;
    background: rgb(39, 39, 42);
    border-radius: -7px;
    border: 0;
    width: 100%;
}
.button-res{
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
.b-res{
    display: flex;
    width: 100%;
    height: 31px;
    color: #fafafa;
    background: linear-gradient(to top, #bb432c, #ff4800);
    border: 2px solid #b43f11;
    background-color: #bb432c;
    border-radius: 5px;
    cursor: pointer;
    justify-content: space-around;
    /* align-content: center; */
    align-items: center;
    margin-top: 10px;
}
</style>