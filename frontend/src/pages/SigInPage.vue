<template>
        <div class="header">
            <div class="name-site">vkaolimp</div>
        </div>
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
                <input type="text" class="email" v-model="email">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/user_svg.svg" alt="" class="svg">
                </div>
                <input type="password" class="password" v-model="password">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/user_svg.svg" alt="" class="svg">
                </div>
                <input type="text" class="f_name" v-model="f_name">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/user_svg.svg" alt="" class="svg">
                </div>
                <input type="text" class="Second_name"  v-model="Second_name">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/user_svg.svg" alt="" class="svg">
                </div>
                <input type="text" class="Last_name"  v-model="Last_name">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/city.svg" alt="" class="svg">
                </div>
                <input type="text" class="City"  v-model="City">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/school.svg" alt="" class="svg">
                </div>
                <input type="text" class="School"  v-model="School">
            </div>
            <div class="row-input">
                <div class="svg-elem">
                    <img src="../assets/class_.svg" alt="" class="svg">
                </div>
                <input type="text" class="Class_"  v-model="Class_">
            </div>
        </div>
        <div class="button-res">
            <button class="b-res" type="submit">Зарегистрироваться</button>
        </div>
        <p>Уже есть аккаунт?</p>
        <p>Войти</p>
    </div>

</template>

<script>
export default{
    data(){
        return{
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
    }, 
    methods:{
        register: function(){

        }
    }
}

</script>
export default {
    data(){
        return{}
    }
};

<style>
.table-sigin{
    background-color: brown;

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