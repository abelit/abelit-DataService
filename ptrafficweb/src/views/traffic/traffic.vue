<template>
  <div>
    <div style="background:#409EFF;color:#ffffff;padding:10px;">
      花果园购物中心疫情期间客流
    </div>
    <el-row>
      <el-col>
        <div class="block">
          <el-date-picker
            v-model="value2"
            type="daterange"
            align="right"
            unlink-panels
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :picker-options="pickerOptions"
            format="yyyy-MM-dd"
            value-format="yyyy-MM-dd"
          ></el-date-picker>
          <el-button
            icon="el-icon-search"
            circle
            class="ma-5"
            @click="btn"
          ></el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-table
          :data="tableData"
          border
          show-summary
          :summary-method="getSummaries"
          style="width: 100%"
          :default-sort="{ prop: 'date', order: 'descending' }"
        >
          <el-table-column type="index" width="50"></el-table-column>
          <el-table-column prop="tbheader" label="出入口"></el-table-column>
          <el-table-column prop="tbdata" label="客流"></el-table-column>
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
  tableData: Array<object> = [];

  pickerOptions: any = {
    disabledDate(time: any) {
      return time.getTime() >= Date.now();
    },
    shortcuts: [
      {
        text: "上一日",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          start.setTime(start.getTime() - 3600 * 1000 * 24);
          picker.$emit("pick", [start, start]);
        },
      },
      {
        text: "今日",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          //start.setTime(start.getTime() - 3600 * 1000 * 24);
          picker.$emit("pick", [start, start]);
        },
      },
      {
        text: "最近一周",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          start.setTime(start.getTime() - 3600 * 1000 * 24 * 6);
          picker.$emit("pick", [start, end]);
        },
      },
    ],
  };

  public value2: Array<string> = [
    this.formatDate(
      new Date(new Date().setTime(new Date().getTime() - 3600 * 1000 * 24 * 1))
    ),
    this.formatDate(
      new Date(new Date().setTime(new Date().getTime() - 3600 * 1000 * 24 * 1))
    ),
  ];

  public thousandSeparator(num: number) {
    return (
      num &&
      (num.toString().indexOf(".") != -1
        ? num.toString().replace(/(\d)(?=(\d{3})+\.)/g, function($1, $2) {
            return $2 + ",";
          })
        : num.toString().replace(/(\d)(?=(\d{3})+\b)/g, function($1, $2) {
            return $2 + ",";
          }))
    );
  }

  btn() {
    //console.log(this.startTime.setTime(this.star));
    // console.log(this.value2);
    // console.log(this.thousandSeparator(4656262.262))

    this.tableData = [];
    this.getData(this.value2[0].toString(), this.value2[1].toString());
  }
  private mounted() {
    console.log(this.value2);
  }
  public getData(s: string, d: string) {
    Axios.get("http://58.42.231.98:5060/api/ptraffic/time", {
      params: {
        start: s,
        end: d,
      },
    })
      .then((res) => {
        if (res.status == 200) {
          //{"tbheader":"psquare","tbdata":2000},{"tbheader":"phm","tbdata":3000}

          let resData = res.data[0];
          let tbheader;
          for (let j in resData) {
            switch (j) {
              case "psquare":
                tbheader = "沿湖广场";
                break;
              case "phm":
                tbheader = "H&M";
                break;
              case "pgateway":
                tbheader = "人行天桥";
                break;
              case "pparking":
                tbheader = "停车场";
                break;
              default:
                continue;
            }

            this.tableData.push({
              tbheader: tbheader,
              tbdata: this.thousandSeparator(resData[j]),
            });
            //console.log(j+":"+resData[j]);
          }
          console.log(this.tableData);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }

  public formatDate(date: Date) {
    var d = date,
      month = "" + (d.getMonth() + 1),
      day = "" + d.getDate(),
      year = d.getFullYear();

    if (month.length < 2) month = "0" + month;
    if (day.length < 2) day = "0" + day;

    return [year, month, day].join("-");
  }
  public getSummaries(param:any) {
        const { columns, data } = param;
        const sums:any = [];
        columns.forEach((column:any, index:any) => {
          if (index === 0) {
            sums[index] = '总计';
            return;
          }
          const values:any = data.map((item: any) => Number(item[column.property].replace(',','')));
          if (!values.every((value: any) => isNaN(value))) {
            sums[index] = values.reduce((prev:any, curr:any) => {
              const value = Number(curr);
              if (!isNaN(value)) {
                return prev + curr;
              } else {
                return prev;
              }
            }, 0);
            sums[index] = this.thousandSeparator(sums[index]) + ' (人)';
          } else {
            sums[index] = '';
          }
        });

        console.log(sums)

        return sums;
      }
}
</script>

<style scoped lang="scss">
@import "@/assets/scss/style.scss";
/* @import url(); 引入css类 */
</style>
