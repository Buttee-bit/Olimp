<template>
    <div class="register-page">
        <Header_olimp/>
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
                    <input type="text" class="email"   v-model="user_data.email " placeholder="email">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/user_svg.svg" alt="" class="svg">
                    </div>
                    <input type="password" class="password"  v-model="user_data.password " placeholder="password">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/user_svg.svg" alt="" class="svg">
                    </div>
                    <input type="text" class="f_name"  v-model="user_data.f_name " placeholder="f_name">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/user_svg.svg" alt="" class="svg">
                    </div>
                    <input type="text" class="Second_name"   v-model="user_data.Second_name " placeholder="Second_name">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/user_svg.svg" alt="" class="svg">
                    </div>
                    <input type="text" class="Last_name"   v-model="user_data.Last_name " placeholder="Last_name">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/city.svg" alt="" class="svg">
                    </div>
                    <input type="text" class="City"   v-model="user_data.City " placeholder="City">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/school.svg" alt="" class="svg">
                    </div>
                    <input type="text" class="School"   v-model="user_data.School " placeholder="School">
                </div>
                <div class="row-input">
                    <div class="svg-elem">
                        <img src="../assets/class_.svg" alt="" class="svg">
                    </div>
                    <input type="text" class="Class_"   v-model="user_data.Class_ " placeholder="Class_">
                </div>
            </div>
            <div class="button-res">
                <button class="b-res" type="submit">Зарегистрироваться</button>
            </div>
            <p>Уже есть аккаунт?</p>
            <div class="button-sigin">
                    <button class="b-res" @click="$router.push({ name: 'sign' })">Войти</button>
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


<style>
.register-page{
    background-color: black;
}
.table-sigin{
    background-color: rgb(218, 86, 9);
    justify-content: center;
    justify-items: baseline;
    align-content: center;
    flex-wrap: wrap;
    margin: 30%;
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
    /* align-content: revert; */
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
    align-items: flex-end;
}
.svg-elem{
    width: 21px;
    height: 21px;
}
</style>