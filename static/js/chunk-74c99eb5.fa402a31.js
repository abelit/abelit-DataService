(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-74c99eb5"],{"22ef":function(t,e,r){"use strict";var n=r("efe2");function a(t,e){return RegExp(t,e)}e.UNSUPPORTED_Y=n((function(){var t=a("a","y");return t.lastIndex=2,null!=t.exec("abcd")})),e.BROKEN_CARET=n((function(){var t=a("^r","gy");return t.lastIndex=2,null!=t.exec("str")}))},"2eeb":function(t,e,r){"use strict";var n=r("1c8b"),a=r("5dfd").map,i=r("1ea7"),o=r("ff9c"),c=i("map"),s=o("map");n({target:"Array",proto:!0,forced:!c||!s},{map:function(t){return a(this,t,arguments.length>1?arguments[1]:void 0)}})},"44bb":function(t,e,r){"use strict";var n=r("d1be"),a=r.n(n);a.a},5139:function(t,e,r){"use strict";var n=r("99ad"),a=r("22ef"),i=RegExp.prototype.exec,o=String.prototype.replace,c=i,s=function(){var t=/a/,e=/b*/g;return i.call(t,"a"),i.call(e,"a"),0!==t.lastIndex||0!==e.lastIndex}(),u=a.UNSUPPORTED_Y||a.BROKEN_CARET,l=void 0!==/()??/.exec("")[1],f=s||l||u;f&&(c=function(t){var e,r,a,c,f=this,h=u&&f.sticky,p=n.call(f),d=f.source,v=0,g=t;return h&&(p=p.replace("y",""),-1===p.indexOf("g")&&(p+="g"),g=String(t).slice(f.lastIndex),f.lastIndex>0&&(!f.multiline||f.multiline&&"\n"!==t[f.lastIndex-1])&&(d="(?: "+d+")",g=" "+g,v++),r=new RegExp("^(?:"+d+")",p)),l&&(r=new RegExp("^"+d+"$(?!\\s)",p)),s&&(e=f.lastIndex),a=i.call(h?r:f,g),h?a?(a.input=a.input.slice(v),a[0]=a[0].slice(v),a.index=f.lastIndex,f.lastIndex+=a[0].length):f.lastIndex=0:s&&a&&(f.lastIndex=f.global?a.index+a[0].length:e),l&&a&&a.length>1&&o.call(a[0],r,(function(){for(c=1;c<arguments.length-2;c++)void 0===arguments[c]&&(a[c]=void 0)})),a}),t.exports=c},"59da":function(t,e,r){var n=r("2118"),a=r("5139");t.exports=function(t,e){var r=t.exec;if("function"===typeof r){var i=r.call(t,e);if("object"!==typeof i)throw TypeError("RegExp exec method returned something other than an Object or null");return i}if("RegExp"!==n(t))throw TypeError("RegExp#exec called on incompatible receiver");return a.call(t,e)}},"6a61":function(t,e,r){var n=function(t){"use strict";var e,r=Object.prototype,n=r.hasOwnProperty,a="function"===typeof Symbol?Symbol:{},i=a.iterator||"@@iterator",o=a.asyncIterator||"@@asyncIterator",c=a.toStringTag||"@@toStringTag";function s(t,e,r){return Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}),t[e]}try{s({},"")}catch(I){s=function(t,e,r){return t[e]=r}}function u(t,e,r,n){var a=e&&e.prototype instanceof g?e:g,i=Object.create(a.prototype),o=new R(n||[]);return i._invoke=k(t,r,o),i}function l(t,e,r){try{return{type:"normal",arg:t.call(e,r)}}catch(I){return{type:"throw",arg:I}}}t.wrap=u;var f="suspendedStart",h="suspendedYield",p="executing",d="completed",v={};function g(){}function y(){}function m(){}var x={};x[i]=function(){return this};var b=Object.getPrototypeOf,w=b&&b(b(S([])));w&&w!==r&&n.call(w,i)&&(x=w);var D=m.prototype=g.prototype=Object.create(x);function E(t){["next","throw","return"].forEach((function(e){s(t,e,(function(t){return this._invoke(e,t)}))}))}function _(t,e){function r(a,i,o,c){var s=l(t[a],t,i);if("throw"!==s.type){var u=s.arg,f=u.value;return f&&"object"===typeof f&&n.call(f,"__await")?e.resolve(f.__await).then((function(t){r("next",t,o,c)}),(function(t){r("throw",t,o,c)})):e.resolve(f).then((function(t){u.value=t,o(u)}),(function(t){return r("throw",t,o,c)}))}c(s.arg)}var a;function i(t,n){function i(){return new e((function(e,a){r(t,n,e,a)}))}return a=a?a.then(i,i):i()}this._invoke=i}function k(t,e,r){var n=f;return function(a,i){if(n===p)throw new Error("Generator is already running");if(n===d){if("throw"===a)throw i;return j()}r.method=a,r.arg=i;while(1){var o=r.delegate;if(o){var c=O(o,r);if(c){if(c===v)continue;return c}}if("next"===r.method)r.sent=r._sent=r.arg;else if("throw"===r.method){if(n===f)throw n=d,r.arg;r.dispatchException(r.arg)}else"return"===r.method&&r.abrupt("return",r.arg);n=p;var s=l(t,e,r);if("normal"===s.type){if(n=r.done?d:h,s.arg===v)continue;return{value:s.arg,done:r.done}}"throw"===s.type&&(n=d,r.method="throw",r.arg=s.arg)}}}function O(t,r){var n=t.iterator[r.method];if(n===e){if(r.delegate=null,"throw"===r.method){if(t.iterator["return"]&&(r.method="return",r.arg=e,O(t,r),"throw"===r.method))return v;r.method="throw",r.arg=new TypeError("The iterator does not provide a 'throw' method")}return v}var a=l(n,t.iterator,r.arg);if("throw"===a.type)return r.method="throw",r.arg=a.arg,r.delegate=null,v;var i=a.arg;return i?i.done?(r[t.resultName]=i.value,r.next=t.nextLoc,"return"!==r.method&&(r.method="next",r.arg=e),r.delegate=null,v):i:(r.method="throw",r.arg=new TypeError("iterator result is not an object"),r.delegate=null,v)}function L(t){var e={tryLoc:t[0]};1 in t&&(e.catchLoc=t[1]),2 in t&&(e.finallyLoc=t[2],e.afterLoc=t[3]),this.tryEntries.push(e)}function T(t){var e=t.completion||{};e.type="normal",delete e.arg,t.completion=e}function R(t){this.tryEntries=[{tryLoc:"root"}],t.forEach(L,this),this.reset(!0)}function S(t){if(t){var r=t[i];if(r)return r.call(t);if("function"===typeof t.next)return t;if(!isNaN(t.length)){var a=-1,o=function r(){while(++a<t.length)if(n.call(t,a))return r.value=t[a],r.done=!1,r;return r.value=e,r.done=!0,r};return o.next=o}}return{next:j}}function j(){return{value:e,done:!0}}return y.prototype=D.constructor=m,m.constructor=y,y.displayName=s(m,c,"GeneratorFunction"),t.isGeneratorFunction=function(t){var e="function"===typeof t&&t.constructor;return!!e&&(e===y||"GeneratorFunction"===(e.displayName||e.name))},t.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,m):(t.__proto__=m,s(t,c,"GeneratorFunction")),t.prototype=Object.create(D),t},t.awrap=function(t){return{__await:t}},E(_.prototype),_.prototype[o]=function(){return this},t.AsyncIterator=_,t.async=function(e,r,n,a,i){void 0===i&&(i=Promise);var o=new _(u(e,r,n,a),i);return t.isGeneratorFunction(r)?o:o.next().then((function(t){return t.done?t.value:o.next()}))},E(D),s(D,c,"Generator"),D[i]=function(){return this},D.toString=function(){return"[object Generator]"},t.keys=function(t){var e=[];for(var r in t)e.push(r);return e.reverse(),function r(){while(e.length){var n=e.pop();if(n in t)return r.value=n,r.done=!1,r}return r.done=!0,r}},t.values=S,R.prototype={constructor:R,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=e,this.done=!1,this.delegate=null,this.method="next",this.arg=e,this.tryEntries.forEach(T),!t)for(var r in this)"t"===r.charAt(0)&&n.call(this,r)&&!isNaN(+r.slice(1))&&(this[r]=e)},stop:function(){this.done=!0;var t=this.tryEntries[0],e=t.completion;if("throw"===e.type)throw e.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var r=this;function a(n,a){return c.type="throw",c.arg=t,r.next=n,a&&(r.method="next",r.arg=e),!!a}for(var i=this.tryEntries.length-1;i>=0;--i){var o=this.tryEntries[i],c=o.completion;if("root"===o.tryLoc)return a("end");if(o.tryLoc<=this.prev){var s=n.call(o,"catchLoc"),u=n.call(o,"finallyLoc");if(s&&u){if(this.prev<o.catchLoc)return a(o.catchLoc,!0);if(this.prev<o.finallyLoc)return a(o.finallyLoc)}else if(s){if(this.prev<o.catchLoc)return a(o.catchLoc,!0)}else{if(!u)throw new Error("try statement without catch or finally");if(this.prev<o.finallyLoc)return a(o.finallyLoc)}}}},abrupt:function(t,e){for(var r=this.tryEntries.length-1;r>=0;--r){var a=this.tryEntries[r];if(a.tryLoc<=this.prev&&n.call(a,"finallyLoc")&&this.prev<a.finallyLoc){var i=a;break}}i&&("break"===t||"continue"===t)&&i.tryLoc<=e&&e<=i.finallyLoc&&(i=null);var o=i?i.completion:{};return o.type=t,o.arg=e,i?(this.method="next",this.next=i.finallyLoc,v):this.complete(o)},complete:function(t,e){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&e&&(this.next=e),v},finish:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var r=this.tryEntries[e];if(r.finallyLoc===t)return this.complete(r.completion,r.afterLoc),T(r),v}},catch:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var r=this.tryEntries[e];if(r.tryLoc===t){var n=r.completion;if("throw"===n.type){var a=n.arg;T(r)}return a}}throw new Error("illegal catch attempt")},delegateYield:function(t,r,n){return this.delegate={iterator:S(t),resultName:r,nextLoc:n},"next"===this.method&&(this.arg=e),v}},t}(t.exports);try{regeneratorRuntime=n}catch(a){Function("r","regeneratorRuntime = r")(n)}},"6d20":function(t,e,r){"use strict";r.r(e);var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("div",{staticStyle:{background:"#409eff",color:"#ffffff",padding:"10px"}},[t._v(" 花果园购物中心1-每日销售情况汇报 ")]),r("el-row",[r("el-col",[r("div",{staticClass:"block"},[r("span",{staticClass:"demonstration mx-5"},[t._v("按月查询")]),r("el-date-picker",{attrs:{"value-format":"yyyy-MM-dd",type:"daterange",align:"right",placeholder:"选择日期范围","default-value":t.search.date,"picker-options":t.pickerOptions,"range-separator":" ~ "},model:{value:t.search.date,callback:function(e){t.$set(t.search,"date",e)},expression:"search.date"}}),r("el-button",{staticClass:"ma-5",attrs:{icon:"el-icon-search",circle:"",disabled:t.disabled},on:{click:t.searchData}})],1),r("div",[r("ul",[r("li",[t._v(" 汇报时间范围： "+t._s(t.search.date[0])+" ~ "+t._s(t.search.date[1])+" ")]),r("li",[t._v(" 客流数据： "+t._s(t.trafficData.alltraffics)+" (人次) ")]),r("li",[t._v(" 单日客流("+t._s(t.search.date[1])+")： "+t._s(t.trafficData.daytraffics)+" (人次) ")]),r("li",[t._v(" A8POS机安装量： "+t._s(t.saleData.posa8)+" (台) ")]),r("li",[t._v(" W280PPOS机安装量： "+t._s(t.saleData.posw280p)+" (台) ")]),r("li",[t._v(" 期间使用量： "+t._s(t.saleData.posusage)+" (台) ")]),r("li",[t._v(" 期间POS机收入： "+t._s(t.saleData.possale)+" (元) ")]),r("li",[t._v(" 期间系统总收入： "+t._s(t.saleData.totalsale)+" (元) ")]),r("li",[t._v(" "+t._s(t.search.date[1])+"未进行销售补录商户共"+t._s(t.saleData.inputsale.length)+"家(已撤铺的商铺可忽略)： ")]),r("div",t._l(t.saleData.inputsale,(function(e){return r("p",{key:e.scode},[t._v(" "+t._s(e.scode)+" --- "+t._s(e.sname)+" ")])})),0)])])])],1)],1)},a=[];r("b4fb"),r("9302"),r("2eeb"),r("e50e"),r("e18c"),r("e35a"),r("9cf3"),r("6a61");function i(t,e,r,n,a,i,o){try{var c=t[i](o),s=c.value}catch(u){return void r(u)}c.done?e(s):Promise.resolve(s).then(n,a)}function o(t){return function(){var e=this,r=arguments;return new Promise((function(n,a){var o=t.apply(e,r);function c(t){i(o,n,a,c,s,"next",t)}function s(t){i(o,n,a,c,s,"throw",t)}c(void 0)}))}}var c=r("1462"),s=r("a340"),u=r("bb06"),l=r("9691"),f=r("0372"),h=r("e4a1"),p=r("82ae"),d=r.n(p),v=function(t){Object(u["a"])(r,t);var e=Object(l["a"])(r);function r(){var t;return Object(c["a"])(this,r),t=e.apply(this,arguments),t.search={date:[],beginDate:"",endDate:""},t.pickerOptions={shortcuts:[{text:"今天",onClick:function(t){var e=new Date;e.setHours(23,59,59);var r=new Date(e);r.setTime(e.getTime()-864e5+1e3),t.$emit("pick",[r,e])}},{text:"最近一周",onClick:function(t){var e=new Date,r=new Date;e.setHours(23,59,59),r.setTime(e.getTime()-6048e5+1e3),t.$emit("pick",[r,e])}},{text:"最近一个月",onClick:function(t){var e=new Date,r=new Date;e.setHours(23,59,59),r.setTime(e.getTime()-2592e6+1e3),t.$emit("pick",[r,e])}}]},t.loading=!1,t.disabled=!1,t.initDate=new Date,t.saleData={posa8:0,posw280p:0,inputsale:[],posusage:0,possale:0,totalsale:0},t.trafficData={alltraffics:0,daytraffics:0},t}return Object(s["a"])(r,[{key:"mounted",value:function(){this.getSaleata(this.search.beginDate,this.search.endDate),this.getTrafficData(this.search.beginDate,this.search.endDate)}},{key:"created",value:function(){this.search.beginDate=this.handleTimeOld(1==this.initDate.getDate()?new Date(this.initDate-864e5):this.initDate,"-"),this.search.endDate=this.handleTimeNew(new Date(this.initDate-864e5)),this.search.date.push(this.search.beginDate),this.search.date.push(this.search.endDate)}},{key:"searchData",value:function(){console.log(this.search),this.getSaleata(this.search.beginDate,this.search.endDate),this.getTrafficData(this.search.beginDate,this.search.endDate)}},{key:"handleTimeOld",value:function(t,e){var r=this,n=new Date(t),a=n.getFullYear(),i=n.getMonth()+1;return e="-",[a,i,1].map((function(t){return r.formatNumber(t)})).join(e)}},{key:"handleTimeNew",value:function(t){var e=new Date(t),r=e.getFullYear(),n=e.getMonth()+1>10?e.getMonth()+1:"0"+(e.getMonth()+1),a=e.getDate()>10?e.getDate():"0"+e.getDate();return"".concat(r,"-").concat(n,"-").concat(a)}},{key:"formatNumber",value:function(t){return String(t)[1]?String(t):"0".concat(t)}},{key:"getSaleata",value:function(){var t=o(regeneratorRuntime.mark((function t(e,r){var n=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return this.disabled=!0,this.loading=!0,t.next=4,d.a.get("http://58.42.231.98:5060/api/ptraffic/sales",{params:{start:e,end:r}}).then((function(t){200==t.status&&(console.log(t.data),n.saleData=t.data)}))["catch"]((function(t){console.log(t)}))["finally"]((function(){n.disabled=!1}));case 4:case"end":return t.stop()}}),t,this)})));function e(e,r){return t.apply(this,arguments)}return e}()},{key:"getTrafficData",value:function(){var t=o(regeneratorRuntime.mark((function t(e,r){var n=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return this.disabled=!0,this.loading=!0,t.next=4,d.a.get("http://58.42.231.98:5060/api/ptraffic/traffics",{params:{start:e,end:r}}).then((function(t){200==t.status&&(console.log(t.data),n.trafficData=t.data)}))["catch"]((function(t){console.log(t)}))["finally"]((function(){n.disabled=!1}));case 4:case"end":return t.stop()}}),t,this)})));function e(e,r){return t.apply(this,arguments)}return e}()}]),r}(h["c"]);v=Object(f["a"])([h["a"]],v);var g=v,y=g,m=(r("44bb"),r("9ca4")),x=Object(m["a"])(y,n,a,!1,null,null,null);e["default"]=x.exports},9302:function(t,e,r){"use strict";var n=r("1c8b"),a=r("692f"),i=r("da10"),o=r("d7e1"),c=[].join,s=a!=Object,u=o("join",",");n({target:"Array",proto:!0,forced:s||!u},{join:function(t){return c.call(i(this),void 0===t?",":t)}})},"9cf3":function(t,e,r){"use strict";var n=r("b2a2"),a=r("857c"),i=r("2732"),o=r("9d5c"),c=r("59da");n("search",1,(function(t,e,r){return[function(e){var r=i(this),n=void 0==e?void 0:e[t];return void 0!==n?n.call(e,r):new RegExp(e)[t](String(r))},function(t){var n=r(e,t,this);if(n.done)return n.value;var i=a(t),s=String(this),u=i.lastIndex;o(u,0)||(i.lastIndex=0);var l=c(i,s);return o(i.lastIndex,u)||(i.lastIndex=u),null===l?-1:l.index}]}))},"9d5c":function(t,e){t.exports=Object.is||function(t,e){return t===e?0!==t||1/t===1/e:t!=t&&e!=e}},b2a2:function(t,e,r){"use strict";r("e35a");var n=r("1944"),a=r("efe2"),i=r("90fb"),o=r("5139"),c=r("0fc1"),s=i("species"),u=!a((function(){var t=/./;return t.exec=function(){var t=[];return t.groups={a:"7"},t},"7"!=="".replace(t,"$<a>")})),l=function(){return"$0"==="a".replace(/./,"$0")}(),f=i("replace"),h=function(){return!!/./[f]&&""===/./[f]("a","$0")}(),p=!a((function(){var t=/(?:)/,e=t.exec;t.exec=function(){return e.apply(this,arguments)};var r="ab".split(t);return 2!==r.length||"a"!==r[0]||"b"!==r[1]}));t.exports=function(t,e,r,f){var d=i(t),v=!a((function(){var e={};return e[d]=function(){return 7},7!=""[t](e)})),g=v&&!a((function(){var e=!1,r=/a/;return"split"===t&&(r={},r.constructor={},r.constructor[s]=function(){return r},r.flags="",r[d]=/./[d]),r.exec=function(){return e=!0,null},r[d](""),!e}));if(!v||!g||"replace"===t&&(!u||!l||h)||"split"===t&&!p){var y=/./[d],m=r(d,""[t],(function(t,e,r,n,a){return e.exec===o?v&&!a?{done:!0,value:y.call(e,r,n)}:{done:!0,value:t.call(r,e,n)}:{done:!1}}),{REPLACE_KEEPS_$0:l,REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE:h}),x=m[0],b=m[1];n(String.prototype,t,x),n(RegExp.prototype,d,2==e?function(t,e){return b.call(t,this,e)}:function(t){return b.call(t,this)})}f&&c(RegExp.prototype[d],"sham",!0)}},b4fb:function(t,e,r){"use strict";var n=r("1c8b"),a=r("efe2"),i=r("74e7"),o=r("a719"),c=r("3553"),s=r("d88d"),u=r("1bbd"),l=r("1ca1"),f=r("1ea7"),h=r("90fb"),p=r("f594"),d=h("isConcatSpreadable"),v=9007199254740991,g="Maximum allowed index exceeded",y=p>=51||!a((function(){var t=[];return t[d]=!1,t.concat()[0]!==t})),m=f("concat"),x=function(t){if(!o(t))return!1;var e=t[d];return void 0!==e?!!e:i(t)},b=!y||!m;n({target:"Array",proto:!0,forced:b},{concat:function(t){var e,r,n,a,i,o=c(this),f=l(o,0),h=0;for(e=-1,n=arguments.length;e<n;e++)if(i=-1===e?o:arguments[e],x(i)){if(a=s(i.length),h+a>v)throw TypeError(g);for(r=0;r<a;r++,h++)r in i&&u(f,h,i[r])}else{if(h>=v)throw TypeError(g);u(f,h++,i)}return f.length=h,f}})},d1be:function(t,e,r){},e35a:function(t,e,r){"use strict";var n=r("1c8b"),a=r("5139");n({target:"RegExp",proto:!0,forced:/./.exec!==a},{exec:a})}}]);
//# sourceMappingURL=chunk-74c99eb5.fa402a31.js.map