import Vue from 'vue'
import Vuex from 'vuex'
import axois from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        dataset2Command: {}
    },
    mutations:{
        SET_dataset2Command(state, val){
            state.dataset2Command = val 
        }
    },
    actions:{
        async submitModelData({commit}, data){
            let result = await axois.post('http://127.0.0.1:5000/runModel',data)
            console.log(result)
        },
        async addNewModel({commit}, data){
            let result = await axois.post('http://127.0.0.1:5000/addNewModel', data)
            console.log(result)
        },
        async getModel({commit}){
            let result = await axois.get('http://127.0.0.1:5000/getModel')
            commit('SET_dataset2Command', result['data'])
        }
    },
    modules:{

    }
})