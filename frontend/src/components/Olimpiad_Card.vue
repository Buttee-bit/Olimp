<template>
    <div class="olimpiad-card">
        <div class="left-side">
            <div class="title-olimpiad">
                <p>{{ title }}</p>
            </div>
            <div class="modyle-olimpiad">
                <div>Программирование</div>
                <div>Криптография</div>
                <div>Базы данных</div>
            </div>
        </div>
        <div class="time">
            <div class="date-t">
                {{ time_end_data }}
            </div>
            <div class="hours">
                {{ time_end_hours }}
            </div>
        </div>
        <div class="buton-side">
            <div class="button-wr">
                <button>
                    Записаться 
                </button>
            </div>
         </div>
    </div>
</template>

<script>
export default{
    name: 'Olimpiad_card',
    props:{
        title:{
            type: String,
            default: 'Олимпиада'
        },
        time_end_data:{
            type: String,
            default:''
        },
        time_end_hours:{
            type: String,
            default:''
        },
    },
}

</script>

<style>
.olimpiad-card{
    color: #fafafa;
    display: flex;
    justify-content: center;
    font-size: 28px;
    


    /* border: 2px solid #b43f11; */
    background: linear-gradient(to left, transparent, rgb(223, 95, 21));
    opacity: 0.8;
    border-radius: 7px;
}
.modyle-olimpiad{
    display: flex;
    font-size: 18px;
    margin-left: 10px;
    padding-left: 10px;
    justify-content: space-evenly;

}
.left-side{
    margin-left: 5%;
}
.buton-side{
    margin-left: 5%;
}
.time{
    margin-left: 5%;

}
</style>