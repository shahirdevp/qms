import Vue from 'vue';
import './plugins/vuetify';
import './plugins/axios';
import App from './App.vue';
import router from './router';
import store from './store';
import './registerServiceWorker';
import VueSweetalert2 from 'vue-sweetalert2';
import VueSession from 'vue-session';

Vue.prototype.$apiUrl = 'http://localhost:8000/api/v1/';
Vue.prototype.$owner = '1';
Vue.prototype.$month = [
  {title: 'January', value: 'Jan'},
  {title: 'February', value: 'Feb'},
  {title: 'March', value: 'Mar'},
  {title: 'April', value: 'Apr'},
  {title: 'May', value: 'May'},
  {title: 'June', value: 'Jun'},
  {title: 'July', value: 'Jul'},
  {title: 'August', value: 'Aug'},
  {title: 'September', value: 'Sep'},
  {title: 'October', value: 'Oct'},
  {title: 'November', value: 'Nov'},
  {title: 'December', value: 'Dec'},
];

// Vue.use(vuetify)
Vue.use(VueSession);
Vue.use(VueSweetalert2);

Vue.config.productionTip = false;


new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
