<template>
  <div class="container">
    <div>
      <img alt="Vue logo" src="../assets/logo.png" width="100%" class="mt-2 mb-3" />
      <h3>会员折扣礼遇商户确认函</h3>
      <label for>回复日期2020年4月20日前</label>
    </div>
    <div>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-card style class="mb-2">
          <b-form-group id="input-group-1" label="品牌名称" label-for="input-1">
            <b-form-input id="input-1" v-model="form.base_brdname" required></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label="店铺号" label-for="input-2">
            <b-form-input id="input-2" v-model="form.base_shopno" required></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-3" label="公司名称" label-for="input-3">
            <b-form-input id="input-3" v-model="form.base_company" required></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-4" label="活动有效期" label-for="input-4">
            <v-md-date-range-picker :presets="presets"  :showActivatorLabel='false'  @change="handleChange" required></v-md-date-range-picker>
          </b-form-group>
          <b-form-group label="是否提供会员福利">
            <b-form-radio v-model="form.mem_check" name="some-radios" value="1">是</b-form-radio>
            <b-form-radio v-model="form.mem_check" name="some-radios" value="0">否</b-form-radio>
          </b-form-group>
          <div>
            <b-form-group label="如是，提供会员福利如下" v-if="form.mem_check=='1'">
              <b-input-group prepend="百合银卡会员消费折扣" append="折" class="mb-2 mr-sm-2 mb-sm-0">
                <b-input v-model="form.mem_silverdiscount" required></b-input>
              </b-input-group>
              <b-input-group prepend="玫瑰金卡会员消费折扣" append="折" class="mb-2 mr-sm-2 mb-sm-0">
                <b-input v-model="form.mem_gloddiscount" required></b-input>
              </b-input-group>
              <b-input-group prepend="牡丹钻卡会员消费折扣" append="折" class="mb-2 mr-sm-2 mb-sm-0">
                <b-input v-model="form.mem_diamonddiscount" required></b-input>
              </b-input-group>
              <label>其他增值福利</label>
              <b-form-textarea id="textarea-formatter" v-model="form.mem_other"></b-form-textarea>
            </b-form-group>
            <label>备注</label>
            <ul>
              <li>租户承诺此次活动真实可信，完成此确认函双边签署后，租户应及时宣导每一位店员完全知悉并认真执行此活动内容，不得中途修改内容或终止活动。</li>
              <li>折扣活动由租户直接实现优惠，不额外产生任何费用，不与其他优惠同享。</li>
              <li>此确认函租户签字盖章后，经由宏立城商业管理有限公司品牌市场中心会员管理市场部签章确认生效。</li>
            </ul>
          </div>
        </b-card>
        <b-form-group id="input-group-5" label="联系人" label-for="input-5">
          <b-form-input id="input-5" v-model="form.sign_contact" required></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-6" label="联系电话" label-for="input-6">
          <b-form-input id="input-6" type="number" v-model="form.sign_call" required></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-7" label="电子邮箱" label-for="input-7">
          <b-form-input id="input-7" v-model="form.sign_email" type="email"></b-form-input>
        </b-form-group>
        <b-button block type="submit" variant="outline-primary">提交</b-button>
        <!-- <b-button block type="reset" variant="outline-danger">重填</b-button> -->
      </b-form>
    </div>
    <!-- <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>-->
  </div>
</template>

<script>

export default {
  data() {
    return {
      presets:"",
      startDate:"",
      endDate:"",
      form: {
        title_vipperson: "", //不需要
        remark_contact: "", //不需要
        sign_signature: "", //不需要
        sign_replydate: "", //不需要
        base_brdname: "",
        base_shopno: "",
        base_company: "",
        base_expiredate:"",
        mem_check: 1,
        mem_silverdiscount: "",
        mem_gloddiscount: "",
        mem_diamonddiscount: "",
        mem_other: "",
        sign_contact: "",
        sign_call: "",
        sign_email: "",
        datevalues:[]
      },
      show: true
    };
  },
  computed: {
    state() {
      return this.form.spcard_shopmall.length >= 1;
    }
  },
  methods: {
     handleChange (values) {
      this.datevalues=values;
      console.log(this.datevalues)
      //this.values = values
    },
    onSubmit(evt) {
      evt.preventDefault();


      // 方法二:
      //let { options, ...data } = this.form;
     // console.log(options);
      //console.log(JSON.stringify(data));

      this.$axios
        .post("/api/feedback/gift", this.form)
        .then(res => {
          console.log(res);
        })
        .catch(error => {
          console.log(error);
        });

      // data默认接收剩余的属性值, 打印结果同上
      console.log(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>