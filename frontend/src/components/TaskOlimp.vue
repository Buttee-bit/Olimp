<template>
    <div class="wrapper">
        <div class="left-side">
            <div class="titlt-olimp">
                <div class="title">{{olimp_title}}  00:39:34 </div>
            </div>
            <div class="title-task">
                <div class="number">{{number_task}}</div>
                <div class="table-task">
                    <div class="name">{{ title_task }}</div>
                    <div class="score">{{score_task}} </div>
                </div>
            </div>
            <div class="support-title">
                <div class="support-title-block">
                    <div class="support-title-text">
                        Описание
                    </div>
                </div>
                
                <div class="support-title-block">
                    <div class="support-title-text">
                        Дополнительно
                    </div>
                </div>
                <div class="support-title-block">
                    <div class="support-title-text">
                        Скачать файл
                    </div>
                </div>
            </div>
            <div class="block-text-task">
                <div class="text">
                    {{ text_task }}
                </div>
            </div>
            <div class="support-title" v-if="props.type_task=1">
                <div class="support-title-block">
                    <div class="support-title-answer-text">
                        Ответ
                    </div>
                </div>
            </div>
            <div class="answer-field" v-if="props.type_task=1">
                <div class="type_3_task">
                    <input type="text" class="user-answer" placeholder="Ваш ответ">
                </div>
            </div>
            

        </div>
    </div>
</template>

<script>
// import axios from 'axios'
export default{
    
    name:'task_component',
data(){
    return{
        user_answer:'',
    }
},
props:{
    id_olimp:{
        type: Number,
        default: 3
    },
    id_task:{
        type: Number,
        default: 1
    },
    type_task:{
        type: Number,
        default: 1
    },
    olimp_title:{
        type:String,
    },
    number_task:{
        type: Number,
    },
    title_task:{
        type: String,
    },
    score_task:{
        type: Number,
    },
    text_task:{
        type:String,
    },
    decription_task:{
        type: String,
    },
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
</style>