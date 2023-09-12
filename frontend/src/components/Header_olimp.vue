<template>
    <div class="header">
        <div class="name-site">vkaolimp</div>
        <div class="right-side">
            <div class="sigin-button-wrap">
                <button class="sigin-button"
                @click="$router.push({name:'sign'})"
                v-if="this.$route.name == 'start'">
                    Войти
                    
                </button>
            </div>
            <LogOut
            v-if="!isSatartPage && !isRegisterPage && !isSigInpage"
            />
        </div>
    </div>

</template>

<script scoped>
import LogOut from './LogOut.vue';

export default{
    name: 'Header_olimp',
    components:{LogOut},
    computed:{
        isSatartPage(){
            return this.$route.name == 'start'
        },
        isRegisterPage(){
            return this.$route.name == 'registration'
        },
        isSigInpage(){
            return this.$route.name == 'sign'
        }
    }
}

</script>

<style >
.header {
  width: 100%;
  height: 56px;
  display: flex;
  justify-content: space-between;

  background: #18181C;
  /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1); */
  border-bottom: 1px solid #2F2F32;
}

.name-site {
  font-family: 'IBM Plex Serif';
  font-style: normal;
  font-weight: 400px;
  font-size: 36px;
  margin-left: 30px;
  display: flex;
  align-items: center;
  justify-content: center;

  color: #fafafa;
}
.right-side{
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 2%;

}
.registration-button-wrap{
    display: flex;
}
.sigin-button-wrap{
    margin-right: 5%;
    height: 37px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.sigin-button{
    height: 35px;
    width: 95px;
    font-family: Tahoma;
    font-style: normal;
    font-size: 20px;
    color: #fafafa;
    /* background: linear-gradient(to top, #be8301, #ff4800); */
    border: 2px solid #BB432C;
    background-color: #BB432C;
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

}

.register-button{
    height: 35px;
    color: #FFF;
    background-color: #18181C;
    border: 2px solid #b43f11;
    border-radius: 7px;
}
</style>