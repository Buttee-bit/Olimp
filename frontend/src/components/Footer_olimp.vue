<template>
    <div class="footer-wraper">
        <div class="left-side-footer">
            <div class="logo">
                <img src="../assets/academ.svg" alt="">
            </div>
            <div class="kaff-title">
                <div class="kaf">Военно-космическая</div>
                <div class="kaf">академия им. А.Ф.Можайского</div>
                <div class="kaf">62 Кафедра</div>
            </div>
        </div>
        <div class="right-side-footer">
            <div class="link-text">
                <p class="link-text-p">Связаться с нами</p>
                <p class="link-text-p">Регламент</p>
                <p class="link-text-p">Сайт академии</p>

            </div>
        </div>
    </div>

</template>

<script>
export default{
    name:'Footer_olimp'

}
</script>

<style scoped>

.kaf{
    color: #FFF;
    font-family: 'Yandex Sans Display';
    font-size: 24px;
    font-style: normal;
    font-weight: 300;
    line-height: normal;
    padding-bottom: 3px;


}
.footer-wraper{
    display: flex;
    background: #222327;
    margin-top: 10%;
    display: flex;
    /* border-bottom: 2px solid #646262; */
    justify-content: space-between;
    flex-direction: row;

}
.left-side-footer{
    display: flex;
    flex-direction: row;
    align-items: stretch;
    justify-content: flex-start;
    /* align-content: stretch; */
    flex-wrap: nowrap;
}
.logo{
    margin: 10px 20px 10px 30px;
    /* max-height: 90px; */
}
.kaff-title{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.right-side-footer{
    display: flex;
    flex-direction: row;
}
.link-text{
    display: flex;
    align-items: center;
    color: #ffffff;
    margin-right: 120px;

}
.link-text-p{
    margin-left: 60px;
    display: flex;
    align-items: center;
    color: #C3C2C2;
    font-family: Yandex Sans Display;
    font-size: 16px;
    font-style: normal;
    font-weight: 300;
    line-height: normal;
}

</style>