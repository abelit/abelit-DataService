<template>
  <div class="container">
    <div>
      <img alt="Vue logo" src="../assets/logo.png" width="100%" class="mt-2 mb-3" />
      <h3>购物卡租户参与确认函</h3>
      <label for>回复日期2020年4月20日前</label>
    </div>
    <div>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-card style class="mb-2">
          <b-form-group id="input-group-1" label="*品牌名称" label-for="input-1">
            <b-form-input id="input-1" v-model="form.base_brdname" required></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label="*店铺号" label-for="input-2">
            <b-form-input id="input-2" v-model="form.base_shopno" required></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-3" label="*公司名称" label-for="input-3">
            <b-form-input id="input-3" v-model="form.base_company" required></b-form-input>
          </b-form-group>
          <b-form-group label="*接受购物卡">
            <b-form-radio v-model="form.spcard_check" name="some-radios" value="1">确认接受</b-form-radio>
            <b-form-radio v-model="form.spcard_check" name="some-radios" value="0">确认不接受</b-form-radio>
          </b-form-group>
          <div>
            <b-form-group
              label="购物卡面值可根据客户需求自定义购买。持卡人可于卡片有效期内到参与商户设于"
              v-if="form.spcard_check=='1'"
            >
              <b-form-checkbox-group
                v-model="form.spcard_shopmall"
                :options="form.options"
                name="flavour-2a"
                stacked
              >

              </b-form-checkbox-group>
              <label>之店铺进行刷卡消费，购买之商品种类将不受限制。</label>
              <label for>购物卡持卡消费优惠政策(可填)</label>
              <b-form-group class="mb-0" label-for="textarea-formatter" description>
                <b-form-textarea
                  id="textarea-formatter"
                  v-model="form.remark_policy"
                  
                ></b-form-textarea>
              </b-form-group>
            </b-form-group>
            <label>如有任何疑问, 请与品牌市场中心-会员管理市场部 刘另红小姐 联系。Email:liulinghong@honglicheng Tel:18275040052</label>
          </div>
        </b-card>
        <b-form-group id="input-group-4" label="*联系人" label-for="input-4">
          <b-form-input id="input-4" v-model="form.sign_contact" required></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-5" label="*联系电话" label-for="input-5">
          <b-form-input id="input-5" type="number" v-model="form.sign_call" required></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-6" label="电子邮箱" label-for="input-6">
          <b-form-input id="input-6" v-model="form.sign_email" type="email"></b-form-input>
        </b-form-group>
        <b-button block type="submit" variant="outline-primary" class="mb-5">提交</b-button>
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
      form: {
        
        title_vipperson: "", //不需要
        title_vipemail: "", //不需要
        title_viptel: "", //不需要
        remark_contact: "", //不需要
        sign_signature: "", //不需要
        base_brdname: "",
        base_shopno: "",
        base_company: "",
        spcard_check: 1,
        spcard_shopmall: [], // Must be an array reference!
        options: [
          { text: "花果园购物中心", value: "花果园购物中心" },
          { text: "海豚广场", value: "海豚广场" },
          { text: "贵阳国际大道", value: "贵阳国际大道" }
        ],
        remark_policy: "",
        sign_contact: "",
        sign_call: "",
        sign_email: ""
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
    onSubmit(evt) {
      evt.preventDefault();
      if(this.form.spcard_check==1 && this.form.spcard_shopmall.length<1){
        alert("必须选择一个项目");
        return;
      }

      // 方法二:
      let { options, ...data } = this.form;
      console.log(options);
      console.log(JSON.stringify(data));

      this.$axios
        .post("/api/feedback/shop", data)
        .then(res => {
          console.log(res);
          if(res.status==200){
            alert("数据提交成功")
          }else{
            alert("填报异常，请检查后再次提交")
          }
        })
        .catch(error => {
          console.log(error);
          alert("填报异常，请检查后再次提交")
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