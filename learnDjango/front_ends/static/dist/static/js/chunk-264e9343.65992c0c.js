(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-264e9343"],{"046e":function(t,e,s){"use strict";var n=s("0e94"),i=s.n(n);i.a},"0ba3":function(t,e,s){t.exports=s.p+"static/img/avatar.9ecfb832.jpg"},"0e94":function(t,e,s){},"1a9e":function(t,e,s){"use strict";var n=s("c39e"),i=s.n(n);i.a},"855c":function(t,e,s){},bfe9:function(t,e,s){"use strict";s.r(e);var n=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"wrapper"},[s("v-head"),s("v-sidebar"),s("div",{staticClass:"content-box",class:{"content-collapse":t.collapse}},[s("v-tags"),s("div",{staticClass:"content"},[s("transition",{attrs:{name:"move",mode:"out-in"}},[s("keep-alive",{attrs:{include:t.tagsList}},[s("router-view")],1)],1)],1)],1)],1)},i=[],l=(s("7cfd"),function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"header"},[s("div",{staticClass:"collapse-btn",on:{click:t.collapseChage}},[s("i",{staticClass:"el-icon-menu"})]),s("div",{staticClass:"logo"},[t._v("自动化测试平台")]),s("div",{staticClass:"header-right"},[s("div",{staticClass:"header-user-con"},[s("div",{staticClass:"btn-fullscreen",on:{click:t.handleFullScreen}},[s("el-tooltip",{attrs:{effect:"dark",content:t.fullscreen?"取消全屏":"全屏",placement:"bottom"}},[s("i",{staticClass:"el-icon-rank"})])],1),t._m(0),s("el-dropdown",{staticClass:"user-name",attrs:{trigger:"hover"},on:{command:t.handleCommand}},[s("span",{staticClass:"el-dropdown-link"},[t._v("\n                    "+t._s(t.username)+" "),s("i",{staticClass:"el-icon-caret-bottom"})]),s("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[s("el-dropdown-item",{attrs:{divided:"",command:"logout"}},[t._v("退出登录")])],1)],1)],1)])])}),a=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"user-avator"},[n("img",{attrs:{src:s("0ba3")}})])}],o=s("6e6d"),c=new o["default"],r=c,u={data:function(){return{collapse:!1,fullscreen:!1,name:"野柠檬"}},computed:{username:function(){var t=sessionStorage.getItem("username")||localStorage.getItem("username");return t||this.name}},methods:{handleCommand:function(t){"logout"==t&&(sessionStorage.clear(),localStorage.clear(),this.$router.push("/login"))},collapseChage:function(){this.collapse=!this.collapse,r.$emit("collapse",this.collapse)},handleFullScreen:function(){var t=document.documentElement;this.fullscreen?document.exitFullscreen?document.exitFullscreen():document.webkitCancelFullScreen?document.webkitCancelFullScreen():document.mozCancelFullScreen?document.mozCancelFullScreen():document.msExitFullscreen&&document.msExitFullscreen():t.requestFullscreen?t.requestFullscreen():t.webkitRequestFullScreen?t.webkitRequestFullScreen():t.mozRequestFullScreen?t.mozRequestFullScreen():t.msRequestFullscreen&&t.msRequestFullscreen(),this.fullscreen=!this.fullscreen}},mounted:function(){document.body.clientWidth<1500&&this.collapseChage()}},d=u,h=(s("046e"),s("6691")),m=Object(h["a"])(d,l,a,!1,null,"0184e27a",null),p=m.exports,f=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"sidebar"},[s("el-menu",{staticClass:"sidebar-el-menu",attrs:{"default-active":t.onRoutes,collapse:t.collapse,"background-color":"#324157","text-color":"#bfcbd9","active-text-color":"#20a0ff","unique-opened":"",router:""}},[t._l(t.items,(function(e){return[e.subs?[s("el-submenu",{key:e.index,attrs:{index:e.index}},[s("template",{slot:"title"},[s("i",{class:e.icon}),s("span",{attrs:{slot:"title"},slot:"title"},[t._v(t._s(e.title))])]),t._l(e.subs,(function(e){return[e.subs?s("el-submenu",{key:e.index,attrs:{index:e.index}},[s("template",{slot:"title"},[t._v(t._s(e.title))]),t._l(e.subs,(function(e,n){return s("el-menu-item",{key:n,attrs:{index:e.index}},[t._v("\n                                "+t._s(e.title)+"\n                            ")])}))],2):s("el-menu-item",{key:e.index,attrs:{index:e.index}},[t._v("\n                            "+t._s(e.title)+"\n                        ")])]}))],2)]:[s("el-menu-item",{key:e.index,attrs:{index:e.index}},[s("i",{class:e.icon}),s("span",{attrs:{slot:"title"},slot:"title"},[t._v(t._s(e.title))])])]]}))],2)],1)},g=[],v={data:function(){return{collapse:!1,items:[{icon:"el-icon-lx-home",index:"dashboard",title:"系统首页"},{icon:"el-icon-s-claim",index:"1",title:"项目管理",subs:[{index:"projects_list",title:"项目列表"},{index:"projects_add",title:"项目新增"}]},{icon:"el-icon-s-open",index:"2",title:"环境管理",subs:[{index:"envs_list",title:"环境列表"},{index:"envs_add",title:"环境新增"}]},{icon:"el-icon-s-tools",index:"3",title:"内置函数",subs:[{index:"builtin_list",title:"函数列表"}]},{icon:"el-icon-lx-tag",index:"4",title:"接口管理",subs:[{index:"interfaces_list",title:"接口列表"},{index:"interfaces_add",title:"接口新增"}]},{icon:"el-icon-lx-hot",index:"8",title:"用例管理",subs:[{index:"testcases_list",title:"用例列表"},{index:"testcases_add",title:"用例新增"}]},{icon:"el-icon-lx-apps",index:"10",title:"配置管理",subs:[{index:"configures_list",title:"配置列表"},{index:"configures_add",title:"配置新增"}]},{icon:"el-icon-files",index:"13",title:"套件管理",subs:[{index:"testsuites_list",title:"套件列表"},{index:"testsuites_add",title:"套件新增"}]},{icon:"el-icon-s-marketing",index:"16",title:"报告管理",subs:[{index:"reports_list",title:"报告列表"}]}]}},computed:{onRoutes:function(){return this.$route.path}},created:function(){var t=this;r.$on("collapse",(function(e){t.collapse=e}))}},x=v,_=(s("1a9e"),Object(h["a"])(x,f,g,!1,null,"3215117a",null)),b=_.exports,C=function(){var t=this,e=t.$createElement,s=t._self._c||e;return t.showTags?s("div",{staticClass:"tags"},[s("ul",t._l(t.tagsList,(function(e,n){return s("li",{key:n,staticClass:"tags-li",class:{active:t.isActive(e.path)}},[s("router-link",{staticClass:"tags-li-title",attrs:{to:e.path}},[t._v("\n                "+t._s(e.title)+"\n            ")]),s("span",{staticClass:"tags-li-icon",on:{click:function(e){return t.closeTags(n)}}},[s("i",{staticClass:"el-icon-close"})])],1)})),0),s("div",{staticClass:"tags-close-box"},[s("el-dropdown",{on:{command:t.handleTags}},[s("el-button",{attrs:{size:"mini",type:"primary"}},[t._v("\n                标签选项"),s("i",{staticClass:"el-icon-arrow-down el-icon--right"})]),s("el-dropdown-menu",{attrs:{slot:"dropdown",size:"small"},slot:"dropdown"},[s("el-dropdown-item",{attrs:{command:"other"}},[t._v("关闭其他")]),s("el-dropdown-item",{attrs:{command:"all"}},[t._v("关闭所有")])],1)],1)],1)]):t._e()},w=[],$={data:function(){return{tagsList:[]}},methods:{isActive:function(t){return t===this.$route.fullPath},closeTags:function(t){var e=this.tagsList.splice(t,1)[0],s=this.tagsList[t]?this.tagsList[t]:this.tagsList[t-1];s?e.path===this.$route.fullPath&&this.$router.push(s.path):this.$router.push("/")},closeAll:function(){this.tagsList=[],this.$router.push("/")},closeOther:function(){var t=this,e=this.tagsList.filter((function(e){return e.path===t.$route.fullPath}));this.tagsList=e},setTags:function(t){var e=this.tagsList.some((function(e){return e.path===t.fullPath}));e||(this.tagsList.length>=8&&this.tagsList.shift(),this.tagsList.push({title:t.meta.title,path:t.fullPath,name:t.matched[1].components.default.name})),r.$emit("tags",this.tagsList)},handleTags:function(t){"other"===t?this.closeOther():this.closeAll()}},computed:{showTags:function(){return this.tagsList.length>0}},watch:{$route:function(t,e){t.name!==e.name&&this.setTags(t)}},created:function(){var t=this;this.setTags(this.$route),r.$on("close_current_tags",(function(){for(var e=0,s=t.tagsList.length;e<s;e++){var n=t.tagsList[e];if(n.path===t.$route.fullPath){e<s-1?t.$router.push(t.tagsList[e+1].path):e>0?t.$router.push(t.tagsList[e-1].path):t.$router.push("/"),t.tagsList.splice(e,1);break}}}))}},k=$,L=(s("c5f3"),Object(h["a"])(k,C,w,!1,null,null,null)),F=L.exports,S={data:function(){return{tagsList:[],collapse:!1}},components:{vHead:p,vSidebar:b,vTags:F},created:function(){var t=this;r.$on("collapse",(function(e){t.collapse=e})),r.$on("tags",(function(e){for(var s=[],n=0,i=e.length;n<i;n++)e[n].name&&s.push(e[n].name);t.tagsList=s}))}},T=S,q=Object(h["a"])(T,n,i,!1,null,null,null);e["default"]=q.exports},c39e:function(t,e,s){},c5f3:function(t,e,s){"use strict";var n=s("855c"),i=s.n(n);i.a}}]);