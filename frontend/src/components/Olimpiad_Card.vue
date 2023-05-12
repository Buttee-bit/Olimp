<template>
    <div class="olimpiad-card">
        <div class="left-side">
            <div class="title-olimpiad">
                <p>{{ title }}</p>
            </div>
            <div class="modyle-olimpiad">
                <div>Программирование</div>
                <div>Криптография</div>
                <div>Базы данных</div>
            </div>
        </div>
        <div class="time">
            <div class="date-t">
                {{ time_end_data }}
            </div>
            <div class="hours">
                {{ time_end_hours }}
            </div>
        </div>
        <div class="buton-side">
            <div class="button-wr">
                <button
                @click="RegisterOlimpiad()">
                    Записаться 
                </button>
            </div>
         </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name: 'Olimpiad_card',
    props:{
        id_olimp:{
            type: Number,
        },
        title:{
            type: String,
            default: 'Олимпиада'
        },
        time_end_data:{
            type: String,
            default:''
        },
        time_end_hours:{
            type: String,
            default:''
        },
    },
    methods:{
        async RegisterOlimpiad(){
            let axiosConfig = {
                withCredentials: true,
                headers: {
                    'Accept': '*/*'}
                }
            await axios.post('olimpiads/register/olimpiad',
            {
                "id":this.id_olimp
            },axiosConfig).then((response)=>{
                console.log(response.data)
            })
        }

    }
}

</script>

<style>
.olimpiad-card{
    color: #fafafa;
    display: flex;
    justify-content: center;
    font-size: 28px;
    


    /* border: 2px solid #b43f11; */
    background: linear-gradient(to left, transparent, rgb(223, 95, 21));
    opacity: 0.8;
    border-radius: 7px;
    margin-bottom: 3%;
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