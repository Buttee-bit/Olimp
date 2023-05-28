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
                <button @click="OpenModal()">
                Регистрация
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
            await axios.get(`task/task/${Number(this.id_olimp)}`, {
                withCredentials: true
                })
                .then(
                    this.$router.push({ name: 'olimpiad' })
                )
                .catch(error => {
                console.error(error);
                })
        },
        async SeeResult(){
            await console.log('Посмотреть результаты')
        },
        async OpenModal(){
            this.isModalOpen = true;
    }

    }
}

</script>

<style>
.olimpiad-card{
    color: #fafafa;
    display: flex;
    justify-content: initial;
    font-size: 28px;
    min-width: 100%;
    background: linear-gradient(to left, transparent, rgb(223, 95, 21));
    opacity: 0.8;
    border-radius: 7px;
    margin-bottom: 3%;
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