import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
// import axios from "axios";

const app = createApp(App)
  .use(store)
  .use(router)
  .use(Antd);

app.mount("#app");