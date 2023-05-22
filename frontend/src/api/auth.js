export default function(instance){
    return{
        register(payload){
            return instance.post('/auth/register', payload,{
                headers:{
                    "Content-Type": "application/json"
                }
            })
        }
    }
}