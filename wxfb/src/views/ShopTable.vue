<template>
  <b-container fluid>
    <div>
      <img alt="Vue logo" src="../assets/logo.png" class="mt-2 mb-3" />
      <h3>购物卡租户参与查询表</h3>
    </div>
    <!-- User Interface controls -->

    <!-- Main table element -->
    <b-table show-empty small stacked="md" :items="items" :fields="fields">
      <!-- <template v-slot:cell(name)="row">
        {{ row.value.first }} {{ row.value.last }}
      </template>

      <template v-slot:cell(actions)="row">
        <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
          Info modal
        </b-button>
        <b-button size="sm" @click="row.toggleDetails">
          {{ row.detailsShowing ? 'Hide' : 'Show' }} Details
        </b-button>
      </template>-->

      <!-- <template v-slot:row-details="row">
        <b-card>
          <ul>
            <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
          </ul>
        </b-card>
      </template>-->
    </b-table>

    <!-- Info modal -->
    <!-- <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
      <pre>{{ infoModal.content }}</pre>
    </b-modal>-->
  </b-container>
</template>

<script>
import shop_zh from "@/en_cn/EntoZh";
export default {
  data() {
    return {
      items: [],
      fields: []
    };
  },
  computed: {
    // sortOptions() {
    //   // Create an options list from our fields
    //   return this.fields
    //     .filter(f => f.sortable)
    //     .map(f => {
    //       return { text: f.label, value: f.key };
    //     });
    // }
  },
  mounted() {
    // Set the initial number of items
    this.getData();
    // console.log(entozh1);
    // console.log(entozh2);
    this.totalRows = this.items.length;
  },
  methods: {
    getData() {
      this.$axios
        .get("/api/feedback/shop")
        .then(res => {
          console.log(res);
          if (res.status == 200) {
            //  console.log(res.data);
            // let arrKey = Object.keys(res.data[0]);
            // let arrTitle = [];
            // for (let i = 0; i < arrKey.length; i++) {
            //   arrTitle.push({
            //     key: arrKey[i],
            //     label: arrKey[i]
            //   });
            // }
            // // console.log(arrTitle);
            // this.fields = arrTitle;

            // let arrTile = []
            // arrTile = Object.keys(entozh)

            let arrTitle = [];

            let resData = res.data;

            for (let i = 0; i < Object.keys(shop_zh.shop_zh).length; i++) {
              arrTitle.push({
                key: Object.keys(shop_zh.shop_zh)[i],
                label: Object.values(shop_zh.shop_zh)[i]
              });
            }

            console.log(arrTitle);

            let filterList = [
              "title_vipperson",
              "title_vipemail",
              "title_confirmdate",
              "title_viptel"
            ];

            arrTitle = arrTitle.filter(item => !filterList.includes(item.key));

            // console.log(arrTitle)

            this.fields = arrTitle;

            resData.map(item =>
              item.spcard_check == 1
                ? (item.spcard_check = "同意")
                : (item.spcard_check = "不同意")
            );

            this.items = resData;
          }
          // if (res.status == 200) {
          //   alert("数据提交成功");
          // } else {
          //   alert("填报异常，请检查后再次提交");
          // }
        })
        .catch(error => {
          console.log(error);
          alert("填报异常，请检查后再次提交");
        });

      // data默认接收剩余的属性值, 打印结果同上
      console.log(JSON.stringify(this.form));
    }
  }

  // info(item, index, button) {
  //   this.infoModal.title = `Row index: ${index}`
  //   this.infoModal.content = JSON.stringify(item, null, 2)
  //   this.$root.$emit('bv::show::modal', this.infoModal.id, button)
  // },
  // resetInfoModal() {
  //   this.infoModal.title = ''
  //   this.infoModal.content = ''
  // },
  // onFiltered(filteredItems) {
  //   // Trigger pagination to update the number of buttons/pages due to filtering
  //   this.totalRows = filteredItems.length
  //   this.currentPage = 1
  // }
};
</script>
