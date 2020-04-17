<template>
  <div>
    <div class="">
      sdfsdf
    </div>
    <el-row>
      <el-col>
        <div class="block">
          <label for="" class="text-primarytext ma-5">查询时间</label>
          <el-date-picker
            v-model="value2"
            type="datetimerange"
            :picker-options="pickerOptions"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            align="right"
            value-format="timestamp"
            @change="btn"
          ></el-date-picker>
          <el-button icon="el-icon-search" circle class="ma-5"></el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-table
          :data="tableData"
          border
          style="width: 100%"
          :default-sort="{ prop: 'date', order: 'descending' }"
        >
          <el-table-column prop="id" label="出入口"></el-table-column>
          <el-table-column prop="da" label="客流" sortable></el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Axios from "axios";

@Component
export default class ComponentName extends Vue {
  tableData: Array<object> = [
    { id: "沿湖广场", da: "1222" },
    { id: "H&M", da: "23333" },
  ];
  pickerOptions: any = {
    shortcuts: [
      {
        text: "最近一周",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
          picker.$emit("pick", [start, end]);
        },
      },
      {
        text: "最近一个月",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
          picker.$emit("pick", [start, end]);
        },
      },
      {
        text: "最近三个月",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
          picker.$emit("pick", [start, end]);
        },
      },
    ],
  };
  public value2: string = "";
  btn() {
    console.log(this.value2[0] + "||" + this.value2[1]);
  }
  private mounted() {
    this.getData();
  }
  public getData() {
    Axios.get("/api/employee/attend")
      .then((res) => {
        if (res.status == 200) {
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
}
</script>

<style scoped lang="scss">
@import "@/assets/scss/style.scss";
/* @import url(); 引入css类 */
</style>
