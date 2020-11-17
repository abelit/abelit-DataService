<template>
  <a-table
    :columns="columns"
    :data-source="data"
    class="components-table-demo-nested"
  >
    <template #expandedRowRender="{text,record, index}">
      <a-table
        :columns="innerColumns"
        :data-source="innerData.filter(item => item.code == record.code && item.saledate == record.saledate)"
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
          #[col]="{ text, record, index }"
        >
          <div :key="col">
            <a-input
              v-if="record.editable"
              style="margin: -5px 0"
              :value="text"
              @change="(e) => handleChange(e.target.value, record.key, col)"
              :disabled="col == 'minput'"
            />
            <template v-else> {{ text }}</template>
          </div>
        </template>
        <template #operation="{ text, record, index }">
          <div class="editable-row-operations">
            <span v-if="record.editable">
              <a @click="save(record.key)">Save</a>
              <a-popconfirm
                title="Sure to cancel?"
                @confirm="cancel(record.key)"
              >
                <a>Cancel</a>
              </a-popconfirm>
            </span>
            <span v-else>
              <a
                v-bind="editingKey !== '' ? { disabled: 'disabled' } : {}"
                @click="edit(record.key)"
              >
                <!-- <EditFilled /> -->
                <a-button :type="editingKey !== '' ? 'dashed': 'primary'" v-bind="editingKey !== '' ? { disabled: 'disabled' } : {}">
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
</template>
<script>
import { EditFilled } from "@ant-design/icons-vue";
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
    key: 1,
    name: "科技眼镜",
    code: "107101",
    saledate: "2020-11-01",
    saleamount: 500,
    status: "正常",
    updatestatus: "已调整",
  },
  {
    key: 2,
    name: "科技眼镜",
    code: "107101",
    saledate: "2020-11-02",
    saleamount: 600,
    status: "正常",
    updatestatus: "已调整",
  }
,
{
    key: 3,
    name: "周大福",
    code: "207101",
    saledate: "2020-11-01",
    saleamount: 700,
    status: "正常",
    updatestatus: "已调整",
  }
];

const innerColumns = [
  { title: "货品名称", dataIndex: "goodsname", key: "goodsname" },
  { title: "货品编码", dataIndex: "goodscode", key: "goodscode" },

  { title: "POS销售", dataIndex: "possale", key: "possale" },
  { title: "程序补差", dataIndex: "comparesale", key: "comparesale" },
  { title: "MIS补录", dataIndex: "misinput", key: "misinput" },
  { title: "MIS", dataIndex: "missale", key: "missale" },
  { title: "商户补录", dataIndex: "minput", key: "minput" },
  { title: "实际销售", dataIndex: "realsale", key: "realsale",slots: { customRender: "realsale" } },
  { title: "货品销售状态", dataIndex: "goodsstate", key: "goodsstate" },
  {
    title: "业绩调整操作",
    dataIndex: "operation",
    key: "operation",
    slots: { customRender: "operation" },
  },
];

const innerData = [
  {
    key: 1,
    goodsname: "科技货品1",
    goodscode: "K001",
    possale: 300,
    comparesale: 100,
    misinput: 50,
    missale: 300,
    minput: 500,
    realsale: null,
    goodsstate: "正常",
    code: '107101',
    saledate: '2020-11-01',
  },
  {
    key: 2,
    goodsname: "科技货品2",
    goodscode: "K002",
    possale: 300,
    comparesale: 100,
    misinput: 50,
    missale: 300,
    minput: 500,
    realsale: null,
    goodsstate: "正常",
    code: '107101',
    saledate: '2020-11-01',
  },

  {
    key: 3,
    goodsname: "周大福货品1",
    goodscode: "Z001",
    possale: 300,
    comparesale: 100,
    misinput: 50,
    missale: 300,
    minput: 500,
    realsale: null,
    goodsstate: "正常",
    code: '207101',
    saledate: '2020-11-01',
  }
];


export default {
  components: {
    EditFilled,
  },
  data() {
    this.cacheData = innerData.map((item) => ({ ...item }));
    return {
      data,
      columns,
      innerColumns,
      innerData,
      editingKey: "",
    };
  },
  methods: {
    handleChange(value, key, column) {
      const newData = [...this.innerData];
      const target = newData.filter((item) => key === item.key)[0];
      if (target) {
        target[column] = value;
        this.innerData = newData;
      }
    },
    edit(key) {
      const newData = [...this.innerData];
      const target = newData.filter((item) => key === item.key)[0];
      this.editingKey = key;
      if (target) {
        target.editable = true;
        this.innerData = newData;
      }
    },
    save(key) {
      const newData = [...this.innerData];
      const newCacheData = [...this.cacheData];
      const target = newData.filter((item) => key === item.key)[0];
      const targetCache = newCacheData.filter((item) => key === item.key)[0];
      if (target && targetCache) {
        delete target.editable;
        this.innerData = newData;
        Object.assign(targetCache, target);
        this.cacheData = newCacheData;
      }
      this.editingKey = "";
      console.log(target)
    },
    cancel(key) {
      const newData = [...this.innerData];
      const target = newData.filter((item) => key === item.key)[0];
      this.editingKey = "";
      if (target) {
        Object.assign(
          target,
          this.cacheData.filter((item) => key === item.key)[0]
        );
        delete target.editable;
        this.innerData = newData;
      }
    },
    // expand(expanded,record) {
    //   this.expandedRowKeys = [] // 重置展开节点，只展开当前点击的节点（内部数据调用模板，无法做到同时几个内层表格数据直接缓存在页面）
    //   // if (expanded) {
    //   // this.expandedRowKeys = [record.dict_id]
    //   // this.getDictItem() // 获取表格内部数据
    //   // }
    //   console.log(expanded, record)
    //   if (expanded) {
    //     this.innerData = this.innerData.filter(item => item.code == record.code && item.saledate == record.saledate)
    //   }
    // }
  },
};
</script>

<style scoped>
.editable-row-operations a {
  margin-right: 8px;
}
</style>
