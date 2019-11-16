(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-482730fc"],{"0290":function(t,n,e){"use strict";e.r(n);var r=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{staticClass:"login-wrap"},[e("div",{staticClass:"ms-login"},[e("div",{staticClass:"ms-title"},[t._v("用户登录")]),e("el-form",{ref:"ruleForm",staticClass:"ms-content",attrs:{model:t.ruleForm,rules:t.rules}},[e("el-form-item",{attrs:{prop:"username"}},[e("el-input",{attrs:{placeholder:"请输入用户名"},on:{focus:function(n){return t.clearValidate("username")}},model:{value:t.ruleForm.username,callback:function(n){t.$set(t.ruleForm,"username",n)},expression:"ruleForm.username"}},[e("el-button",{attrs:{slot:"prepend",icon:"el-icon-lx-people"},slot:"prepend"})],1)],1),e("el-form-item",{attrs:{prop:"password"}},[e("el-input",{attrs:{type:"password",placeholder:"请输入密码"},on:{focus:function(n){return t.clearValidate("password")}},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&t._k(n.keyCode,"enter",13,n.key,"Enter")?null:t.submitForm("ruleForm")}},model:{value:t.ruleForm.password,callback:function(n){t.$set(t.ruleForm,"password",n)},expression:"ruleForm.password"}},[e("el-button",{attrs:{slot:"prepend",icon:"el-icon-lx-lock"},slot:"prepend"})],1)],1),e("el-form-item",{staticClass:"remember_me",attrs:{label:"记住我",size:"mini"}},[e("el-switch",{model:{value:t.ruleForm.remember_me,callback:function(n){t.$set(t.ruleForm,"remember_me",n)},expression:"ruleForm.remember_me"}}),e("el-link",{staticClass:"register_link",attrs:{type:"info",underline:!1,href:"/register"}},[t._v("没有账号？点击注册")])],1),e("div",{staticClass:"login-btn"},[e("el-button",{attrs:{type:"primary"},on:{click:function(n){return t.submitForm("ruleForm")}}},[t._v("登录")])],1),e("p",{directives:[{name:"show",rawName:"v-show",value:t.err_info,expression:"err_info"}],staticClass:"login-tips"},[t._v(t._s(t.err_msg))])],1)],1)])},u=[],o=e("4ec3"),c={data:function(){return{ruleForm:{username:"",password:"",remember_me:!1},err_info:!1,err_msg:"",rules:{username:[{required:!0,message:"请输入用户名",trigger:"blur"}],password:[{required:!0,message:"请输入密码",trigger:"blur"}]}}},methods:{submitForm:function(t){var n=this;this.$refs[t].validate((function(t){if(!t)return n.err_msg="参数有误",n.err_info=!0,!1;var e=n;Object(o["D"])(n.ruleForm).then((function(t){e.remember_me?(sessionStorage.clear(),localStorage.token=t.data.token,localStorage.user_id=t.data.user_id,localStorage.username=t.data.username):(localStorage.clear(),sessionStorage.token=t.data.token,sessionStorage.user_id=t.data.user_id,sessionStorage.username=t.data.username),e.$router.push({name:"index"})})).catch((function(t){"non_field_errors"in t&&400==t.status_code&&(e.err_msg="用户名或密码错误"),t.response?e.err_msg="服务器异常":t.request&&(e.err_msg="网络异常"),e.err_info=!0}))}))},clearValidate:function(t){this.$refs["ruleForm"].clearValidate(t)}}},a=c,s=(e("31d3"),e("6691")),i=Object(s["a"])(a,r,u,!1,null,"ba0c1ed4",null);n["default"]=i.exports},"31d3":function(t,n,e){"use strict";var r=e("6562"),u=e.n(r);u.a},"4ec3":function(t,n,e){"use strict";e.d(n,"D",(function(){return c})),e.d(n,"G",(function(){return a})),e.d(n,"k",(function(){return s})),e.d(n,"j",(function(){return i})),e.d(n,"E",(function(){return f})),e.d(n,"q",(function(){return l})),e.d(n,"v",(function(){return d})),e.d(n,"d",(function(){return p})),e.d(n,"F",(function(){return m})),e.d(n,"x",(function(){return g})),e.d(n,"M",(function(){return _})),e.d(n,"h",(function(){return v})),e.d(n,"g",(function(){return b})),e.d(n,"i",(function(){return k})),e.d(n,"C",(function(){return w})),e.d(n,"p",(function(){return F})),e.d(n,"u",(function(){return h})),e.d(n,"c",(function(){return z})),e.d(n,"L",(function(){return y})),e.d(n,"S",(function(){return j})),e.d(n,"s",(function(){return x})),e.d(n,"f",(function(){return C})),e.d(n,"A",(function(){return S})),e.d(n,"V",(function(){return $})),e.d(n,"O",(function(){return O})),e.d(n,"B",(function(){return V})),e.d(n,"R",(function(){return q})),e.d(n,"r",(function(){return E})),e.d(n,"l",(function(){return J})),e.d(n,"Q",(function(){return D})),e.d(n,"e",(function(){return N})),e.d(n,"N",(function(){return T})),e.d(n,"z",(function(){return A})),e.d(n,"U",(function(){return B})),e.d(n,"K",(function(){return G})),e.d(n,"H",(function(){return H})),e.d(n,"I",(function(){return I})),e.d(n,"J",(function(){return K})),e.d(n,"m",(function(){return L})),e.d(n,"n",(function(){return M})),e.d(n,"a",(function(){return P})),e.d(n,"y",(function(){return Q})),e.d(n,"T",(function(){return R})),e.d(n,"w",(function(){return U})),e.d(n,"o",(function(){return W})),e.d(n,"t",(function(){return X})),e.d(n,"b",(function(){return Y})),e.d(n,"P",(function(){return Z}));var r=e("f753"),u=e.n(r),o="http://49.235.177.249:9000",c=function(t){return u.a.post("".concat(o,"/user/login/"),t)},a=function(t){return u.a.post("".concat(o,"/user/register/"),t)},s=function(t){return u.a.get("".concat(o,"/user/")+t+"/count/")},i=function(t){return u.a.get("".concat(o,"/user/")+t+"/count/")},f=function(t){return u.a.get("".concat(o,"/projects/?page=")+t.page+"&size="+t.size)},l=function(t){return u.a.delete("".concat(o,"/projects/")+t+"/")},d=function(t,n){return u.a.put("".concat(o,"/projects/")+t+"/",n)},p=function(t){return u.a.post("".concat(o,"/projects/"),t)},m=function(){return u.a.get("".concat(o,"/projects/names/"))},g=function(){return u.a.get("".concat(o,"/envs/names/"))},_=function(t,n){return u.a.post("".concat(o,"/projects/")+t+"/run/",{env_id:n})},v=function(t){return u.a.get("".concat(o,"/debugtalks/?page=")+t.page+"&size="+t.size)},b=function(t){return u.a.get("".concat(o,"/debugtalks/")+t+"/")},k=function(t,n){return u.a.put("".concat(o,"/debugtalks/")+t+"/",{debugtalk:n})},w=function(t){return u.a.get("".concat(o,"/interfaces/?page=")+t.page+"&size="+t.size)},F=function(t){return u.a.delete("".concat(o,"/interfaces/")+t+"/")},h=function(t,n){return u.a.put("".concat(o,"/interfaces/")+t+"/",n)},z=function(t){return u.a.post("".concat(o,"/interfaces/"),t)},y=function(t,n){return u.a.post("".concat(o,"/interfaces/")+t+"/run/",{env_id:n})},j=function(t){return u.a.get("".concat(o,"/testsuites/?page=")+t.page+"&size="+t.size)},x=function(t){return u.a.delete("".concat(o,"/testsuites/")+t+"/")},C=function(t){return u.a.post("".concat(o,"/testsuites/"),t)},S=function(t){return u.a.get("".concat(o,"/testsuites/")+t+"/")},$=function(t,n){return u.a.put("".concat(o,"/testsuites/")+t+"/",n)},O=function(t,n){return u.a.post("".concat(o,"/testsuites/")+t+"/run/",{env_id:n})},V=function(t){return u.a.get("".concat(o,"/projects/")+t+"/interfaces/")},q=function(t){return u.a.get("".concat(o,"/testcases/?page=")+t.page+"&size="+t.size)},E=function(t){return u.a.delete("".concat(o,"/testcases/")+t+"/")},J=function(t){return u.a.get("".concat(o,"/interfaces/")+t+"/configs/")},D=function(t){return u.a.get("".concat(o,"/interfaces/")+t+"/testcases/")},N=function(t){return u.a.post("".concat(o,"/testcases/"),t)},T=function(t,n){return u.a.post("".concat(o,"/testcases/")+t+"/run/",{env_id:n})},A=function(t){return u.a.get("".concat(o,"/testcases/")+t+"/")},B=function(t,n){return u.a.put("".concat(o,"/testcases/")+t+"/",n)},G=function(t){return u.a.get("".concat(o,"/reports/?page=")+t.page+"&size="+t.size)},H=function(t){return u.a.delete("".concat(o,"/reports/")+t+"/")},I=function(t){return u.a.get("".concat(o,"/reports/")+t+"/download/",{responseType:"blob"})},K=function(t){return u.a.get("".concat(o,"/reports/")+t+"/")},L=function(t){return u.a.get("".concat(o,"/configures/?page=")+t.page+"&size="+t.size)},M=function(t){return u.a.delete("".concat(o,"/configures/")+t+"/")},P=function(t){return u.a.post("".concat(o,"/configures/"),t)},Q=function(t){return u.a.get("".concat(o,"/configures/")+t+"/")},R=function(t,n){return u.a.put("".concat(o,"/configures/")+t+"/",n)},U=function(t){return u.a.get("".concat(o,"/envs/?page=")+t.page+"&size="+t.size)},W=function(t){return u.a.delete("".concat(o,"/envs/")+t+"/")},X=function(t,n){return u.a.put("".concat(o,"/envs/")+t+"/",n)},Y=function(t){return u.a.post("".concat(o,"/envs/"),t)},Z=function(){return u.a.get("".concat(o,"/summary/"))}},6562:function(t,n,e){}}]);