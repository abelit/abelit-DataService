<template>
  <div class="c-check">
    <!-- <el-card style="border-radius: 0">
      <span>打卡记录查询</span>
    </el-card> -->
    <el-row class="mt-20">
      <el-col>
        <div class="block">
          <label for="" class="text-primarytext ma-5">查询时间</label>
          <el-date-picker
            v-model="datevalue2"
            type="datetimerange"
            :picker-options="pickerOptions"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :default-time="['00:00:00', '23:59:00']"
            align="right"
            value-format="yyyy-MM-dd HH:mm:ss"
          />
          <label for="" class="text-primarytext ma-5">查询工号</label>
          <el-input
            v-model="usernum"
            placeholder="请输入内容"
            style="width:180px;"
          />
          <el-button icon="el-icon-search" circle class="ma-5" @click="btn1" />
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-table
          v-loading="loading"
          :data="tableData"
          border
          :row-class-name="tableRowClassName"
          style="width: 100%"
          :default-sort="{prop: 'date', order: 'descending'}"
        >
          <el-table-column type="index" width="50" label="序号" />
          <el-table-column prop="id" label="ID" width="40" />
          <el-table-column prop="userid" label="工号" width="180" />
          <el-table-column prop="username" label="姓名" width="180" />
          <el-table-column
            prop="checktime"
            label="打卡时间"
            :formatter="dateFormat"
          />
          <el-table-column prop="temperature" label="体温(参考值)" sortable />
          <el-table-column prop="snname" label="打卡地点" />
          <el-table-column prop="snid" label="设备号" />
          <el-table-column
            prop="status"
            label="状态"
            :filters="[
              {text: '同步成功', value: 0},
              {text: '同步失败', value: 1},
              {text: '重复打卡', value: 2}
            ]"
            :filter-method="filterTag"
            ><template slot-scope="scope">
              <p v-if="scope.row.status === 0">
                同步成功
              </p>
              <p v-if="scope.row.status === 1">
                同步失败
              </p>
              <p v-if="scope.row.status === 2">
                重复打卡
              </p>
            </template></el-table-column
          >
          <el-table-column prop="image" label="照片">
            <template slot-scope="scope">
              <img
                :src="'data:image/jpeg;base64,' + scope.row.image"
              /> </template
          ></el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import Axios from 'axios'
import DateUtil from '../../mixins/DateUtil'
import * as fecha from 'element-ui/lib/utils/date'

// interface DataInterface {
//   start: string;
//   end: string;
//   usernum: string;
//   getData(obj: object): void;
// }

@Component
export default class ComponentName extends Vue {
  public datevalue2: any[] = [];
  public usernum = '';

  tableData: Array<object> = [];
  loading = false;
  pickerOptions: any = {
    // shortcuts: [
    //   {
    //     text: '上一日',
    //     onClick(picker: any) {
    //       const end = new Date();
    //       const start = new Date();
    //       start.setTime(start.getTime() - 3600 * 1000 * 24);
    //       picker.$emit('pick', [start, start]);
    //     },
    //   },
    //   {
    //     text: '今日',
    //     onClick(picker: any) {
    //       const end = new Date();
    //       const start = new Date();
    //       //start.setTime(start.getTime() - 3600 * 1000 * 24);
    //       console.log(start);
    //       picker.$emit('pick', [start, start]);
    //     },
    //   },
    //   {
    //     text: '最近一周',
    //     onClick(picker: any) {
    //       const end = new Date();
    //       const start = new Date();
    //       start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
    //       picker.$emit('pick', [start, end]);
    //     },
    //   },
    //   {
    //     text: '最近一个月',
    //     onClick(picker: any) {
    //       const end = new Date();
    //       const start = new Date();
    //       start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
    //       picker.$emit('pick', [start, end]);
    //     },
    //   },
    // ],
  };

  btn(e: any) {
    if (e === null) {
    } else {
      console.log(this.datevalue2[0])
    }
  }

  btn1() {
    if (this.datevalue2 == null) {
      this.getData(null, null, this.usernum)
    } else {
      this.getData(this.datevalue2[0], this.datevalue2[1], this.usernum)
    }
    this.loading = true
  }

  private mounted() {
    // this.getData();
  }

  public getData(s: any, e: any, u: any) {
    Axios.get('http://10.46.101.70:5060/api/employee/attend', {
      params: {
        start: s,
        end: e,
        userid: u || null
      }
    })
      .then(res => {
        if (res.status === 200) {
          this.tableData = []
          // console.log(typeof res.data[22].checktime);
          this.loading = false
          this.tableData = res.data
        }
      })
      .catch(err => {
        console.log(err)
      })
  }

  public formatDate(date: Date) {
    var d = date
    var month = '' + (d.getMonth() + 1)
    var day = '' + d.getDate()
    var year = d.getFullYear()

    if (month.length < 2) month = '0' + month
    if (day.length < 2) day = '0' + day

    return [year, month, day].join('-')
  }

  // 列表日期时间格式化
  public dateFormat(row: object, column: object, cellValue: any) {
    //    let aa = new Date(cellValue).toUTCString();
    const XXXXTime = Date.parse(cellValue)
    // console.log(XXXXTime);
    return cellValue
      ? fecha.format(new Date(XXXXTime - 8 * 3600 * 1000), 'yyyy-MM-dd HH:mm')
      : ''
  }

  public tableRowClassName({ row, rowIndex }: any) {
    if (row.temperature > 37.3) {
      return 'danger-row'
    } else {
      return ''
    }
  }

  filterTag(value: any, row: any) {
    console.log('aaaa')
    return row.status === value
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/style.scss";
.c-check {
  margin-top: 50px;
  margin-left: 25px;
  margin-right: 25px;
}
</style>
