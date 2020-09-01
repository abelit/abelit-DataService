<template>
  <div class="c-device">
    <!-- <el-card style="border-radius: 0">
      <span>设备设置</span>
    </el-card> -->
    <el-row class="mt-20">
      <el-col />
    </el-row>
    <el-row class="ml-10">
      <el-button
        type="primary"
        @click="(dialogFormVisible = true), ClearData()"
      >
        添加新设备
      </el-button>
      <el-dialog
        title="添加新设备"
        :visible.sync="dialogFormVisible"
        :show-close="true"
        :close-on-click-modal="false"
      >
        <el-form
          ref="formDevice"
          :model="formDevice"
          :rules="rules"
        >
          <el-form-item
            label="设备号"
            prop="snid"
          >
            <el-input
              v-model="formDevice.snid"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item
            label="设备地点"
            prop="snname"
          >
            <el-input
              v-model="formDevice.snname"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item
            label="所属项目"
            prop="unname"
          >
            <el-input
              v-model="formDevice.unname"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item
            label="设备IP"
            prop="ip"
          >
            <el-input
              v-model="formDevice.ip"
              autocomplete="off"
            />
          </el-form-item>
        </el-form>
        <div
          slot="footer"
          class="dialog-footer"
        >
          <el-button @click="dialogFormVisible = false">
            关 闭 取 消
          </el-button>
          <el-button
            type="primary"
            @click="addDevice('formDevice')"
          >
            确 定
          </el-button>
        </div>
      </el-dialog>
      <el-dialog
        title="修改设备"
        :visible.sync="dialogFormVisible2"
      >
        <el-form
          ref="formDevice"
          :model="formDevice"
          :rules="rules"
        >
          <el-form-item
            label="设备号"
            prop="snid"
          >
            <el-input
              v-model="formDevice.snid"
              autocomplete="off"
              :disabled="true"
            />
          </el-form-item>
          <el-form-item
            label="设备地点"
            prop="snname"
          >
            <el-input
              v-model="formDevice.snname"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item
            label="所属项目"
            prop="unname"
          >
            <el-input
              v-model="formDevice.unname"
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item
            label="设备IP"
            prop="ip"
          >
            <el-input
              v-model="formDevice.ip"
              autocomplete="off"
            />
          </el-form-item>
        </el-form>
        <div
          slot="footer"
          class="dialog-footer"
        >
          <el-button @click="dialogFormVisible2 = false">
            取 消
          </el-button>
          <el-button
            type="primary"
            @click="UpDevice('formDevice')"
          >
            确 定
          </el-button>
        </div>
      </el-dialog>
    </el-row>
    <el-row class="mt-20">
      <el-col>
        <el-table
          v-loading="loading"
          :data="tableData"
          border
          style="width: 100%"
          :default-sort="{prop: 'date', order: 'descending'}"
        >
          <el-table-column
            type="index"
            width="50"
            label="序号"
          />
          <el-table-column
            prop="id"
            label="ID"
            width="40"
          />
          <el-table-column
            prop="snid"
            label="设备号"
          />
          <el-table-column
            prop="snname"
            label="设备地点"
          />
          <el-table-column
            prop="unname"
            label="所属项目"
          />
          <el-table-column
            prop="ip"
            label="设备IP"
          />
          <el-table-column
            prop="created_timestamp"
            label="创建时间"
            :formatter="dateFormat"
          />
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="handleEdit(scope.$index, scope.row)"
              >
                编辑
              </el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)"
              >
                删除
              </el-button>
            </template>
          </el-table-column>
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

class DeviceData {
  snid = '';
  snname = '';
  unname = '';
  ip = 0;
}

@Component
export default class ComponentName extends Vue {
  public datevalue2: any[] = [];
  public usernum = '';
  formDevice: DeviceData = new DeviceData();
  tableData: Array<object> = [];
  loading = false;
  pickerOptions: any = {};
  dialogFormVisible = false;
  dialogFormVisible2 = false;
  myThis: any = this;
  rules: any = {
    snid: [{ required: true, message: '请输入设备号', trigger: 'blur' }],
    snname: [{ required: true, message: '请输入设备地点', trigger: 'blur' }],
    unname: [{ required: true, message: '请输入所属项目', trigger: 'blur' }],
    ip: [
      { required: true, trigger: 'blur', validator: this.myThis.validcodeip }
    ]
  };

  private mounted() {
    this.getData()
  }

  public getData() {
    Axios.get('/api/employee/device', {})
      .then(res => {
        if (res.status == 200) {
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

  public DelData(_data: string) {
    Axios.delete('/api/employee/device', {
      data: {
        snid: _data
      }
    })
      .then(res => {
        if (res.status == 200) {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          this.getData()
        } else {
          this.$message({
            type: 'error',
            message: '删除失败!'
          })
        }
      })
      .catch(err => {
        console.log(err)
      })
  }

  public AddData(_data: any) {
    Axios.post('/api/employee/device', _data)
      .then(res => {
        if (res.data.code == 200) {
          this.$message({
            type: 'success',
            message: '添加成功!'
          })
          this.getData()
        } else {
          this.$message({
            type: 'error',
            message: '添加失败!'
          })
        }
      })
      .catch(err => {
        console.log(err)
      })
  }

  public UpData(_data: any) {
    Axios.put('/api/employee/device', _data)
      .then(res => {
        if (res.status == 200) {
          this.$message({
            type: 'success',
            message: '修改成功'
          })
          this.getData()
          this.dialogFormVisible2 = false
        } else {
          this.$message({
            type: 'error',
            message: '修改失败!'
          })
        }
      })
      .catch(err => {
        console.log(err)
      })
  }

  ClearData() {
    this.myThis.formDevice.snid = ''
    this.myThis.formDevice.snname = ''
    this.myThis.formDevice.unname = ''
    this.myThis.formDevice.ip = ''
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

  handleEdit(index: any, row: any) {
    this.myThis.formDevice.snid = row.snid
    this.myThis.formDevice.snname = row.snname
    this.myThis.formDevice.unname = row.unname
    this.myThis.formDevice.ip = row.ip
    this.dialogFormVisible2 = true
  }

  handleDelete(index: any, row: any) {
    // this.DelData(row.snid);
    this.$confirm('此操作将删除该设备, 是否继续?', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
      .then(() => {
        this.DelData(row.snid)
      })
      .catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
  }

  addDevice(formName: string) {
    this.myThis.$refs[formName].validate((valid:any) => {
      if (valid) {
        // alert('submit!');
        // this.updd(this.ruleForm);

        this.AddData(this.formDevice)
      } else {
        console.log('error submit!!')
        return false
      }
    })
  }

  UpDevice(formName: string) {
    this.myThis.$refs[formName].validate((valid: any) => {
      if (valid) {
        // alert('submit!');
        // this.updd(this.ruleForm);

        this.UpData(this.formDevice)
      } else {
        console.log('error submit!!')
        return false
      }
    })
  }

  /* ip正则验证 */
  validcodeip(rule:any, value:any, callback:any) {
    const reg = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/
    if (reg.test(value)) {
      callback()
    } else {
      return callback('IP输入格式不合法！')
    }
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/style.scss";
.c-device {
  margin-top: 50px;
  margin-left: 25px;
  margin-right: 25px;
}
</style>
