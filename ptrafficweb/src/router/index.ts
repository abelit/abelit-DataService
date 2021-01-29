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
    name: 'traffic',
    component: () => import('../views/traffic/traffic.vue'),
  },
  {
    path: '/trafficMonth',
    name: 'trafficmonth',
    component: () => import('../views/traffic/trafficMonth.vue'),
  },
  {
    path: '/trafficContrast',
    name: 'trafficcontrast',
    component: () => import('../views/traffic/trafficContrast.vue'),
  },
  {
    path: '/daysale',
    name: 'daysale',
    component: () => import('../views/sale/DaySale.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
