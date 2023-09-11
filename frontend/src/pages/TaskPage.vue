<template>
    <Header_olimp/>
    <div class="wrapper">
        <div class="left-side"> 
            <TaskOlimp
            :type_task = "card.type_task"
            :olimp_title = "card.olimp_title"
            :number_task = "card.number_task"
            :title_task = "card.title_task"
            :score_task = "card.score_task"
            :text_task = "card.text_task"
            :decription_task = "card.decription_task"
            :id_olimp = "card.id_olimp"
            :id_task = "card.id_task"
            />
        </div>
        <div class="right-side">
            <div class="task-list">
                <div class="square">
                    1
                </div>
                <div class="square">
                    2
                </div>
                <div class="square">
                    3
                </div>
                <div class="square">
                    4
                </div>
                <div class="square">
                    5
                </div>
                <div class="square">
                    6
                </div>
                <div class="square">
                   7
                </div>
                <div class="square">
                    8
                </div>
            </div>
            
            <div class="botton-submit-task">
                <button class="submit">
                    Отправить результаты
                </button>
            </div>
            <timerVue class="timer" />

        </div>
    </div>
    <Footer_olimp/>
</template>

<script>
import Header_olimp from '../components/Header_olimp.vue'
import Footer_olimp from '../components/Footer_olimp.vue'
import TaskOlimp from '@/components/TaskOlimp.vue'
import timerVue from '../components/timer.vue'
import axios from 'axios'
export default{
    components: {
        Header_olimp,
        TaskOlimp,
        timerVue,
        Footer_olimp,
    },
    data(){
        return{
            user_answer:'',
            card : [],
        }
    },
    async mounted(){
        try {
            await axios.get(`task/olimp${3}/task/${this.id_task}`,
                {
                withCredentials: true
                }) .then(response => {
                    console.log(response.data)
                    this.card = response.data
})
}
        catch{
            console.log('wrong')
        }       
},
}

</script>

<style scoped>
.app{
    background-color: #000;
    color: #000;
}
.wrapper{
    display: flex;
    flex-direction: row;
    background-color: #000;

}
.left-side{
    max-width: 65%
}
.table-number{
    color: #000;
    background-color: aqua;
}
.title{
    height: 35px;
    padding: 5px;
    color: #ffffff;
    background-color: #45454e;
    margin-bottom: 10px;
    border-radius: 7px;
    font-size: 22px;
}

.title-task{
    padding: 5px;
    display: flex;
    color: #ffffff;
    background-color: #45454e;
    border-radius: 5px;
    align-items: center;

}

.number{
    margin-left: 5px;
    height: 35px;
    width: 35px;
    color: #fafafa;
    /* background: linear-gradient(to top, #be8301, #ff4800); */
    border: 2px solid transparent;
    border-image: linear-gradient(#be8301, #ff4800);
    -moz-border-image: -moz-linear-gradient(#be8301, #ff4800);
    -webkit-border-image: -webkit-linear-gradient(#be8301, #ff4800);
    border-image-slice: 1;
    background :#45454e;
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: space-around;
    justify-content: center;
    font-size: 24px;

}
.name{
    margin-left: 10px;
    color: #fafafa;
    font-size: 24px;

}
.score{
    margin-left: 10px;
    font-size: 20px
}
.support-title{
    display: flex;
    margin-top: 15px;
    justify-content: flex-start;
    color: #b3b3b6;
    
}
.support-title-block{
    margin-right:20px;
    /* border: 2px solid #b43f11; */
    background-color:linear-gradient(to top, #be8301, #ff4800);
    background:#4b4949;
    border-radius:5px;
    padding: 7px;
}
.block-text-task{
    margin-top: 15px;
    
    color: #b3b3b6;
    background:#45454e;
    border-radius: 5px;
    min-height: 100px;
    display: flex;
    align-items: center;

}
.text{
    margin-left: 30px;
    padding: 1px;
    font-size: 20px

}

.task-list {
  display: grid;
  grid-template-rows: repeat(auto-fill, 45px);
  grid-template-columns: repeat(auto-fill, 45px);
  grid-auto-columns: 100px;
  grid-auto-rows: 45px;
}
.square {
  background: #797c78;
  border-radius: 10px;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.right-side {
  position:fixed;
  left: 75vw;
  margin-top: 60px;
  margin-right: 100px;
  width: 30%;
  max-width: 250px;
}
.botton-submit-task{
    margin-top: 15px;

}
.submit{
    /* height: 35px;
    width: 120px; */
    color: #ffffff;
    background: linear-gradient(to top, #be8301, #ff4800);
    border: 1px solid #b43f11;
    background-color: #b43f11;
    border-radius: 5px;
    /* margin-left: 40px; */
    font-size: 20px;
    padding: 10px;
}
.support-title-answer-text{
    padding-left: 10px;
    padding-right: 10px;
}

.type_3_task{
    background-color: #45454e;
    padding: 10px;
    padding-left: 15px;
    border-radius: 5px;
}
.answer-field{
    margin-top: 15px;
    border-radius: 2px;
    
}
</style>