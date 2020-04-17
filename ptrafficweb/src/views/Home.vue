<template>
  <div>
    <hello-world></hello-world>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import HelloWorld from '../components/HelloWorld.vue';

@Component({ name: 'Home', components: { HelloWorld } })
export default class Home extends Vue {
  @Prop() private msg!: string;
}
</script>

<style scoped lang="scss">
/* @import url(); 引入css类 */
</style>
