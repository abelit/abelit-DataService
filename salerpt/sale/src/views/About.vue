<template>
  <div>
    {{ count.value }}
    <button @click.prevent="Add">Add</button>
    <div>
      <button @click="GetTraffic">获取数据</button>
      <li v-for="item in traffic.data" :key="item">{{ item.psquare }}</li>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, reactive, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "VueTest",
  setup() {
    const count = reactive({ value: 0 });
    const url = "api/ptraffic/compare";
    // const traffic = ref([]);
    const traffic = reactive({ data: [] });

    function Add() {
      count.value += 1;
    }

    const GetTraffic = () => {
      return  axios
        .get(url, {
          params: {
            start: "2020-11-01",
            end: "2020-11-30",
          },
        })
        .then((res) => {
          // // const traffic = ref([]);
          // traffic.value = res.data;
          traffic.data = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };
    onMounted(() =>{
      GetTraffic()
    });
    return {
      count,
      Add,
      traffic,
      GetTraffic,
    };
  },
  mounted() {
    // this.GetTraffic()
  }
});
</script>