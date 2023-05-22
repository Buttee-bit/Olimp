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
                <button class="text-olimp"
                v-bind:class="{ 'btn-active': isActive1 }"
                @click="getDataActualOlimp(isActive1), isActive1 = !isActive1">
                Доступные олимпиады</button>
                <button class="text-olimp"
                v-bind:class="{ 'btn-active': isActive2 }" 
                @click="getDataYourOlimp(isActive2), isActive2 = !isActive2">Ваши Олимпиады</button>
                <button class="text-olimp"
                v-bind:class="{ 'btn-active': isActive3 }" 
                @click="getDataEndOlimp(isActive3), isActive3 = !isActive3">Архивные олимпиады</button>
            </div>
        </div>
        <div class="card-wrapper">
            <div class ='one-card'
            v-for="(product, title) in items"
            :key="title"
            >
                <Olimpiad_Card
                :id_olimp = "product.id_olimp"
                :title="product.title"
                :time_end_data="product.time_end_data"
                :time_end_hours="product.time_end_hours"
                :flag_user_in_olimp="product.flag_user_in_olimp"
                />
            </div>
            
        </div>
        <Footer_olimp/>
    </div>
</template>

<script>
import axios from 'axios';
import Header_olimp from '../components/Header_olimp.vue'
import Olimpiad_Card from '@/components/Olimpiad_Card.vue';
import Footer_olimp from '@/components/Footer_olimp.vue';

export default {
    components: {
        Header_olimp,
        Olimpiad_Card,
        Footer_olimp,
    },
    data(){
        return{
            user_data:{
                name:'',
                city:'',
                class_:'',
                School :''
            },

            isActive1:false,
            isActive2:false,
            isActive3:false,

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
}
        catch{
            this.$router.push({ name: 'start' })
        }       
},
methods:{
    async getDataActualOlimp(isActive1){
        if(!isActive1){
        await axios.get('olimpiads/all/not_end',
            {
                withCredentials: true           
            }).then(response => {
          this.items = response.data;
          console.error(response.data);
          return true
        })
        .catch(error => {
          console.error(error);
        })
        }
        else{
            this.items=[]
        }
    },
    async getDataYourOlimp(isActive2){
        if(!isActive2){
        await axios.get('olimpiads/all/you_olimp',
            {
                withCredentials: true           
            }).then(response => {
          this.items = response.data;
          console.error(response.data);
          return true
        })
        .catch(error => {
          console.error(error);
        })
        }
        else{
            this.items=[]
        }
    },
    async getDataEndOlimp(isActive3){
        if(!isActive3){
            await axios.get('olimpiads/all/end',
            {
                withCredentials: true           
            }).then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.error(error);
        });
        }
        else{
            this.items=[]
        }
        
    },
    OpenModal(){
        this.modalShow = true;
    },

    async StartOlimpiad(){
    await axios.get('task/task/${id_olimp}',{withCredentials: true})
        .then(
            this.$router.push({ name: 'olimpiad' })
        )
},


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
    display: contents;
    padding-right: 40px

}

.olimpiad-board{
    color: #fafafa;
    margin-top: 5%;
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
.btn-active {
  background-color: #f00;
  color: #fff;
}

</style>

