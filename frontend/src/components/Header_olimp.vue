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

<script>
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

<style scoped>
.header {
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: space-between;

  background: #18181C;
  /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1); */
  border-bottom: 2px solid #646262
}

.name-site {
  font-family: 'IBM Plex Serif';
  font-style: normal;
  font-weight: 400;
  font-size: 36px;
  margin-left: 15%;
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
}
.sigin-button{
    height: 35px;
    width: 95px;
    color: #fafafa;
    background: linear-gradient(to top, #be8301, #ff4800);
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