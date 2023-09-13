<template>
    <ModalWindow
                v-if="isModalOpen"
                title ='Очень важна информация'
                :id_olimpiad = "id_olimp"

                @close="isModalOpen = false"
                >
                <li>Для участия в олимпиаде необходимо предварительно зарегистрироваться[ на сайте олимпиады] и вступить в telegram-канал, предназначенный для информирования конкурсантов.</li>
                <li>Конкурсантам предлагается комплект заданий , включающий в себя вопросы с развернутыми, однозначными и множественными ответами . Оценке подлежит правильность и скорость выполнения заданий. [ можно ещё написать тут про баллы ]</li>
                <li>После окончания испытаний результат конкурсанта фиксируется в общем рейтинге . По завершении Олимпиады каждому участнику высылается на личную почту сертификат участника, а победителям и призёрам- сертификаты победителя и призера соответственно</li>
    </ModalWindow>
    <div class="olimpiad-card">
        <div class="left-side">
            <div class="title-olimpiad">
                <p class="title-olimp-card-text">{{ title }}</p>
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
                <button class="button-button" @click="OpenModal()">
                Регистрация
                </button>

            </div>
            <div class="button-wr" v-if="flag_user_in_olimp == 1">
                <button class="button-button"
                @click="StartOlimpiad()">
                    Участвовать 
                </button>
            </div>
            <div class="button-wr" v-if="flag_user_in_olimp == 2">
                <button class="button-button"
                @click="SeeResult()">
                    Результаты 
                </button>
            </div>
         </div>
    </div>
</template>

<script>
import axios from 'axios';
import ModalWindow from './ModalWindow.vue';

export default{
    name: 'Olimpiad_card',
    components:{
    ModalWindow,
},
data() {
    return {
      isModalOpen: false,
    }
  },
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
            // await axios.get(`task/olimp/${this.id_olimp}/task/${1}`, {
            //     withCredentials: true
            //     })
                // .then(
                    this.$router.push({ name: 'olimpiad' })
                // )
                // .catch(error => {
                // console.error(error);
                // })
        },
        async SeeResult(){
            await console.log('Посмотреть результаты')
        },
        // 
        async OpenModal(){
            this.isModalOpen = true;
    }

    }
}

</script>

<style>
.olimpiad-card{
    color: #D4D4D8;
    display: flex;
    /* font-size: 28px; */
    height: 143px;
    background: #222327;
    border-radius: 7px;
    margin-bottom: 2%;
    flex-direction: row;
    margin-left: 10px;
}
.one-card{
    display: flex;
    justify-items: center;
    justify-content: center;
    flex-direction: column-reverse;
    max-width: 70%;
    min-width: 70%;

}
.modyle-olimpiad{
    display: flex;
    justify-content: space-evenly;
    gap: 12px;
    margin: 0px;
    padding: 0px;
    font-size: 17px;

}
.left-side{
    display: flex;
    flex-direction: column;
    margin-left: 25px;
    align-items: center;
    justify-content: space-evenly;

}
.buton-side{
    margin-left: 25px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;

}
.date-t{
    font-size: 22px;
}
.hours{
    font-size: 22px;
}
.time{
    margin-left: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.title-olimpiad{
    display: flex;
    flex-direction: row;    
}
.title-olimp-card-text{
    font-size: 32px;
    margin: 0px;
}
/* .button-button{
    background: #BB432C;
    border: 2px solid #b43f11;
    background-color: #bb432c;
} */
.button-register{
    background: #BB432C;
    border: 2px solid #b43f11;
    background-color: #bb432c;
}
.button-button{
    background: #BB432C;
    border: 2px solid #b43f11;
    background-color: #bb432c;
    height: 100%;
    width: 100px;
    border-radius: 5px;
    color: #D4D4D8;
    height: 40px;
    width: 120%;
}
</style>