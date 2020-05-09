<template>
  <div>
    <b-table
      ref="selectableTable"
      selectable
      :select-mode="selectMode"
      :items="items"
      :fields="fields"
      @row-selected="onRowSelected"
      responsive="sm"
    >
      <!-- Example scoped slot for select state illustrative purposes -->
      <template v-slot:cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">&check;</span>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>
      </template>
    </b-table>

    <p>
      Selected Rows:<br />
      {{ selected }}
    </p>
    <b-button type="submit" block variant="danger" @click="upDate"
          >提交中奖人</b-button
        >
  </div>
</template>

<script>
export default {

  data() {
    return {
      fields: ["selected", "name", "phone", "signdate","label"],
      items: [],
      selectMode: "multi",
      selected: [],
      phone_arr:[],
    };
  },
   mounted() {
    this.getData();
  },
  methods: {
    onRowSelected(items) {
      
      this.phone_arr=items.map(item => item.phone);

      

      this.selected = items;
    },
    getData() {
      this.$axios
        .get("/api/feedback/activity")
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            this.items = res.data;
          }
        })
        .catch((error) => {
          console.log(error);
          alert("填报异常，请检查后再次提交");
        });

      // data默认接收剩余的属性值, 打印结果同上
      console.log(JSON.stringify(this.form));
    },
    upDate(){

      this.$axios
        .put("/api/feedback/activity", {phone_arr:this.phone_arr})
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("数据提交成功");
          } else {
            alert("填报异常，请检查后再次提交");
          }
        })
        .catch((error) => {
          console.log(error);
          alert("填报异常，请检查后再次提交");
        });
      //console.log(JSON.stringify(this.form));
    }
  },
};
</script>
