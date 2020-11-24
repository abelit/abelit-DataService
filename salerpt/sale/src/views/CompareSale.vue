<template>
  <div>
    <div class="search-panel">
      <a-button
        type="primary"
        @click="expandAll(isExpanded)"
        class="expand-item"
      >
        {{ isExpanded ? "收起所有行" : "展开所有行" }}
      </a-button>
      <a-input
        v-model:value="storeName"
        placeholder="店铺名称"
        class="content-item"
      />
      <a-range-picker v-model:value="dateValue" class="date-item" />
      <a-button type="primary" @click="getStoreSale">
        <template #icon><SearchOutlined /></template>
      </a-button>
    </div>
    <div>
      <a-table
        :columns="columns"
        :data-source="data"
        :expandedRowKeys="defaultExpandedRowKeys"
        bordered
        @expand="onExpand"
        :expandRowByClick="true"
        class="components-table-demo-nested"
      >
        <template #expandedRowRender="{text,record, index}">
          <a-table
            :columns="innerColumns"
            :data-source="record.idata"
            :pagination="false"
          >
            <template
              v-for="col in [
                'goodsname',
                'goodscode',
                'possale',
                'comparesale',
                'misinput',
                'missale',
                'minput',
                'realsale',
                'goodsstate',
              ]"
              #[col]="{ text: inputText, record: inputRecord, index: inputIndex }"
            >
              <div :key="col">
                <a-input
                  v-if="inputRecord.editable"
                  style="margin: -5px 0"
                  :value="inputText"
                  @change="
                    (e) =>
                      handleChange(
                        record.key,
                        inputRecord.key,
                        e.target.value,
                        col
                      )
                  "
                  :disabled="col == 'minput'"
                />
                <template v-else> {{ inputText }} </template>
              </div>
            </template>
            <template
              #operation="{ text: innerText, record: innerRecord, index: innerIndex }"
            >
              <div class="editable-row-operations">
                <span v-if="innerRecord.editable">
                  <a @click="save(record.key, innerRecord.key)">保存</a>
                  <a @click="cancel(record.key, innerRecord.key)">取消</a>
                </span>
                <span v-else>
                  <a
                    v-bind="editingKey !== '' ? { disabled: 'disabled' } : {}"
                    @click="edit(record.key, innerRecord.key)"
                  >
                    <!-- <EditFilled /> -->
                    <a-button
                      :type="editingKey !== '' ? 'dashed' : 'primary'"
                      v-bind="editingKey !== '' ? { disabled: 'disabled' } : {}"
                    >
                      <template #icon>
                        <EditFilled />
                      </template>
                    </a-button>
                  </a>
                </span>
              </div>
            </template>
          </a-table>
        </template>
      </a-table>
    </div>
  </div>
</template>
<script>
import { EditFilled } from "@ant-design/icons-vue";
import { SearchOutlined } from "@ant-design/icons-vue";
import moment from "moment";
import { getCurrentInstance } from "vue";
const columns = [
  { title: "店铺名称", dataIndex: "name", key: "name" },
  { title: "店铺编号", dataIndex: "code", key: "code" },
  { title: "销售日期", dataIndex: "saledate", key: "saledate" },
  { title: "销售总额", dataIndex: "saleamount", key: "saleamount" },
  { title: "业绩状态", dataIndex: "status", key: "status" },
  { title: "调整状态", dataIndex: "updatestatus", key: "updatestatus" },
];

const data = [
  {
    key: 0,
    name: "科技眼镜",
    code: "107101",
    saledate: "2020-11-01",
    saleamount: 500,
    status: "正常",
    updatestatus: "已调整",
    idata: [
      {
        key: 0,
        goodsname: "科技货品1",
        goodscode: "K001",
        possale: 300,
        comparesale: 100,
        misinput: 50,
        missale: 300,
        minput: 500,
        realsale: null,
        goodsstate: "正常",
      },
      {
        key: 1,
        goodsname: "科技货品2",
        goodscode: "K002",
        possale: 300,
        comparesale: 100,
        misinput: 50,
        missale: 300,
        minput: 500,
        realsale: null,
        goodsstate: "正常",
      },
    ],
  },
  {
    key: 1,
    name: "科技眼镜",
    code: "107101",
    saledate: "2020-11-02",
    saleamount: 600,
    status: "正常",
    updatestatus: "已调整",
    idata: [
      {
        key: 0,
        goodsname: "科技货品2",
        goodscode: "K002",
        possale: 300,
        comparesale: 100,
        misinput: 50,
        missale: 300,
        minput: 500,
        realsale: null,
        goodsstate: "正常",
      },
    ],
  },
  {
    key: 2,
    name: "周大福",
    code: "207101",
    saledate: "2020-11-01",
    saleamount: 700,
    status: "正常",
    updatestatus: "已调整",
    idata: [
      {
        key: 0,
        goodsname: "周大福货品1",
        goodscode: "Z001",
        possale: 300,
        comparesale: 100,
        misinput: 50,
        missale: 300,
        minput: 500,
        realsale: null,
        goodsstate: "正常",
      },
    ],
  },
];

