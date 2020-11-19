<template>
    <div>
      <p>
        {{book.tittle}}  -- {{book.author}} -- {{book.year}}
      </p>
      <button @click="getTraffic()">{{msg}}</button>
      <li v-for="item in traffic" :key="item.pdate">
        {{ item.pdate }} -- {{item.psquare}}
      </li>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

interface Book {
  tittle:string
  author:string
  year:number
}

const Component =  defineComponent({
  data() {
    return {
      msg: "获取数据",
      traffic: [],
      book: {
        tittle: "Vue 3.0",
        author: "Abelit",
        year: 2020
      }
    }
  },
  methods: {
    getTraffic() {
      const url = "api/ptraffic/compare";
      this.$http.get(url, {
        params: {
          start: '2020-11-01',
          end: '2020-11-30'
        }
      })
      .then(res => {
        this.traffic = res.data
        console.log(this.traffic)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
});
export default Component;
</script>