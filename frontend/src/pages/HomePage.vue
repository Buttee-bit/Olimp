<template>
<div class="home-pages">
    <Header_olimp/>
    <logo_olimp/>
    <div class="first-block">
        <div class="text-olimpiad">
            <p>Онлайн-олимпиады от</p>
            <p></p>
            <p>Военно-Космической академии им. А. Ф. Можайского</p>
            <!-- <p>им. А. Ф. Можайского</p> -->
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
    <div class="main-theme">
        <div class="second-block-first">
            <div class="prog-table">
                <div class="svg-elem">
                    <img src="../assets/program.svg" alt="">
                </div>
                <div class="title-prog">
                    <h3 class="title-block-text">Программирование</h3>
                </div>
                <div class="text-block">
                    <p class="text-first-block">Будут затронуты такие</p>
                    <p class="text-first-block">темы как ООП, алгоритмы, </p>
                    <p class="text-first-block">структуры данных архитектура</p>
                </div>
            </div>
    </div>
    <div class="second-block-two">
        <div class="second-block">
            <div class="prog-table">
                <div class="title-prog">
                    <h3 class="title-block-text">Криптография</h3>
                </div>
                <div class="text-block">
                    <p class="text-first-block">Создавайте программы,</p> 
                    <p class="text-first-block">которые используются для</p> 
                    <p class="text-first-block">шифрования данных,</p>  
                    <p class="text-first-block">информацией и её хранении</p> 
                </div>
            </div>
        </div>
    <div class="second-block-right">
        <div class="prog-table">
            <div class="title-prog">
                <h3 class="title-block-text">Базы данных</h3>
            </div>
            <div class="text-block">
                <!-- Проектирование и оптимизирование баз данных. Эффективная работа с ними через код -->
                <p class="text-first-block">Проектирование и </p>
                <p class="text-first-block">оптимизирование баз данных.</p>
                <p class="text-first-block">Эффективная работа</p>
                <p class="text-first-block">с ними через код</p>
            </div>
        </div>
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

<style scoped>
.home-pages{
    background: radial-gradient(48.28% 14.14% at 49.5% 19.95%, rgba(255, 77, 77, 0.28) 0%, rgba(0, 0, 0, 0.00) 100%), #19191D;
}
/* .home-pages{
    background: url("../assets/program.svg"), lightgray 0% 0% / 50px 50px repeat; 
} */
.text-olimpiad{
    display: grid;
    color: #ffffff;
    justify-content: space-around;
    align-items: center;
    justify-items: center;
    font-size: 55px;
    margin-top: 15px;
}

p {
	margin: 0;
	padding: 0 0 10px 0;
}
.color-head{
    font-size: 36px;
    background-image: linear-gradient(-195deg, #FFED00, #FF4F4E);
    -webkit-background-clip: text;
    font-size: 55px;


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
    background: #FF4D4D;
    font-size: 36px;
    padding: 17px 42px 18px 41px;

    border-radius: 5px;
}
.main-theme{
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    align-content: stretch;
    flex-direction: column;

}
.second-block{
    display: flex;
    width: 100%;
    /* margin-left: 196px; */
    flex-direction: column;
    align-items: flex-end;
    margin-right: 20px;
    margin-left: 5px;

}
.second-block-right{
    display: flex;
    width: 100%;
    /* margin-left: 196px; */
    flex-direction: column;
    align-items: stretch;
    margin-right: 4px;
}
.second-block-first{
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    margin-top: 5%;
}
/* .prog-table-first{
    display: flex;
} */
.title-prog_first{
    display: flex;

}
.prog-table{
    width: 70%;
    display: table-column;
    /* background: linear-gradient(to left, transparent, rgb(223, 95, 21));
     */
    /* background: rgba(34, 35, 39, 0.53); */
    /* background-color: #FF4F4E; */
    opacity: 0.75;
    border-radius: 20px;
    background: rgba(255, 77, 77, 0.12);

}
.second-block-two{
    display: flex;
    flex-direction: row;
    align-items: stretch;
    justify-content: flex-start;
    align-content: flex-start;
    margin-top: 10px;

}
.svg-elem{
    display: flex;
    width: 77px;
    height: 77px;
    margin-left: 3%;
    margin-top: 1%;
}
.title-prog{
    color: #ffffff;
    margin-left: 3%;
    font-size: 48px;
}
.title-block-text{
    /* margin-top: 5px; */
    margin: 10px 50px 5px 0;


}
.text-block{
    color: #EBE9E9;
    margin-left: 3%;
    margin-bottom: 3%;
    font-size: 32px;
}
.text-first-block{
    margin: 0px;
    padding: 0%;
    width: 100%;
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