<template>
  <div class="c-staff">
      <el-form
    ref="ruleForm"
    :model="ruleForm"
    :rules="rules"
    label-width="100px"
    class="demo-ruleForm"
  >
    <el-form-item
      label="工号"
      prop="userid"
    >
      <el-input v-model="ruleForm.userid" />
    </el-form-item>
    <el-form-item
      label="姓名"
      prop="username"
    >
      <el-input v-model="ruleForm.username" />
    </el-form-item>
    <el-form-item
      label="所属单位"
      prop="userunit"
    >
      <el-select
        v-model="ruleForm.userunit"
        placeholder="所属单位"
        style="width: 100%;"
      >
        <el-option
          label="区域一"
          value="a1"
        />
        <el-option
          label="区域二"
          value="a2"
        />
      </el-select>
    </el-form-item>
    <el-form-item
      label="所属部门"
      prop="userdm"
    >
      <el-select
        v-model="ruleForm.userdm"
        placeholder="所属部门"
        style="width: 100%;"
      >
        <el-option
          label="区域一"
          value="b1"
        />
        <el-option
          label="区域二"
          value="b2"
        />
      </el-select>
    </el-form-item>
    <el-form-item
      label="职务级别"
      prop="userjl"
    >
      <el-select
        v-model="ruleForm.userjl"
        placeholder="职务级别"
        style="width: 100%;"
      >
        <el-option
          label="区域一"
          value="c1"
        />
        <el-option
          label="区域二"
          value="c2"
        />
      </el-select>
    </el-form-item>
    <el-form-item
      v-model="ruleForm.userpic"
      label="上传照片"
      prop="userpic"
    >
      <el-upload
        class="avatar-uploader"
        action="https://jsonplaceholder.typicode.com/posts/"
        list-type="picture-card"
        :before-upload="beforeAvatarUpload"
        :on-change="picUpChange"
        :limit="1"
      >
        <i class="el-icon-plus" />
      </el-upload>
    </el-form-item>

    <el-form-item>
      <el-button
        type="primary"
        @click="submitForm('ruleForm')"
      >
        立即创建
      </el-button>
      <!-- <el-button @click="resetForm('ruleForm')">重置</el-button> -->
    </el-form-item>
  </el-form>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import Axios from 'axios'
import DateUtil from '../../mixins/DateUtil'
import * as fecha from 'element-ui/lib/utils/date'

class PersonsData {
  userid = '';
  username = '';
  userunit = '';
  userdm = '';
  userjl = '';
  userpic = '';
}

// class RegImages {
//   format: string = '';
//   image_data: string = '0';
// }

@Component
export default class ComponentName extends Vue {
  dialogVisible: any = '';
  ruleForm: PersonsData = new PersonsData();
  rules: any = {
    userid: [
      { required: true, message: '请输入工号', trigger: 'blur' },
      { min: 3, max: 5, message: '长度 5 个数字', trigger: 'blur' }
    ],
    username: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
    userunit: [
      { required: true, message: '请选择所属单位', trigger: 'change' }
    ],
    userdm: [{ required: true, message: '请选择所属部门', trigger: 'change' }],
    userjl: [{ required: true, message: '请选择职务级别', trigger: 'change' }],
    userpic: [{ required: true, message: '请上传图片' }]
  };

  myThis: any = this;
  public picUpChange(file:any, editFileList:any) {
    const reader = new FileReader()
    reader.onload = () => {
      const _base64: any = reader.result
      const BASE64: any = _base64.split(',')
      //      this.ruleForm.userpic64 = reader;
      this.ruleForm.userpic = BASE64[1]
    }
    reader.readAsDataURL(file.raw)
    this.ruleForm.userpic = file.name
    console.log(this.ruleForm.userpic)
  }

  public beforeAvatarUpload(file:any) {
    const isSize = new Promise(function(resolve, reject) {
      const width = 150
      const height = 150
      const _URL = window.URL || window.webkitURL
      const img = new Image()
      img.onload = function() {
        const valid = img.width === width && img.height === height
        // eslint-disable-next-line prefer-promise-reject-errors
        valid ? resolve() : reject()
      }
      img.src = _URL.createObjectURL(file)
    }).then(
      () => {
        return file
      },
      () => {
        this.myThis.$message.error('上传的icon必须是等于150*150!')
        // eslint-disable-next-line prefer-promise-reject-errors
        return Promise.reject()
      }
    )
    // const isJPG = file.type === 'image/jpeg';
    // const isLt2M = file.size / 150 / 150 < 2;
    // //console.log(file);
    // if (!isJPG) {
    //   //console.log(this);

    //   this.myThis.$message.error('上传头像图片只能是 JPG 格式!');
    // }
    // if (!isLt2M) {
    //   this.myThis.$message.error('上传头像图片大小不能超过 2MB!');
    // }
    return isSize
    // return isJPG && isLt2M;
  }

  public submitForm(formName: string) {
    console.log(this.$refs[formName])

    this.myThis.$refs[formName].validate((valid:any) => {
      if (valid) {
        // alert('submit!');
        console.log(this.ruleForm)
        this.updd(this.ruleForm)
      } else {
        console.log('error submit!!')
        return false
      }
    })
  }

  public resetForm(formName:any) {
    console.log(this.myThis.$refs[formName])
    console.log(this.$refs[formName])
    this.myThis.$refs[formName].resetFields()
  }

  // eslint-disable-next-line @typescript-eslint/no-empty-function
  public handlePictureCardPreview() {}
  // eslint-disable-next-line @typescript-eslint/no-empty-function
  public handleRemove() {}
  public onSubmit() {
    console.log(this.ruleForm)
  }

  public updd(obt: any) {
    console.log(obt)
    Axios.post('http://10.46.100.128:8000', JSON.stringify(obt), {})
      .then(res => {
        console.log(res)
        // console.log(JSON.stringify(res));
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/style.scss";
.c-staff {
    margin-top: 50px;
    margin-left: 25px;
    margin-right: 25px;
}
</style>
