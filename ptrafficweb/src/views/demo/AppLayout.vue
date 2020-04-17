<template>
  <el-container class="hello">
    <el-aside width="200px">Aside</el-aside>
    <el-container>
      <el-header>Header</el-header>
      <el-main
        >Main
        <router-view></router-view>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </el-container>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class ComponentName extends Vue {
  @Prop() private msg!: string;
}
</script>

<style scoped lang="scss">
/* @import url(); 引入css类 */
.el-header,
.el-footer {
  background-color: #353538;
  color: #f5e2e2;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #353538;
  color: #f5e2e2;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  //   height: 100%;
}
.el-container {
  height: 100%;
}
</style>
