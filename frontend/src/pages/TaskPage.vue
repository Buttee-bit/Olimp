<template>
    <Header_olimp/>
    <div class="wrapper">
        <div class="left-side">
            <div class="titlt-olimp">
                <div class="title">Олимпиада по программированию  00:39:34 </div>
            </div>
            <div class="title-task">
                <div class="number">11</div>
                <div class="table-task">
                    <div class="name">Задача на координаты</div>
                    <div class="score">2 балла </div>
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
                    Именем какого ученого названа машина, имеющая следующее описание: математическая модель вычислений, описывающая абстрактную машину, которая манипулирует символами на полосе ленты в соответствии с таблицей правил.
                </div>
            </div>
            <div class="support-title">
                <div class="support-title-block">
                    <div class="support-title-answer-text">
                        Ответ
                    </div>
                </div>
            </div>
            

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

        </div>
    </div>
    <Footer_olimp/>
</template>

<script>
import Header_olimp from '../components/Header_olimp.vue'
import Footer_olimp from '../components/Footer_olimp.vue'

export default{
    components: {
        Header_olimp,
        Footer_olimp
    }
}

</script>

<style scoped>
.wrapper{
    display: flex;
    flex-direction: row;
    background-color: #b3adad;

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
</style>