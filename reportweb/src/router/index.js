import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/wxfb1",
    name: "wxfb1",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/wxfb1.vue")
  },
  {
    path: "/wxfb2",
    name: "wxfb2",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/wxfb2.vue")
  },
  {
    path: "/ShopTable",
    name: "ShopTable",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/ShopTable.vue")
  },
  {
    path: "/GiftTable",
    name: "GiftTable",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/GiftTable.vue")
  },
  {
    path: "/MotherDay",
    name: "MotherDay",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/hl_wx_1.vue")
  },
  {
    path: "/Mother_list",
    name: "Mother_list",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/hl_wx_2.vue")
  }
];

const router = new VueRouter({
  // mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to,_from,next) => {
  if(to.path == '/MotherDay') {
    document.title = "Garland#时光荏苒，爱您依旧#"
  }
  next()
})

export default router;
