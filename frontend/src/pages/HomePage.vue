<template>
<div class="home-pages">
    <Header_olimp/>
    <logo_olimp/>
    <div class="text-olimpiad">
        <p>Онлайн-олимпиады от</p>
        <p></p>
        <p>Военно-Космической академии</p>
        <p>им. А. Ф. Можайского</p>

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