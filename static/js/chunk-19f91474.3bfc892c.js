(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-19f91474"],{2047:function(t,e,a){"use strict";a.r(e);var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticStyle:{background:"#409eff",color:"#ffffff",padding:"10px"}},[t._v(" 花果园购物中心1-各入口客流去年同期对比统计(全天) ")]),a("el-row",[a("el-col",[a("div",{staticClass:"block"},[a("span",{staticClass:"demonstration mx-5"},[t._v("按月查询")]),a("el-date-picker",{attrs:{type:"month",placeholder:"选择月"},model:{value:t.value2,callback:function(e){t.value2=e},expression:"value2"}}),a("el-button",{staticClass:"ma-5",attrs:{icon:"el-icon-search",circle:"",disabled:t.disabled},on:{click:t.btn}}),a("el-button",{attrs:{type:"primary"},on:{click:t.exportExcel}},[t._v("导出")])],1)])],1),a("el-row",[a("el-col",[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],attrs:{data:t.tableData,"show-summary":"","summary-method":t.getSummaries,id:"export-table"}},[a("el-table-column",{attrs:{type:"index",width:"70",label:"序号"}}),a("el-table-column",{attrs:{prop:"pdate",label:"日期",width:"120",formatter:t.dateFormat}}),a("el-table-column",{attrs:{label:"花果园购物中心1-各入口客流去年同期对比统计(全天)"}},[a("el-table-column",{attrs:{prop:"psquare",label:"沿湖广场",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"psquare_last",label:"沿湖广场(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"phm",label:"H&M",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"phm_last",label:"H&M(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pgateway_lz",label:"人行天桥(乐转旁)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pgateway_lz_last",label:"人行天桥(乐转旁)(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pgateway_b",label:"人行天桥(必胜客旁)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pgateway_b_last",label:"人行天桥(必胜客旁)(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pkfc",label:"肯德基",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pkfc_last",label:"肯德基(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pqbj",label:"一楼黔宝金店旁",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pqbj_last",label:"一楼黔宝金店旁(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pck",label:"CKJeans",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pck_last",label:"CKJeans(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"prest",label:"食尚汇门厅旁",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"prest_last",label:"食尚汇门厅旁(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"ppark",label:"停车场",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"ppark_last",label:"停车场(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pone",label:"一期天桥",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pone_last",label:"一期天桥(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"eone",label:"E区天桥",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"eone_last",label:"E区天桥(去年同期)",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pall",label:"总计",formatter:t.numberFormat,width:"100"}}),a("el-table-column",{attrs:{prop:"pall_last",label:"总计(去年同期)",formatter:t.numberFormat,width:"100"}})],1)],1)],1)],1)],1)},l=[],n=(a("f390"),a("8601"),a("cc16"),a("df47"),a("a8aa"),a("2885"),a("aef1"),a("4016"),a("7d72"),a("bc4a"),a("c12e"),a("e967"),a("b66b"),a("48d1"),a("85a2"),a("0e4d")),o=a("94ef"),p=a("76ff"),s=a("3a68"),u=a("fd63"),m=a("e4a1"),i=a("82ae"),b=a.n(i),c=a("b9ef"),d=a("31bf"),f=a.n(d),w=a("c886"),h=a.n(w),_=function(t){Object(p["a"])(a,t);var e=Object(s["a"])(a);function a(){var t;return Object(n["a"])(this,a),t=e.apply(this,arguments),t.value2=new Date,t.loading=!1,t.disabled=!1,t.tableData=[],t.titleLabel=" 客流(人次)/10:00~22:00",t.pickerOptions={disabledDate:function(t){return t.getTime()>=Date.now()}},t}return Object(o["a"])(a,[{key:"renderheader",value:function(t,e){var a=e.column;e.$index;return t("span",{},[t("span",{},a.label.split("/")[0]),t("br"),t("span",{},a.label.split("/")[1])])}},{key:"exportExcel",value:function(){var t=h.a.utils.table_to_book(document.querySelector("#export-table"),{raw:!0}),e=this.formatDate(this.re_month(this.value2)[0]).split("-"),a=h.a.write(t,{bookType:"xlsx",bookSST:!0,type:"array"});try{f.a.saveAs(new Blob([a],{type:"application/octet-stream"}),"trafficContrast"+e[0]+e[1]+".xlsx")}catch(r){"undefined"!==typeof console&&console.log(r,a)}return a}},{key:"thousandSeparator",value:function(t){return t&&(-1!=t.toString().indexOf(".")?t.toString().replace(/(\d)(?=(\d{3})+\.)/g,(function(t,e){return e+","})):t.toString().replace(/(\d)(?=(\d{3})+\b)/g,(function(t,e){return e+","})))}},{key:"btn",value:function(){this.getData(this.formatDate(this.re_month(this.value2)[0]),this.formatDate(this.re_month(this.value2)[1]))}},{key:"mounted",value:function(){}},{key:"getData",value:function(t,e){var a=this;this.disabled=!0,this.loading=!0,b.a.get("http://58.42.231.98:8860/api/ptraffic/compare",{params:{start:t,end:e}}).then((function(t){200==t.status&&(a.tableData=[],t.data.forEach((function(t,e){new Date("2020-01-24")<new Date(t.pdate)&&new Date(t.pdate)<new Date("2020-05-16")&&(t.pgateway_b=0,t.pkfc=0,t.prest=0),new Date("2020-01-24")<new Date(t.pdate)&&new Date(t.pdate)<new Date("2020-05-24")&&(t.pck=0,t.pqbj=0),new Date("2020-01-24")<new Date(t.pdate)&&new Date(t.pdate)<new Date("2020-05-16")&&(t.pgateway_b_last=0,t.pkfc_last=0,t.prest_last=0),new Date("2020-01-24")<new Date(t.pdate)&&new Date(t.pdate)<new Date("2020-05-24")&&(t.pck_last=0,t.pqbj_last=0),t.pall=t.psquare+t.phm+t.pgateway_lz+t.pgateway_b+t.pkfc+t.prest+t.ppark+t.pck+t.pqbj+t.pone+t.eone,t.pall_last=t.psquare_last+t.phm_last+t.pgateway_lz_last+t.pgateway_b_last+t.pkfc_last+t.prest_last+t.ppark_last+t.pck_last+t.pqbj_last+t.pone_last+t.eone_last})),a.tableData=t.data,a.loading=!1,a.disabled=!1)}))["catch"]((function(t){console.log(t),a.disabled=!1}))}},{key:"formatDate",value:function(t){var e=t,a=""+(e.getMonth()+1),r=""+e.getDate(),l=e.getFullYear();return a.length<2&&(a="0"+a),r.length<2&&(r="0"+r),[l,a,r].join("-")}},{key:"getSummaries",value:function(t){var e=t.columns,a=t.data,r=[];return e.forEach((function(t,e){if(0!==e){var l=a.map((function(e){return Number(e[t.property])}));return l.every((function(t){return isNaN(t)}))?r[e]="N/A":(r[e]=l.reduce((function(t,e){var a=Number(e);return isNaN(a)?t:t+e}),0),r[e]=r[e].toLocaleString()),r}r[e]="总计"})),r}},{key:"tableRowClassName",value:function(t){var e=t.row;t.rowIndex;return e["tbdata"].replace(",","")>=5e3?"warning-row":""}},{key:"re_month",value:function(t){var e=[],a=(new Date,t.getMonth()),r=t.getFullYear(),l=new Date(r,a,1),n=new Date(r,a+1,0);return e=[l,n],e}},{key:"dateFormat",value:function(t,e,a){var r=Date.parse(a),l=["周一","周二","周三","周四","周五","周六","周日"];return a?c["format"](new Date(r-288e5),"yyyy-MM-dd")+" ("+l[new Date(r-288e5).getUTCDay()]+")":""}},{key:"numberFormat",value:function(t,e,a){return a.toLocaleString()}}]),a}(m["c"]);_=Object(u["a"])([m["a"]],_);var v=_,y=v,g=(a("ac4a"),a("5d22")),k=Object(g["a"])(y,r,l,!1,null,null,null);e["default"]=k.exports},"459e":function(t,e,a){},ac4a:function(t,e,a){"use strict";a("459e")}}]);
//# sourceMappingURL=chunk-19f91474.3bfc892c.js.map