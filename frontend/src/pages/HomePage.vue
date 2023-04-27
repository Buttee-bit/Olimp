<template>
<div class="home-pages">
    <Header_olimp/>
    <logo_olimp/>
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
    background-color: #b43f11;
    /* width: 68px; */
    font-size: 20px;
    height: 60px;
    border: 2px solid #cf663c;
    background-color: #cf663c;
    border-radius: 7px;

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