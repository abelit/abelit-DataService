import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },

  {
    path: '/demo/element',
    name: 'ElementDemo',
    component: () => import('../views/demo/ElementDemo.vue'),
  },
  {
    path: '/demo/layout',
    name: 'LayoutDemo',
    component: () => import('../views/demo/AppLayout.vue'),
  },
  {
    path: '/traffic',
    name: 'test',
    component: () => import('../views/traffic/traffic.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
