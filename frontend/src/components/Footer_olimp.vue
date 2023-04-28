<template>
    <div class="footer-wraper">
        <div class="logo">
            <img src="../assets/academ.svg" alt="">
        </div>
        <div class="kaff-title">
            <h3 class="kaf">Военно-космическая</h3>
            <p></p>
            <h3 class="kaf">академия им. А.Ф.Можайского</h3>
            <p></p>
            <h3 class="kaf">62 Кафедра</h3>
        </div>
        <div class="link-text">
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
.kaf{
    margin: 0px;
    padding: 0 0 10px 0;
    color: #ffffff;


}
.footer-wraper{
    background: #18181C;
    margin-top: 10%;
    display: flex;
    /* border-bottom: 2px solid #646262 */
    justify-content: space-evenly;

    border-top: 2px solid #646262;

}
.logo{
    margin: 1%;
    /* max-height: 90px; */
}
.kaff-title{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.link-text{
    display: flex;
    align-items: center;
    color: #ffffff;

}

</style>