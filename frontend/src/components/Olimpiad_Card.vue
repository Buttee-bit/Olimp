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
            <div class="button-wr" v-if="flag_user_in_olimp == 0">
                <button
                @click="RegisterOlimpiad()">
                    Записаться 
                </button>
            </div>
            <div class="button-wr" v-if="flag_user_in_olimp == 1">
                <button
                @click="StartOlimpiad()">
                    Участвовать 
                </button>
            </div>
            <div class="button-wr" v-if="flag_user_in_olimp == 2">
                <button
                @click="SeeResult()">
                    Результаты 
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
        flag_user_in_olimp:{
            type: Number,
            default: 1
        }
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
        },
        async StartOlimpiad(){
            const params = new URLSearchParams()
            params.append("id", this.id_olimp);
            await axios.get('task/task',{withCredentials: true},
            params
                )
                .then((response)=>{
                    console.log(response)
                })
//             await axios.get('lk/personalCabinet',
//                 {
//                 withCredentials: true
//                 }) .then(response => { 
//                     this.user_data.name = response.data.name
//                     this.user_data.city = response.data.city
//                     this.user_data.class_ = response.data.class_
//                     this.user_data.School = response.data.School
// })
// }
//         catch{
//             this.$router.push({ name: 'start' })
//         }    
        },
        async SeeResult(){
            await console.log('Посмотреть результаты')
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
    min-width: 100%;
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
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.time{
    margin-left: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
</style>