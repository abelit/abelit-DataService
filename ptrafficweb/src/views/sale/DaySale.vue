<template>
  <div>
    <div style="background: #409eff; color: #ffffff; padding: 10px;">
      花果园购物中心1-每日销售情况汇报
    </div>
    <el-row>
      <el-col>
        <div class="block">
          <span class="demonstration mx-5">按月查询</span>
          <el-date-picker
            value-format="yyyy-MM-dd"
            v-model="search.date"
            type="daterange"
            align="right"
            placeholder="选择日期范围"
            :default-value="search.date"
            :picker-options="pickerOptions"
            range-separator=" ~ "
          >
          </el-date-picker>
          <el-button
            icon="el-icon-search"
            circle
            class="ma-5"
            :disabled="disabled"
            @click="searchData"
          ></el-button>
          <!-- <el-button type="primary" @click="exportExcel">导出</el-button> -->
        </div>
        <div>
          <ul>
            <li>
              汇报时间范围： {{search.date[0]}} ~ {{search.date[1]}}
            </li>
            <li>
              客流数据： {{trafficData.alltraffics}} (人次)
            </li>
            <li>
              单日客流({{search.date[1]}})： {{trafficData.daytraffics}} (人次) 
            </li>
            <li>
              A8POS机安装量： {{saleData.posa8}} (台)
            </li>
            <li>
              W280PPOS机安装量： {{saleData.posw280p}} (台)
            </li>
            <li>
              期间使用量： {{saleData.posusage}} (台)
            </li>
            <li>
              期间POS机收入： {{saleData.possale}} (元)
            </li>
            <li>
              期间系统总收入： {{saleData.totalsale}} (元)
            </li>

            <li>
              {{search.date[1]}}未进行销售补录商户共{{saleData.inputsale.length}}家(已撤铺的商铺可忽略)：
            </li>
            <div>
              <p v-for="item in saleData.inputsale" :key="item.scode">
              {{item.scode}} --- {{item.sname}}
              </p>
            </div>
          </ul>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Axios from "axios";
import * as fecha from "element-ui/lib/utils/date";

@Component
export default class ComponentName extends Vue {
  search: any = {
    date: [],
    beginDate: "",
    endDate: "",
  };
  pickerOptions: any = {
    shortcuts: [
      {
        text: "今天",
        onClick(picker) {
          const end = new Date();
          end.setHours(23, 59, 59);
          const start = new Date(end);
          start.setTime(end.getTime() - 3600 * 1000 * 24 + 1000);
          picker.$emit("pick", [start, end]);
        },
      },
      {
        text: "最近一周",
        onClick(picker) {
          const end = new Date();
          const start = new Date();
          end.setHours(23, 59, 59);
          start.setTime(end.getTime() - 3600 * 1000 * 24 * 7 + 1000);
          picker.$emit("pick", [start, end]);
        },
      },
      {
        text: "最近一个月",
        onClick(picker) {
          const end = new Date();
          const start = new Date();
          end.setHours(23, 59, 59);
          start.setTime(end.getTime() - 3600 * 1000 * 24 * 30 + 1000);
          picker.$emit("pick", [start, end]);
        },
      },
      // {
      //   text: "最近三个月",
      //   onClick(picker) {
      //     const end = new Date();
      //     const start = new Date();
      //     end.setHours(23, 59, 59);
      //     start.setTime(end.getTime() - 3600 * 1000 * 24 * 90 + 1000);
      //     picker.$emit("pick", [start, end]);
      //   },
      // },
    ],
  };
  loading: boolean = false;
  disabled: boolean = false;
  initDate: any = new Date();
  saleData: any = {posa8: 0, posw280p: 0,inputsale:[],posusage: 0,possale: 0, totalsale: 0};
  trafficData: any = {alltraffics: 0, daytraffics: 0};

  private mounted() {
    this.getSaleata(this.search.beginDate,this.search.endDate);
    this.getTrafficData(this.search.beginDate,this.search.endDate);
  }

  private created() {
    this.search.beginDate = this.handleTimeOld(
      this.initDate.getDate() == 1
        ? new Date(this.initDate - 24 * 60 * 60 * 1000)
        : this.initDate,
      "-"
    ); //2012-12-1   handleTimeOld是我用来获取当月的第一天的
    this.search.endDate = this.handleTimeNew(
      new Date(this.initDate - 24 * 60 * 60 * 1000)
    ); //2012-12-1 handleTimeNew是获取昨天的日期
    this.search.date.push(this.search.beginDate);
    this.search.date.push(this.search.endDate);
  }
  public searchData() {
    console.log(this.search)
    this.search.beginDate=this.search.date[0];
    this.search.endDate=this.search.date[1];
    this.getSaleata(this.search.beginDate,this.search.endDate);
    this.getTrafficData(this.search.beginDate,this.search.endDate);
  }

  public handleTimeOld(time, split) {
    //是我用来获取当月的第一天的
    let date = new Date(time);
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    split = "-";
    return [year, month, 1].map((num) => this.formatNumber(num)).join(split);
  }
  public handleTimeNew(time) {
    //handleTimeNew是获取今天的日期
    let date = new Date(time);
    let year = date.getFullYear();
    let month =
      date.getMonth() + 1 >= 10
        ? date.getMonth() + 1
        : "0" + (date.getMonth() + 1);
    let day = date.getDate() > 10 ? date.getDate() : "0" + date.getDate();
    return `${year}-${month}-${day}`;
  }

  public formatNumber(number) {
    return String(number)[1] ? String(number) : `0${number}`;
  }

  public async getSaleata(start: string, end: string) {
    this.disabled = true;
    this.loading = true;
    await Axios.get("http://58.42.231.98:5060/api/ptraffic/sales", {
      params: {
        start: start,
        end: end,
      },
    })
      .then((res) => {
        if (res.status == 200) {
          console.log(res.data)
          this.saleData = res.data
        }
      })
      .catch((err) => {
        console.log(err);
      })
      .finally(() => {
                  this.disabled = false;
      });
  }

  public async getTrafficData(start: string, end: string) {
    this.disabled = true;
    this.loading = true;
    await Axios.get("http://58.42.231.98:5060/api/ptraffic/traffics", {
      params: {
        start: start,
        end: end,
      },
    })
      .then((res) => {
        if (res.status == 200) {
         console.log(res.data)
         this.trafficData = res.data
        }
      })
      .catch((err) => {
        console.log(err);
      })
      .finally(() => {
        this.disabled = false;
      });
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/style.scss";
/* @import url(); 引入css类 */
.el-table {
  .success-row {
    background: green;
  }
  th {
    padding: 3px;
    text-align: center;
  }
  td {
    padding: 0px;
    text-align: right;
  }
  * {
    font-size: 0.8rem;
  }
}
</style>
