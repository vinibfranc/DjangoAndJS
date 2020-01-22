import Vue from 'vue'
import VueResource from 'vue-resource'
import Exemplo from './components/Exemplo.vue'
import lodash from 'lodash'

Vue.use(VueResource)

new Vue(Exemplo).$mount(".exemplo")