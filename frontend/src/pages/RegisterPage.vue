<!-- <template>
    <Header_olimp/>

    <div class="register-page">
        <form @submit.prevent="registerButton">
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
                        <input type="text" class="email"   v-model="user_data.email " placeholder="Почта">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input type="password" class="password"  v-model="user_data.password " placeholder="Пароль">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="f_name"  v-model="user_data.f_name " placeholder="Фамилия">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="Second_name"   v-model="user_data.Second_name " placeholder="Имя">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="Last_name"   v-model="user_data.Last_name " placeholder="Отчество">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/city.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="City"   v-model="user_data.City " placeholder="Город">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/school.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="School"   v-model="user_data.School " placeholder="Школа">
                    </div>
                    <div class="row-input">
                        <div class="svg-elem">
                            <img src="../assets/class_.svg" alt="" class="svg">
                        </div>
                        <input type="text" class="Class_"   v-model="user_data.Class_ " placeholder="Класс">
                    </div>
                </div>
                <div class="button-res">
                    <button class="b-res" type="submit">Зарегистрироваться</button>
                </div>
                <div class="alternative">
                    <p>Уже есть аккаунт?</p>
                    <div class="button-alternative">
                        <div class="button-alternative" @click="$router.push({ name: 'sign' })">Войти</div>
                    </div>
                </div>
                
            </div>
        </form>
    </div>
<Footer_olimp/>

</template> -->
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
                <div class="else">
                    <hr color="#3F3F46" width=40%  height= "1px" >
                    ИЛИ
                    <hr color="#3F3F46" width=40%  height= "1px"  >
                    </div>
                <div class="table-user-reg">
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"  v-model="user_data.password " placeholder="Почта">
                    </div>
                    <div class="row-input_top">
                        <!-- <div class="svg-elem">
                            <img src="../assets/email-svgrepo-com.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"   v-model="user_data.username " placeholder="Пароль">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="password" class="user-input"  v-model="user_data.password " placeholder="Фамилия">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"  v-model="user_data.password " placeholder="Имя">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"  v-model="user_data.password " placeholder="Отчество">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"  v-model="user_data.password " placeholder="Город">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"  v-model="user_data.password " placeholder="Школа">
                    </div>
                    <div class="row-input_button">
                        <!-- <div class="svg-elem">
                            <img src="../assets/user_svg.svg" alt="" class="svg">
                        </div> -->
                        <input  type="text" class="user-input"  v-model="user_data.password " placeholder="Класс">
                    </div>
                    
                </div>
                <div class="last-wrap">
                    <div class="button-res">
                        <button class="b-res" type="submit">Зарегистрироваться</button>
                    </div>
                    <div class="else-no-acc">
                        <p>Уже есть аккаунт? </p>
                        <div class="div-text_last">
                            <p class="text-last" @click="$router.push({ name: 'sign' })"> Войти</p>
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

        // logo_olimp,
        // Footer_olimp
    },
data(){
    return{
        user_data:{
            email:'',
            password:'',
            f_name:'',
            Second_name:'',
            Last_name:'',
            City:'',
            School:'',
            Class_:'',
            is_admin: null
        }
    }
}, 
methods:{
    async registerButton(){

        const response = await axios.post('/lk/register',{
            email: this.user_data.email,
            password: this.user_data.password,
            name: this.user_data.f_name + ' ' + this.user_data.Second_name + ' ' + this.user_data.Last_name,
            city: this.user_data.City,
            School: this.user_data.School,
            class_: this.user_data.Class_,
            role_id: 1
        });
        console.log(response)
        this.$router.push({ name: 'sign' })
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

.table-sigin{
    background-color: #222327;
    justify-content: center;
    justify-items: baseline;
    align-content: center;
    flex-wrap: wrap;
    border-radius: 0.5rem!important;
    padding: 40px;
    width: 436px;
    height: 940px;
}
.logo-wrap{
    margin-bottom: 25px;
    margin-top: 40px;
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
    flex-direction: row;
    margin-top: 4.2%;
    justify-content: center;
    color: #5F5F66;
    text-align: center;
    font-family: IBM Plex Serif;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    align-items: flex-start;
    margin-bottom: 15px;
}

.table-user-reg{
    display: flex;
    align-items: stretch;
    flex-direction: column;

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
    margin-bottom: 2.2%;
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