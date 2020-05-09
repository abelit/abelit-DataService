<template>
  <div class="container">
    <div id="bg"><img src="../assets/bg.jpg" /></div>
    <div id="page1" style="z-index:2;top:150px" v-if="currentPage == 1">
      <b-button
        type="submit"
        block
        variant="outline-info"
        size="lg"
        class="p-3"
        @click="btn1"
        >立即报名</b-button
      >
      <b-button
        type="submit"
        block
        variant="outline-success"
        size="lg"
        class="p-3 mt-5"
        @click="btn2"
        >查看中奖详情</b-button
      >
      <div id="info">
        <p>填写真实姓名+电话</p>
        <p>5月10日20:00 将抽取3名幸运“花粉” 获赠“爱的赠礼”一份</p>
      </div>
    </div>
    <div id="page2" style="z-index:2;top:100px;" v-if="currentPage == 2">
      <h2>信息填写</h2>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-1" label="姓名" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.name"
            required
            placeholder=""
            autocomplete="off"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="手机号码" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.phone"
            type="number"
            required
            autocomplete="off"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" block variant="outline-secondary"
          >确定</b-button
        >
              <b-button type="submit" block variant="outline-primary" @click="btn3" style="margin-top:10px;"
        >返回首页</b-button
      >
      </b-form>

    </div>
    <div id="page2" style="z-index:2;top:100px;" v-if="currentPage == 3">
      <h2>中奖名单</h2>
      <div id="list" v-if="isOpen">
        <b-alert
          show
          variant="light"
          style="border:1px solid #cccccc;margin-top:20px"
          v-for="item in items.filter((itm) => itm.label == 1)"
          :key="item.phone"
          ><span>电话:{{ item.phone }}</span
          ><span>姓名:{{ item.name }}</span></b-alert
        >
      </div>
      <div id="list" v-else>
        <b-alert show variant="danger" style="margin-top:60px;"
          >未到开奖时间，请等候...</b-alert
        >
        <b-button type="submit" block variant="outline-primary" @click="btn3" style="margin-top:10px;"
        >返回首页</b-button
      >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: "",
        phone: "",
      },
      items: [],
      hours: '2020-05-10 20:00:00',
      show: true,
      currentPage: 1,
      isOpen: false,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      if (!/^1(3|4|5|6|7|8|9)\d{9}$/.test(this.form.phone)) {
        alert("手机号码有误，请重填");
        return false;
      }

      this.$axios
        .post("/api/feedback/activity", this.form)
        .then((res) => {
          // console.log(res);
          if (res.data.code == 200) {
            alert("数据提交成功");
          } 
          if (res.data.code == 501)
          {
            alert("该手机号已经报名！");
          }
        })
        .catch((error) => {
          console.log(error);
          alert("填报异常，请检查后再次提交");
        });
      console.log(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.tel = "";
    },
    btn1() {
      this.currentPage = 2;
    },
    btn2() {
      this.currentPage = 3;
      this.$axios
        .get("/api/feedback/activity")
        .then((res) => {
          console.log(new Date(res.data[0].servertime).getHours());
          if (new Date(res.data[0].servertime) >= new Date(this.hours)) {
            if (res.status == 200) {
              var reg = /^(\d{3})\d*(\d{4})$/;

              // .phone.replace(reg, "$1****$2")
              this.items = res.data;
              this.items.forEach(function(item, index, array) {
                console.log(item);
                console.log(array[index].phone);
                array[index].phone = array[index].phone.replace(
                  reg,
                  "$1****$2"
                );
                array[index].name = array[index].name.substr(0, 1) + "*";
                // console.log(item.phone.replace(reg, "$1****$2"))
              });

              console.log(this.items);
            }
            this.isOpen = true;
          } else {
            this.isOpen = false;
          }
        })
        .catch((error) => {
          console.log(error);
          alert("填报异常，请检查后再次提交");
        });

      // data默认接收剩余的属性值, 打印结果同上
      console.log(JSON.stringify(this.form));
    },
    btn3() {
      this.currentPage = 1;
    },
  },
};
</script>
<style scoped>
* {
  font-size: 1rem;
}
h2 {
  font-size: 1.5rem;
  color: #c89661;
  text-align: center;
}
#bg {
  width: 100%;
  height: 100%;
  position: fixed;
  z-index: 1;
  left: 0px;
}
#bg img {
  width: 100%;
}

#page1,
#page2,
#page3 {
  position: absolute;
  width: 90%;
}
#info {
  position: fixed;
  bottom: 20px;
}
#info p {
  margin: 0px;
  font-size: 0.8rem;
  color: crimson;
}
#list span {
  margin: 5px;
}
</style>
