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
                    <button class="Ouath">
                        Войти с помощью  Яндекс 
                    </button>
                    <br>
                    <button class="Ouath">
                        Войти с помощью Google 
                    </button>
                </div>
                <p class="else">------ или ------</p>
                <div class="table-user-reg">
                    <div class="row-input_top">
                        <!-- <div class="svg-elem">
                            <img src="../assets/email-svgrepo-com.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"   v-model="user_data.username " placeholder="Почта">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="password" class="user-input"  v-model="user_data.password " placeholder="Пароль">
                    </div>
                    
                </div>
                <div class="last-wrap">
                    <div class="button-res">
                        <button class="b-res" type="submit">Войти</button>
                    </div>
                    <div class="else-no-acc">
                        <p>Еще нет аккаунта? </p>
                        <div class="div-text_last">
                            <p class="text-last" @click="$router.push({ name: 'registration' })"> Зарегистрироваться</p>
                        </div>
                    </div>
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
    width: 411px;
    height: 666px;
}
.logo-wrap{
    margin: 0px;
}

.reg-Oauth{
    display: flex;
    flex-direction: column;
    align-items: stretch;

}
.form-sigin{
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-top: 5%;
}

.Ouath{
    border-radius: 5px;
    border: 1px solid #3F3F46;
    background: #27272A;
    color: #D4D4D8;
    font-size: 14px;
    height: 40px
}
.else{
    display: flex;
    margin-top: 4.2%;
    justify-content: center;
}
.table-user-reg{
    display: flex;
    align-items: stretch;
    flex-direction: column;

}

.row-input_top{
    /* display: flex;
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
    border-left-style: solid; */


}
.row-input_button{

}
.user-input{
    
    /* border-radius: 5px 5px 0px 0px; */
    width: 100%;
    height: 40px;
    border-radius: 5px;
    border: 1px solid #3F3F46;
    background: #27272A;
    color: #D4D4D8;
    font-size: 14px;
    height: 40px;
    margin-bottom: 4.2%;
    text-align: center;
        
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
    height: 60px;
    color: #fafafa;
    border-radius: 5px;
    background: #BB432C;
    border: 2px solid #b43f11;
    background-color: #bb432c;
    border-radius: 5px;
    cursor: pointer;
    justify-content: space-around;
    /* align-content: center; */
    align-items: center;
    margin-top: 10px;
    text-align: center;
    font-family: Yandex Sans Display;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    padding: 11px 83px 11px 84px;
}
.last-wrap{
    display: flex;
    flex-direction: column;
}
.else-no-acc{
    display: flex;
    flex-direction: row;
}
.text-last{
    color: #C0C0C0;
    text-decoration-line: underline;
    color: #C0C0C0;

}
.else-no-acc{
    display: flex;
    flex-direction: row;
    align-items: stretch;
    justify-content: center;
    color: #C0C0C0;
}
.div-text_last{
    margin-left: 5px;
}
</style>