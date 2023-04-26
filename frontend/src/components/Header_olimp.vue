<template>
    <div class="header">
        <div class="name-site">vkaolimp</div>
        <div class="right-side">
            <div class="sigin-button-wrap">
                <button class="sigin-button">
                    Войти
                </button>
            </div>
            <div class="registration-button-wrap">
                <button class="register-button">
                    Регистраиця
                </button>
            </div>
        </div>
    </div>

</template>

<script>
export default{
    name: 'Header_olimp'
}

</script>

<style>
.header {
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: space-evenly;

  background: #18181C;
  /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1); */
  border-bottom: 2px solid #646262
}

.name-site {
  font-family: 'IBM Plex Serif';
  font-style: normal;
  font-weight: 400;
  font-size: 36px;
  display: flex;
  align-items: center;
  justify-content: center;

  color: #fafafa;
}
.right-side{
    display: flex;
    align-items: center;
    justify-content: center;

}
.registration-button-wrap{
    display: flex;
    margin-left: 10%;
}
.sigin-button{
    height: 35px;
    width: 95px;
    color: #fafafa;
    border: 2px solid #b43f11;
    background-color: #b43f11;
    border-radius: 7px;
}

.register-button{
    height: 35px;
    color: #ffffff;
    background-color: #18181C;
    border: 2px solid #b43f11;
    border-radius: 7px;


}
</style>