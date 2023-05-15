<template>
    <div class="buton-side">
        <div class="button-wr">
            <button
            @click="RegisterOlimpiad()">
                Записаться 
            </button>
        </div>
     </div>
</template>

<script>
export default{
    name:'RegisterButton',
    methods:{
        async RegisterOlimpiad(){
            let axiosConfig = {
                withCredentials: true,
                headers: {
                    'Accept': '*/*'}
                }
            await axios.post('olimpiads/register/olimpiad',
            {
                "id":this.id_olimp
            },axiosConfig).then((response)=>{
                console.log(response.data)
            })
        }

    }
}


</script>

<style></style>