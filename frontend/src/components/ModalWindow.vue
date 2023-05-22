<template>
    <div class="modal fade show">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              {{ title }}
            </h5>
            <button
              type="button"
              class="close"
              aria-label="Close"
              @click="closeModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div
            class="modal-body"
            @scroll="onScroll"
          >{{ id_olimpiad }}
            <slot></slot>
          </div>
          <div class="modal-footer">
            <slot name="footer">
              <button
                type="button"
                class="btn btn-secondary"
                @click="closeModal"
              >
                Отмена
              </button>
                <button
                @click="RegisterOlimpiad()">
                    Записаться 
                </button>
              >
            </slot>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    
    props: {
      title: {
        type: String,
        default: ''
      },
      id_olimpiad: Number
    },
    data() {
      return {
        isRulesReaded: true // поменять 
      }
    },
    methods: {
      closeModal() {
        this.$emit('close')
      },
      onScrollEnd() {
        this.isRulesReaded = true
      },
      async RegisterOlimpiad(){
            let axiosConfig = {
                withCredentials: true,
                headers: {
                    'Accept': '*/*'}
                }
            await axios.post('olimpiads/register/olimpiad',
            {
                "id":this.id_olimpiad
            },axiosConfig).then((response)=>{
                console.log(response.data)
            })
        },
    }
  }
</script>
  
<style scoped>
.modal {
    display: block;
    color: aliceblue;
}
.body {
      height: 200px;
      overflow-y: scroll;
    }
</style>