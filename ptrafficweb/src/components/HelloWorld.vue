<template>
  <div class="hello">
    <el-button @click="handleButton" color="primary">elbutton</el-button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
// import Greeter from '../mixins/Greeter';

// let greeter = new Greeter();

// greeter.greet();

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;

  private handleButton() {
    alert('This is element-ui button');
  }

  private hello() {
    console.log('hello');
  }

  private mounted() {
    this.hello();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