const innerColumns = [
  { title: "货品名称", dataIndex: "goodsname", key: "goodsname" },
  { title: "货品编码", dataIndex: "goodscode", key: "goodscode" },

  { title: "POS销售", dataIndex: "possale", key: "possale" },
  { title: "程序补差", dataIndex: "comparesale", key: "comparesale" },
  { title: "MIS补录", dataIndex: "misinput", key: "misinput" },
  { title: "MIS", dataIndex: "missale", key: "missale" },
  { title: "商户补录", dataIndex: "minput", key: "minput" },
  {
    title: "实际销售",
    dataIndex: "realsale",
    key: "realsale",
    slots: { customRender: "realsale" },
  },
  { title: "货品销售状态", dataIndex: "goodsstate", key: "goodsstate" },
  {
    title: "业绩调整操作",
    dataIndex: "operation",
    key: "operation",
    slots: { customRender: "operation" },
  },
];

export default {
  components: {
    EditFilled,
    SearchOutlined,
  },
  data() {
    // // 嵌套对象会导致内部对象无法进行深度拷贝
    // this.cacheData = data.map(item => ({ ...item }));
    // 使用JSON进行深度拷贝
    this.cacheData = JSON.parse(JSON.stringify(data));
    return {
      data,
      columns,
      innerColumns,
      editingKey: "",
      // defaultExpandAllRows: false,
      defaultExpandedRowKeys: [],
      isExpanded: false,
      storeName: null,
      dateValue: null,
      dateFormat: "YYYY-MM-DD",
    };
  },
  methods: {
    expandAll(param) {
      if (param) {
        this.defaultExpandedRowKeys = [];
      } else {
        this.defaultExpandedRowKeys = [...Array(data.length).keys()];
      }
      this.isExpanded = !this.isExpanded;
    },
    onExpand(expanded, record){//绑定的点击行事件
        console.log(this)
    },
    handleChange(fkey, ckey, value, column) {
      const newData = [...this.data];
      const target = newData[fkey].idata[ckey];
      if (target) {
        target[column] = value;
        this.data = newData;
      }
    },
    edit(fkey, ckey) {
      const newData = [...this.data];
      const target = newData[fkey].idata[ckey];
      this.editingKey = ckey;
      if (target) {
        target.editable = true;
        this.data = newData;
      }
    },
    save(fkey, ckey) {
      const newData = [...this.data];
      const newCacheData = [...this.cacheData];
      const target = newData[fkey].idata[ckey];
      const targetCache = newCacheData[fkey].idata[ckey];
      if (target && targetCache) {
        delete target.editable;
        this.data = newData;
        Object.assign(targetCache, target);
        this.cacheData = newCacheData;
      }
      this.editingKey = "";
    },
    cancel(fkey, ckey) {
      const newData = [...this.data];
      const target = newData[fkey].idata[ckey];
      console.log(target);
      this.editingKey = "";
      if (target) {
        Object.assign(target, this.cacheData[fkey].idata[ckey]);
        delete target.editable;
        this.data = newData;
      }
      console.log(this.cacheData);
    },
    getStoreSale() {
      console.log(moment(this.dateValue[0]).format(this.dateFormat));
      console.log(moment(this.dateValue[1]).format(this.dateFormat));
      console.log(this.storeName);
    },
    getCurrentMonth(day) {
      const date = new Date();
      if (day == 1) {
        return new Date(date.getFullYear(), date.getMonth(), 1);
      }

      if (day == -1) {
        return new Date(date.getFullYear(), date.getMonth() + 1, 0);
      }
      return new Date();
    },
    moment,
  },
  created() {
    this.dateValue = [
      moment(this.getCurrentMonth(1), this.dateFormat),
      moment(this.getCurrentMonth(-1), this.dateFormat),
    ];
  },
};
</script>

<style scoped lang="less">
.editable-row-operations a {
  margin-right: 8px;
}
.search-panel {
  .expand-item {
  }
  .content-item {
    width: 180px;
    margin-left: 20px;
    margin-right: 20px;
  }
  .date-item {
    margin-right: 20px;
  }
}
</style>
