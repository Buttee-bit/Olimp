<template>
    <div class="footer-wraper">
        <div class="logo">
            <img src="../assets/academ.svg" alt="">
        </div>
        <div class="kaff-title">
            <h3>Военно-космическая</h3>
            <p></p>
            <h3>академия им. А.Ф.Можайского</h3>
            <p></p>
            <h3>62 Кафедра</h3>
        </div>
        <div class="link-text">
            <p>Связаться с нами</p>
            <p>Регламент</p>
            <p>Сайт академии</p>
        </div>
    </div>

</template>

<script>
export default{
    name:'Footer_olimp'

}
</script>

<style>
#p{
	margin: 0;
	padding: 0 0 10px 0;
}
#h3{
    margin: 0px;
    padding: 0 0 10px 0;

}
.footer-wraper{
    background: #4d4b4b;
    margin-top: 10%;
    display: flex;
    /* border-bottom: 2px solid #646262 */
    border-top: 2px solid #646262;

}
.logo{
    margin: 2%;
}
.kaff-title{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.link-text{
    display: flex;
    align-items: center;
}

</style>