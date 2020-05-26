<template>
  <div>
    <div style="background:#409EFF;color:#ffffff;padding:10px;">
      花果园购物中心1-疫情期各入口客流统计
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
            :disabled="disabled"
            @click="btn"
          ></el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-table
          :data="tableData"
          v-loading="loading"
          element-loading-text="客流数据加载中..."
          border
          show-summary
          
          style="width: 100%"
          :default-sort="{ prop: 'date', order: 'descending' }"
        >
          <el-table-column type="index" width="50"></el-table-column>
          <el-table-column prop="tbheader" label="入口"></el-table-column>
          <el-table-column
            prop="tbdata"
            :label="titleLabel"
            :formatter="numberFormat"
            :render-header="renderheader"
          ></el-table-column>
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
  loading: boolean = true;
  disabled: boolean = false;
  tableData: Array<object> = [];
  titleLabel: string = " 客流(人次)" + "/" + "10:00~22:00";
  
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
      {
        text: "最近30日",
        onClick(picker: any) {
          const end = new Date();
          const start = new Date();
          start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
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

  private renderheader(h: any, { column, $index }: any) {
    return h("span", {}, [
      h("span", {}, column.label.split("/")[0]),
      h("br"),
      h("span", {}, column.label.split("/")[1]),
    ]);
  }

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

    // this.tableData = [];
    this.getData(this.value2[0].toString(), this.value2[1].toString());
  }
  private mounted() {
    console.log(this.value2);
    this.getData(this.value2[0].toString(), this.value2[1].toString());
  }
  public getData(s: string, d: string) {
    this.disabled = true;
    this.loading = true;
    Axios.get("http://58.42.231.98:5060/api/ptraffic/time", {
      params: {
        start: s,
        end: d,
      },
    })
      .then((res) => {
        if (res.status == 200) {
          //{"tbheader":"psquare","tbdata":2000},{"tbheader":"phm","tbdata":3000}
          this.tableData = [];
          let resData = res.data[0];
          let tbheader;
           res.data.forEach((item,index)=>{
            if(new Date(item.pdate)<new Date("2020-05-16")){
              item.pgatewaypiz=0;
              item.pkfc=0;
              item.prest=0;
            }
            if(new Date(item.pdate)<new Date("2020-05-24")){
              item.pck=0;
              item.pqbj=0;
              
            }
            item.pall=item.psquare+item.phm+item.pgateway+item.pgatewaypiz+item.pkfc+item.prest+item.pparking+item.pck+item.pqbj
            //   <el-table-column prop="psquare" label="沿湖广场" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="phm" label="H&M" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pgateway" label="人行天桥(乐转旁)" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pgatewaypiz" label="人行天桥(必胜客旁)" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pkfc" label="肯德基" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="prest" label="食尚汇门厅旁" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pparking" label="停车场" :formatter="numberFormat" width="100"></el-table-column>
           /// item.pall=item.psquare+item.phm+item.pgateway+item.pgatewaypiz+item.pkfc+item.prest+item.pparking+item.pck+item.pqbj
          
          })
          
          for (let j in resData) {
            switch (j) {
              case "psquare":
                tbheader = "沿湖广场";
                break;
              case "phm":
                tbheader = "H&M";
                break;
              case "pgateway":
                tbheader = "人行天桥(乐转旁)";
                break;
              case "pgatewaypiz":
                tbheader = "人行天桥(必胜客旁)";
                break;
              case "pkfc":
                tbheader = "肯德基";
                break;
              case "pqbj":
                tbheader = "一楼黔宝金店旁";
                break;
              case "pck":
                tbheader = "CKJeans";
                break;
              case "prest":
                tbheader = "食尚汇门厅旁";
                break;
              case "pparking":
                tbheader = "停车场";
                break;
              default:
                continue;
            }

            
            this.tableData.push({
              tbheader: tbheader,
              tbdata: resData[j],
              //tbdata: this.thousandSeparator(resData[j]),
            });
            //console.log(j+":"+resData[j]);
          }
          this.loading = false;
          this.disabled = false;
         
        }
      })
      .catch((err) => {
        console.log(err);
        this.disabled = false;
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
  // public getSummaries(param: any) {
  //   const { columns, data } = param;
  //   const sums: any = [];
  //   columns.forEach((column: any, index: any) => {
  //     if (index === 0) {
  //       sums[index] = "总计";
  //       return;
  //     }
  //     const values: any = data.map((item: any) =>
  //       Number(item[column.property].replace(",", ""))
  //     );
  //     if (!values.every((value: any) => isNaN(value))) {
  //       sums[index] = values.reduce((prev: any, curr: any) => {
  //         const value = Number(curr);
  //         if (!isNaN(value)) {
  //           return prev + curr;
  //         } else {
  //           return prev;
  //         }
  //       }, 0);
  //       sums[index] = this.thousandSeparator(sums[index]) + "";
  //     } else {
  //       sums[index] = "";
  //     }
  //   });

  //   console.log(sums);

  //   return sums;
  // }
  // public tableRowClassName({ row, rowIndex }: any) {
  //   console.log(row["tbdata"].replace(",", ""));
  //   if (row["tbdata"].replace(",", "") >= 5000) {
  //     return "warning-row";
  //   }
  //   return "";
  // }

  public getSummaries(param: any) {
    
    const { columns, data } = param;
    const sums: any = [];
    columns.forEach((column: any, index: any) => {
      if (index === 0) {
        sums[index] = "总计";
        return;
      }
      const values:any = data.map(item => Number(item[column.property]));
      
     if (!values.every((value: any) => isNaN(value))) {
        sums[index] = values.reduce((prev: any, curr: any) => {
          const value = Number(curr);
          if (!isNaN(value)) {
            return prev + curr;
          } else {
            return prev;
          }
        }, 0);
        sums[index] = sums[index].toLocaleString();
      } else {
        sums[index] = "N/A";
      }
      console.log(sums)
      return sums;
    });
  }
    public numberFormat(row: any, column: any, cellValue: any) {
      return cellValue.toLocaleString();
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/style.scss";
/* @import url(); 引入css类 */
.el-table {
  .warning-row {
    // background:greenyellow;
  }
}

.el-table {
  .success-row {
    background: green;
  }
}
</style>
