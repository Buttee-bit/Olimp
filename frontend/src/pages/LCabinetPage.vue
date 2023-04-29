<template>
    <Header_olimp/>
    <div class="wrapper-user">
        <div class="user-card">
            <div class="FIO">
            Иванов Иван Иванович 
        </div>
        <div class="data-user">
            <div class="info">
                Город: Санкт-петербург 
            </div>
            <div class="info">
                Школа: 215
            </div>
            <div class="info">
                Класс: 11
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

    <div class="olimpiad-card">
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
    </div>

</template>

<script>
import Header_olimp from '../components/Header_olimp.vue'

export default {
    components: {
        Header_olimp,
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
.olimpiad-card{
    color: #fafafa;
}
</style>

