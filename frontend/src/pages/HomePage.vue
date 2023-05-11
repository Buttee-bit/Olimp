<template>
<div class="home-pages">
    <Header_olimp/>
    <logo_olimp/>
    <div class="first-block">
        <div class="text-olimpiad">
            <p>Онлайн-олимпиады от</p>
            <p></p>
            <p>Военно-Космической академии</p>
            <p>им. А. Ф. Можайского</p>
            <p></p>
            <p></p>
            <p></p>
            <p class="color-head">Покажи на что способен</p>
        </div>

        <div class="buton-start-wrapper">
            <button class="buton-start"
            @click="$router.push({name:'registration'})">
                Принять участие
            </button>
        </div>
    </div>
    <div class="second-block">
        <div class="prog-table">
            <div class="svg-elem">
                <img src="../assets/program.svg" alt="">
            </div>
            <div class="title-prog">
                <h3>Программирование</h3>
            </div>
            <div class="text-block">
                будут затронуты такие
                темы как ООП, алгоритмы, структуры данных архитектура
            </div>
        </div>
    </div>
    <div class="second-block">
        <div class="prog-table">

            <div class="title-prog">
                <h3>Криптография</h3>
            </div>
            <div class="text-block">
                Разберите программные решения, 
                которые используются для 
                шифрования данных при обмене 
                информацией и её хранении
            </div>
        </div>
    </div>
    <div class="second-block">
        <div class="prog-table">
            <!-- <div class="svg-elem">
                <img src="../assets/program.svg" alt="">
            </div> -->
            <div class="title-prog">
                <h3>Базы данных</h3>
            </div>
            <div class="text-block">
                Проектирование и оптимизирование 
                баз данных. Эффективная работа с 
                ними через код
            </div>
        </div>
    </div>
    <Footer_olimp/>
</div>
</template>



<script>
import Footer_olimp from '@/components/Footer_olimp.vue';
import Header_olimp from '../components/Header_olimp.vue'
import logo_olimp from '@/components/logo_olimp.vue';

export default {
    components: {
        Header_olimp,
        logo_olimp,
        Footer_olimp
    }
};

</script>

<style >
.home-pages{
    background-color: #0a0a0a;
}
.text-olimpiad{
    display: grid;
    color: #ffffff;
    justify-content: space-around;
    align-items: center;
    justify-items: center;
    font-size: 42px;
    margin-top: 15px;
}

p {
	margin: 0;
	padding: 0 0 10px 0;
}
.color-head{
    font-size: 36px;
    background-image: linear-gradient(to bottom right, #ff6600, #ff3c00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.buton-start-wrapper{
    margin-top: 5%;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: flex-start;
    justify-content: center;

}
.buton-start{
    color: #0a0a0a;
    background-color: #d84d16;
    font-size: 20px;
    height: 60px;
    border: 2px solid #612107;
    background-color: #c5330e;
    border-radius: 7px;
}
.second-block{
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    margin-top: 5%;
}
.prog-table{
    width: 70%;
    display: table-column;
    background: linear-gradient(to left, transparent, rgb(223, 95, 21));
    opacity: 0.8;
    border-radius: 7px;

}
.svg-elem{
    
    max-width: 60px;
    max-height: 68px;
    display: flex;
    margin-top: 8px;
    margin-left: 4%;


}
.title-prog{
    color: #ffffff;
    margin-left: 5%;
    font-size: 26px;

}
.text-block{
    color: #ffffff;
    margin-left: 5%;
    margin-bottom: 3%;
    font-size: 20px;


}
.thred-block{
    display: block;
    width: 70%;
    justify-content: center;
    align-items: flex-start;

}
br {
margin: 1px;
padding: 1%;
}
.app{
  background: #0a0a0a;
}
</style>