import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// import Element-UI and Style
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import i18n
import i18n from './locales';

Vue.use(ElementUI, {
  i18n: (key: string, value: any) => i18n.t(key, value),
});

// import Echarts
import echarts from 'echarts';
Vue.prototype.$echarts = echarts;

// import MD5
import md5 from 'js-md5';
Vue.prototype.$md5 = md5;

// import NProgress
// import NProgress from 'nprogress';
// import 'nprogress/nprogress.css';

// import axios for ajax application
import axios from 'axios';
axios.defaults.baseURL = 'http://58.42.231.98:5060';
// Vue.prototype.$axios = axios;

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  render: (h) => h(App),
}).$mount('#app');
