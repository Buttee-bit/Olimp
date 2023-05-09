<template>
    <div class="lk-cabinet">
        <Header_olimp/>
        <div class="wrapper-user">
            <div class="user-card">
                <div class="FIO">
                {{ user_data.name }}
            </div>
            <div class="data-user">
                <div class="info">
                    Город: {{ user_data.city }} 
                </div>
                <div class="info">
                    Школа: {{ user_data.School }} 
                </div>
                <div class="info">
                    Класс: {{ user_data.class_ }} 
                </div>
            </div>
        </div>
            </div>
            
        <div class="olimpiad-board">
            <div class="p-olimpiad">
                <p class="text-olimp">Доступные олимпиады</p>
                <p class="text-olimp">Ваши Олимпиады</p>
                <p class="text-olimp">Архивные олимпиады</p>
            </div>
        </div>
        <div class="card-wrapper">
            <div class="olimpiad-card">
            <div class="left-side">
                <div class="title-olimpiad">
                    <p>Олимпиада по программированию для 9-11 классов</p>
                </div>
                <div class="modyle-olimpiad">
                    <div>Программирование</div>
                    <div>Криптография</div>
                    <div>Базы данных</div>
                </div>
            </div>
            <div class="time">
                <div class="date-t">
                    27.08.2023
                </div>
                <div class="hours">
                    13:00
                </div>
            </div>
            <div class="buton-side">
                <div class="button-wr">
                    <button>
                        Записаться 
                    </button>
                </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Header_olimp from '../components/Header_olimp.vue'

export default {
    components: {
        Header_olimp,
    },
    data(){
        return{
            user_data:{
                name:'',
                city:'',
                class_:'',
                School :''
            }
        }
    },
    async mounted(){
        try {
            await axios.get('lk/personalCabinet',
                {
                withCredentials: true
                }) .then(response => { 
                    this.user_data.name = response.data.name
                    this.user_data.city = response.data.city
                    this.user_data.class_ = response.data.class_
                    this.user_data.School = response.data.School
})}
        catch{
            this.$router.push({ name: 'start' })
        }       
}

};
</script>

<style>
.wrapper-user{
    color: #fafafa;
    display: flex;
    align-items: center;
    flex-direction: column;
    margin-top: 10%;
    height: 60%;
    width: 100%;
    

}
.user-card{
    /* background-color: gray; */
    color-interpolation: linearrgb;
    display: grid;
    padding-right: 10%;
    padding-left: 10%;
    width: 72%;
    align-content: center;
    justify-items: center;

}
.data-user{
    display: flex;
    
}
.FIO{
    margin-left: 3%;
    font-size: 42px;

}
.info{
    /* margin-right: 15%; */
    display: contents;
    padding-right: 40px

}

.olimpiad-board{
    color: #fafafa;
    margin-top: 5%;

        /* background-color: gray; */

    display: grid;
    width: 72%;
    padding-right: 10%;
    padding-left: 10%;
    align-content: center;
    justify-items: center;
}
.p-olimpiad{
    display:flex;
}
.text-olimp{
    margin-left: 12px;
}
.card-wrapper{
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    margin-top: 3%;
}
.olimpiad-card{
    color: #fafafa;
    display: flex;
    justify-content: center;
    font-size: 28px;
    


    /* border: 2px solid #b43f11; */
    background: linear-gradient(to left, transparent, rgb(223, 95, 21));
    opacity: 0.8;
    border-radius: 7px;
}
.modyle-olimpiad{
    display: flex;
    font-size: 18px;
    margin-left: 10px;
    padding-left: 10px;
    justify-content: space-evenly;

}
.left-side{
    margin-left: 5%;
}
.buton-side{
    margin-left: 5%;
}
.time{
    margin-left: 5%;

}
</style>

