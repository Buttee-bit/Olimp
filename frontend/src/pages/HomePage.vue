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
            <button class="buton-start">
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
                <p>будут затронуты такие</p>
                <p>темы как ООП, алгоритмы, структуры данных архитектура</p>
            </div>
        </div>
    </div>
</div>
</template>



<script>
import Header_olimp from '../components/Header_olimp.vue'
import logo_olimp from '@/components/logo_olimp.vue';
export default {
    components: {
        Header_olimp,
        logo_olimp
    }
};

</script>

<style>
.text-olimpiad{
    display: grid;
    color: #ffffff;
    justify-content: space-around;
    align-items: center;
    justify-items: center;
    font-size: 26px;
    margin-top: 15px;
}

p {
	margin: 0;
	padding: 0 0 10px 0;
}
.color-head{
    font-size: 26px;
    background-image: linear-gradient(to bottom right, #ff8800, #ff3c00);
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
    /* width: 68px; */
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
}
.prog-table{
    width: 70%;
    border: 2px solid #b43f11;
    display: table-column;

}
.svg-elem{
    
    max-width: 72px;
    max-height: 62px;
    display: flex;
    margin-top: 8px;

}
.title-prog{
    color: #ffffff;
}
.text-block{
    color: #ffffff;
}
br {
margin: 1px;
padding: 1%;
}
.app{
  width: 100vw;
  height: 100vh;
  background: #0a0a0a;
}
</style>