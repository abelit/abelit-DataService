(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-d29b3c5e"],{"4d9a":function(t,e,a){"use strict";a.r(e);var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticStyle:{background:"#409EFF",color:"#ffffff",padding:"10px"}},[t._v("花果园购物中心1-疫情期各入口客流统计")]),a("el-row",[a("el-col",[a("div",{staticClass:"block"},[a("span",{staticClass:"demonstration mx-5"},[t._v("按月查询")]),a("el-date-picker",{attrs:{type:"month",placeholder:"选择月"},model:{value:t.value2,callback:function(e){t.value2=e},expression:"value2"}}),a("el-button",{staticClass:"ma-5",attrs:{icon:"el-icon-search",circle:"",disabled:t.disabled},on:{click:t.btn}}),a("el-button",{attrs:{type:"primary"},on:{click:t.exportExcel}},[t._v("导出")])],1)])],1),a("el-row",[a("el-col",[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],staticStyle:{width:"1192px"},attrs:{data:t.tableData,"show-summary":"","summary-method":t.getSummaries,id:"export-table"}},[a("el-table-column",{attrs:{type:"index",width:"70",label:"序号"}}),a("el-table-column",{attrs:{prop:"pdate",label:"日期",width:"120",formatter:t.dateFormat}}),a("el-table-column",{attrs:{label:"花果园购物中心1-疫情期各入口客流统计"}},[a("el-table-column",{attrs:{prop:"psquare",label:"沿湖广场",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"phm",label:"H&M",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pgateway",label:"人行天桥(乐转旁)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pgatewaypiz",label:"人行天桥(必胜客旁)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pkfc",label:"肯德基",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pqbj",label:"一楼黔宝金店旁",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pck",label:"CKJeans",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"prest",label:"食尚汇门厅旁",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pparking",label:"停车场",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pall",label:"总计",formatter:t.numberFormat,width:"100"}})],1)],1)],1)],1)],1)},n=[],l=(a("76b0"),a("5cff"),a("4ec5"),a("7f64"),a("957b"),a("4538"),a("665e"),a("41c2"),a("65ba"),a("4d20"),a("6a22"),a("8d56"),a("80cf"),a("5f89"),a("dcd4"),a("0e4d")),o=a("94ef"),i=a("76ff"),u=a("3a68"),c=a("fd63"),p=a("e4a1"),s=a("82ae"),b=a.n(s),d=a("b9ef"),m=a("31bf"),f=a.n(m),h=a("c886"),w=a.n(h),v=function(t){Object(i["a"])(a,t);var e=Object(u["a"])(a);function a(){var t;return Object(l["a"])(this,a),t=e.apply(this,arguments),t.value2=new Date,t.loading=!1,t.disabled=!1,t.tableData=[],t.titleLabel=" 客流(人次)/10:00~22:00",t.pickerOptions={disabledDate:function(t){return t.getTime()>=Date.now()}},t}return Object(o["a"])(a,[{key:"renderheader",value:function(t,e){var a=e.column;e.$index;return t("span",{},[t("span",{},a.label.split("/")[0]),t("br"),t("span",{},a.label.split("/")[1])])}},{key:"exportExcel",value:function(){var t=w.a.utils.table_to_book(document.querySelector("#export-table")),e=w.a.write(t,{bookType:"xlsx",bookSST:!0,type:"array"});try{f.a.saveAs(new Blob([e],{type:"application/octet-stream"}),"trafficMonth.xlsx")}catch(a){"undefined"!==typeof console&&console.log(a,e)}return e}},{key:"thousandSeparator",value:function(t){return t&&(-1!=t.toString().indexOf(".")?t.toString().replace(/(\d)(?=(\d{3})+\.)/g,(function(t,e){return e+","})):t.toString().replace(/(\d)(?=(\d{3})+\b)/g,(function(t,e){return e+","})))}},{key:"btn",value:function(){this.getData(this.formatDate(this.re_month(this.value2)[0]),this.formatDate(this.re_month(this.value2)[1]))}},{key:"mounted",value:function(){}},{key:"getData",value:function(t,e){var a=this;this.disabled=!0,this.loading=!0,b.a.get("http://58.42.231.98:5060/api/ptraffic/date",{params:{start:t,end:e}}).then((function(t){200==t.status&&(a.tableData=[],t.data.forEach((function(t,e){new Date(t.pdate)<new Date("2020-05-16")&&(t.pgatewaypiz=0,t.pkfc=0,t.prest=0),new Date(t.pdate)<new Date("2020-05-24")&&(t.pck=0,t.pqbj=0),t.pall=t.psquare+t.phm+t.pgateway+t.pgatewaypiz+t.pkfc+t.prest+t.pparking+t.pck+t.pqbj})),a.tableData=t.data,a.loading=!1,a.disabled=!1)}))["catch"]((function(t){console.log(t),a.disabled=!1}))}},{key:"formatDate",value:function(t){var e=t,a=""+(e.getMonth()+1),r=""+e.getDate(),n=e.getFullYear();return a.length<2&&(a="0"+a),r.length<2&&(r="0"+r),[n,a,r].join("-")}},{key:"getSummaries",value:function(t){var e=t.columns,a=t.data,r=[];return e.forEach((function(t,e){if(0!==e){var n=a.map((function(e){return Number(e[t.property])}));return n.every((function(t){return isNaN(t)}))?r[e]="N/A":(r[e]=n.reduce((function(t,e){var a=Number(e);return isNaN(a)?t:t+e}),0),r[e]=r[e].toLocaleString()),r}r[e]="总计"})),r}},{key:"tableRowClassName",value:function(t){var e=t.row;t.rowIndex;return e["tbdata"].replace(",","")>=5e3?"warning-row":""}},{key:"re_month",value:function(t){var e=[],a=(new Date,t.getMonth()),r=t.getFullYear(),n=new Date(r,a,1),l=new Date(r,a+1,0);return e=[n,l],e}},{key:"dateFormat",value:function(t,e,a){var r=Date.parse(a),n=["周一","周二","周三","周四","周五","周六","周日"];return a?d["format"](new Date(r-288e5),"yyyy-MM-dd")+" ("+n[new Date(r-288e5).getUTCDay()]+")":""}},{key:"numberFormat",value:function(t,e,a){return a.toLocaleString()}}]),a}(p["c"]);v=Object(c["a"])([p["a"]],v);var g=v,y=g,k=(a("bc14"),a("5d22")),D=Object(k["a"])(y,r,n,!1,null,null,null);e["default"]=D.exports},ae00:function(t,e,a){},bc14:function(t,e,a){"use strict";a("ae00")}}]);
//# sourceMappingURL=chunk-d29b3c5e.b713937e.js.map