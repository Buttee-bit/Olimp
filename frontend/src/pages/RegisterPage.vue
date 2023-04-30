<template>
<div class="register-page">
    <div class="page-SigIn">
        <div class="header">
            <div class="name-site">vkaolimp</div>
        </div>
        <SigInForm/>
    </div>
</div>
</template>

<script>
import SigInForm from '@/components/SigInForm.vue';

export default {
    components:{
        SigInForm
    }
};

</script>

<style>
.header {
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: flex-start;


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
  margin-left: 10%;
  color: #fafafa;
}
</style>