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
            <div
            v-for="(product, title) in items"
            :key="title"
            >
                <Olimpiad_Card
                :title="product.title"
                :time_end_data="product.time_end_data"
                :time_end_hours="product.time_end_hours"
                />

            </div>
            <!-- <div class="olimpiad-card">
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
            </div> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Header_olimp from '../components/Header_olimp.vue'
import Olimpiad_Card from '@/components/Olimpiad_Card.vue';

export default {
    components: {
        Header_olimp,
        Olimpiad_Card 
    },
    data(){
        return{
            user_data:{
                name:'',
                city:'',
                class_:'',
                School :''
            },
            items:[]
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
})
            await axios.get('olimpiads/all/not_end',
            {
                withCredentials: true           
            }).then(response =>
            {
                this.items = response.data
                console.log(this.items[0])
            })
}
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
    flex-direction: column;
    align-items: center;
}

</style>

