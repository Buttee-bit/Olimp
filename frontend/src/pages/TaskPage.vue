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

        </div>
        <div class="right-side-task">
            <div class="table-number">
                <div class="number-task">
                    1
                </div>
                <div class="number-task">
                    2
                </div>
                <div class="number-task">
                    3
                </div>
                <div class="number-task">
                    4
                </div>
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

}
.left-side{
    max-width: 73%
}
.table-number{
    color: #000;
    background-color: aqua;
}
.title{
    height: 35px;
    color: #ffffff;
    background-color: #45454e;
    border: 2px solid #ffffff;
    border-radius: 7px;
    font-size: 22px;
}

.title-task{
    padding: 5px;
    display: flex;
    background-color: #45454e;
    border-radius: 5px;
}

.number{
    margin-left: 5px;
    height: 35px;
    width: 35px;
    color: #fafafa;
    /* background: linear-gradient(to top, #be8301, #ff4800); */
    border: 2px solid #b43f11;
    background-color:linear-gradient(to top, #be8301, #ff4800);
    background :#45454e;
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: space-around;
    justify-content: center;
}
.support-title{
    display: flex;
    justify-content: flex-start;
}
.support-title-block{
    margin-right:20px;
    margin-top:5px;
    /* border: 2px solid #b43f11; */
    background-color:linear-gradient(to top, #be8301, #ff4800);
    background:#4b4949;
    border-radius:2px;
}
.block-text-task{
    margin-top:5px;
    color: #b6b4b4;
    background:#45454e;
    border-radius: 5px;
}
.text{
    padding: 1px;
}
</style>