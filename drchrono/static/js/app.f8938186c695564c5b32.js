webpackJsonp([1],{"0Esk":function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-layout",{attrs:{row:""}},[n("v-flex",{attrs:{xs4:"","offset-xs4":""}},[n("v-card",[n("v-card-title",{attrs:{"primary-title":""}},[n("div",[n("div",{staticClass:"headline"},[t._v("Doctor Login Form")]),t._v(" "),n("span",{staticClass:"grey--text"},[t._v("Please fill out your credentials below.")])])]),t._v(" "),n("v-layout",{staticClass:"bottom",attrs:{row:""}},[n("v-flex",{staticClass:"space"},[n("v-btn",{attrs:{secondary:"",large:"",href:t.login}},[t._v("Login with DrChrono")])],1)],1)],1)],1)],1)},i=[],a={render:s,staticRenderFns:i};e.a=a},"6CT3":function(t,e,n){"use strict";function s(t){n("tiR/")}var i=n("cusF"),a=n("6lEA"),o=n("VU/8"),r=s,c=o(i.a,a.a,r,"data-v-be3f2ce6",null);e.a=c.exports},"6lEA":function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"upper"},[t._v("\n    "+t._s(t.status)+" "),n("span",{staticClass:"lower"},[t._v("for ::")]),t._v("\n     "+t._s(t.days)+" Day"+t._s(1!==t.days?"s":"")+" : \n     "+t._s(t.hours)+" Hour"+t._s(1!==t.hours?"s":"")+" : \n     "+t._s(t.minutes)+" Minute"+t._s(1!==t.minutes?"s":"")+" : \n     "+t._s(t.seconds)+" Second"+t._s(1!==t.seconds?"s":"")+"\n")])},i=[],a={render:s,staticRenderFns:i};e.a=a},BkMU:function(t,e){},GQJu:function(t,e,n){"use strict";var s=n("Gu7T"),i=n.n(s),a=n("eqa6"),o=n("6CT3");e.a={name:"appointments",components:{timer:o.a},data:function(){return{doctors:[],doctor:void 0,appointments:{arrived:[],confirmed:[],finished:[],avg_wait:-1}}},mounted:function(){this.getDoctors(),setInterval(this.getDoctors,3e5)},computed:{doctorNames:function(){return this.doctors.map(function(t,e){return{text:t.first+" "+t.last,value:t}})},toggleStatus:function(){return this.doctor&&"O"===this.doctor.status_code?"I":"O"},statusText:function(){return this.doctor&&"O"===this.doctor.status_code?"Login":"Logout"},arrived:function(){return this.appointments.arrived&&this.appointments.arrived.length>0},confirmed:function(){return this.appointments.confirmed&&this.appointments.confirmed.length>0},finished:function(){return this.appointments.finished&&this.appointments.finished.length>0}},methods:{getAppointments:function(){var t=this;this.doctor&&a.a.getAppointments(this.doctor.id).then(function(e){t.appointments=e})},getDoctors:function(){var t=this;a.a.doctors().then(function(e){if(t.doctors=[].concat(i()(e.checked_in),i()(e.checked_out)),!t.doctor){var n=Math.floor(Math.random()*t.doctors.length);t.doctor=t.doctors[n],t.getAppointments()}})},visit:function(t){var e=this;a.a.visit({appointment_id:t}).then(function(t){e.getAppointments()})},updateStatus:function(){var t=this;a.a.updateDoctorStatus({doctor_id:this.doctor.id,status:this.toggleStatus}).then(function(e){t.doctor.status=e.status,t.doctor.status_code=e.status_code})}},watch:{doctor:function(){this.getAppointments()}}}},LpN7:function(t,e,n){"use strict";function s(t){n("BkMU")}var i=n("pz6b"),a=n("baIP"),o=n("VU/8"),r=s,c=o(i.a,a.a,r,"data-v-e1467db2",null);e.a=c.exports},M93x:function(t,e,n){"use strict";function s(t){n("PmHi")}var i=n("xJD8"),a=n("yK4V"),o=n("VU/8"),r=s,c=o(i.a,a.a,r,null,null);e.a=c.exports},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=n("7+uW"),i=n("M93x"),a=n("YaEn"),o=n("3EgV"),r=n.n(o);s.a.use(r.a),s.a.config.productionTip=!1,new s.a({el:"#app",router:a.a,template:"<App/>",components:{App:i.a}})},PmHi:function(t,e){},R59Z:function(t,e,n){"use strict";var s=n("eqa6"),i=n("ciEJ"),a=n("LpN7");e.a={name:"kiosk",components:{doctors:i.a,patient:a.a},data:function(){return{doctors:{checked_in:[],checked_out:[]},selectedDoctor:void 0,alert:!1,alertMsg:"",alertType:"error",loggedIn:s.a.loggedIn}},mounted:function(){this.getDoctors(),setInterval(this.getDoctors,3e5)},methods:{getDoctors:function(){var t=this;s.a.doctors().then(function(e){t.doctors=e})},selectDoctor:function(t){this.selectedDoctor=t},unSelectDoctor:function(){this.selectedDoctor=void 0},sendAlert:function(t,e){var n=this;this.alertType=t,this.alertMsg=e,this.alert=!0,setTimeout(function(){n.alert=!1},5e3)}}}},T20o:function(t,e){},YaEn:function(t,e,n){"use strict";var s=n("7+uW"),i=n("/ocq"),a=n("toJX"),o=n("kh0m"),r=n("yAaf");s.a.use(i.a),e.a=new i.a({routes:[{path:"/kiosk",name:"Kiosk",component:a.a},{path:"/login",name:"Login",component:o.a},{path:"/appointments",name:"Appointments",component:r.a},{path:"*",redirect:"/kiosk"}]})},apBB:function(t,e){},baIP:function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-card",[n("v-card-title",{attrs:{"primary-title":""}},[n("div",[n("div",{staticClass:"headline"},[t._v("Patient Form: Dr. "+t._s(t.doctor.last))]),t._v(" "),n("span",{staticClass:"grey--text"},[t._v("Please fill out the information below to check-in. Thank you.")])])]),t._v(" "),n("v-layout",{staticClass:"top generationParams",attrs:{row:""}},[n("v-flex",{staticClass:"space",attrs:{xs3:""}},[n("v-text-field",{attrs:{label:"First Name:"},model:{value:t.patient.first,callback:function(e){t.patient.first=e},expression:"patient.first"}})],1),t._v(" "),n("v-flex",{staticClass:"space",attrs:{xs3:""}},[n("v-text-field",{attrs:{label:"Last Name:"},model:{value:t.patient.last,callback:function(e){t.patient.last=e},expression:"patient.last"}})],1),t._v(" "),n("v-flex",{staticClass:"space",attrs:{xs3:""}},[n("v-text-field",{attrs:{label:"SSN:"},model:{value:t.patient.ssn,callback:function(e){t.patient.ssn=e},expression:"patient.ssn"}})],1)],1),t._v(" "),t.verified?n("v-layout",{staticClass:"generationParams",attrs:{row:""}},[n("v-flex",{staticClass:"space",attrs:{xs3:""}},[n("v-text-field",{attrs:{label:"City:"},model:{value:t.patient.city,callback:function(e){t.patient.city=e},expression:"patient.city"}})],1),t._v(" "),n("v-flex",{staticClass:"space",attrs:{xs3:""}},[n("v-text-field",{attrs:{label:"State:"},model:{value:t.patient.state,callback:function(e){t.patient.state=e},expression:"patient.state"}})],1),t._v(" "),n("v-flex",{staticClass:"space",attrs:{xs3:""}},[n("v-text-field",{attrs:{label:"Ethnicity:"},model:{value:t.patient.ethnicity,callback:function(e){t.patient.ethnicity=e},expression:"patient.ethnicity"}})],1)],1):t._e(),t._v(" "),n("v-layout",{staticClass:"bottom",attrs:{row:""}},[n("v-flex",{staticClass:"space"},[n("v-btn",{attrs:{secondary:"",loading:t.loading,disabled:t.loading},on:{click:function(e){t.submitAction()}}},[t._v(t._s(t.submitText))])],1),t._v(" "),n("v-flex",{staticClass:"space"},[n("v-btn",{attrs:{secondary:""},on:{click:function(e){t.clear()}}},[t._v("Close")])],1)],1)],1)],1)},i=[],a={render:s,staticRenderFns:i};e.a=a},cPfH:function(t,e,n){"use strict";var s=n("6CT3");e.a={name:"doctors",props:{doctors:Array,title:String,disabled:{type:Boolean,default:!1},action:{type:Function,default:function(t){}}},components:{timer:s.a}}},ciEJ:function(t,e,n){"use strict";var s=n("cPfH"),i=n("di7X"),a=n("VU/8"),o=a(s.a,i.a,null,null,null);e.a=o.exports},cusF:function(t,e,n){"use strict";var s=n("INCx"),i=n.n(s);e.a={name:"timer",props:{status:String,start:String},data:function(){return{elapsed:0}},mounted:function(){this.timeDiff(),setInterval(this.timeDiff,1e3)},methods:{timeDiff:function(){this.elapsed=new Date-new Date(this.start)}},computed:{seconds:function(){return i()(this.elapsed/1e3)%60},minutes:function(){return i()(this.elapsed/1e3/60)%60},hours:function(){return i()(this.elapsed/1e3/60/60)%24},days:function(){return i()(this.elapsed/1e3/60/60/24)}}}},di7X:function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-list",{attrs:{subheader:""}},[n("v-subheader",[t._v(t._s(t.title))]),t._v(" "),t._l(t.doctors,function(e,s){return n("v-list-tile",{key:s,attrs:{disabled:t.disabled},on:{click:function(n){t.action(e)}}},[n("v-list-tile-content",[n("v-list-tile-title",[t._v(" Dr. "+t._s(e.last)+" ("+t._s(e.first)+")")]),t._v(" "),n("v-list-tile-sub-title",[n("timer",{attrs:{start:e.time,status:e.status}})],1)],1)],1)})],2)},i=[],a={render:s,staticRenderFns:i};e.a=a},eqa6:function(t,e,n){"use strict";var s=n("//Fk"),i=n.n(s),a=n("mtWM"),o=n.n(a),r=n("lbHh"),c=n.n(r);o.a.defaults.withCredentials=!0;var l=function(){return console.log(c.a.get()),c.a.get("sessionid")},u=function(t,e){return{method:"post",url:"/"+e,data:t,headers:{"X-CSRFToken":c.a.get("csrftoken")}}},d=function(){return o.a.get("/doctors").then(function(t){return t.data})},v=function(){return c.a.get("csrftoken")?new i.a(function(t,e){t(c.a.get("csrftoken"))}):o.a.get("/get-token/").then(function(t){c.a.set("csrftoken",t.data.token)})},f=function(t){return v().then(function(){return o()(u(t,"appointment/verify/")).then(function(t){return t.data}).catch(function(t){console.log(t)})})},p=function(t){return o.a.get("/appointment/"+t+"/").then(function(t){return t.data})},h=function(t){return v().then(function(){return o()(u(t,"appointment/visit/")).then(function(t){return t.data}).catch(function(t){console.log(t)})})},_=function(t){return v().then(function(){return o()(u(t,"doctor/status/")).then(function(t){return t.data}).catch(function(t){console.log(t)})})},m=function(t){return v().then(function(){return o()(u(t,"appointment/finalize/")).then(function(t){return t.data}).catch(function(t){console.log(t)})})};e.a={doctors:d,verifyAppointment:f,getAppointments:p,finalizeCheckin:m,updateDoctorStatus:_,loggedIn:l,visit:h,host:"/",login:"/login/drchrono/"}},hJnq:function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-layout",{staticClass:"content",attrs:{row:"",wrap:""}},[n("v-flex",[n("h1",[t._v("Check-in Kiosk")])])],1),t._v(" "),n("v-layout",{attrs:{row:"",wrap:""}},[n("v-flex",{attrs:{xs4:"","offset-xs4":""}},[n("v-card",[n("doctors",{attrs:{doctors:t.doctors.checked_in,title:"Doctors Available",action:t.selectDoctor}}),t._v(" "),n("v-divider"),t._v(" "),t.selectedDoctor?t._e():n("doctors",{attrs:{doctors:t.doctors.checked_out,title:"Doctors Unavailable",disabled:!0}})],1),t._v(" "),t.selectedDoctor?n("patient",{attrs:{doctor:t.selectedDoctor,action:t.sendAlert,close:t.unSelectDoctor}}):t._e(),t._v(" "),n("v-alert",{attrs:{success:"success"===t.alertType,error:"error"===t.alertType,info:"info"===t.alertType,value:t.alert,transition:"scale-transition"}},[t._v("\n        "+t._s(t.alertMsg)+"\n      ")])],1)],1)],1)},i=[],a={render:s,staticRenderFns:i};e.a=a},k0pg:function(t,e,n){"use strict";var s=n("eqa6");e.a={name:"login",data:function(){return{first:"",last:"",login:s.a.login}}}},kh0m:function(t,e,n){"use strict";function s(t){n("apBB")}var i=n("k0pg"),a=n("0Esk"),o=n("VU/8"),r=s,c=o(i.a,a.a,r,"data-v-65acf041",null);e.a=c.exports},pz6b:function(t,e,n){"use strict";var s=n("Dd8w"),i=n.n(s),a=n("eqa6");e.a={name:"patient",props:{doctor:Object,action:Function,close:Function},data:function(){return{patient:{first:"",last:"",ssn:"",city:"",state:"",ethnicity:""},verified:!1,loading:!1}},computed:{submitText:function(){return this.verified?"Finalize / Complete":"Submit"}},methods:{submitAction:function(){this.verified?this.finalize():this.verify()},verify:function(){var t=this;this.loading=!0,a.a.verifyAppointment({first:this.patient.first,last:this.patient.last,ssn:this.patient.ssn,doctor_id:this.doctor.id}).then(function(e){t.verified="error"!==e.status,t.verified&&(t.patient=i()({},e.patient,{appointment:e.appointment})),t.action(e.status,e.message),t.loading=!1})},finalize:function(){var t=this;this.loading=!0,a.a.finalizeCheckin({city:this.patient.city,state:this.patient.state,ethnicity:this.patient.ethnicity,appointment:this.patient.appointment}).then(function(e){t.verified="error"!==e.status,t.action(e.status,e.message),t.loading=!1,t.clear()})},clear:function(){this.patient={first:"",last:"",ssn:"",city:"",state:"",ethnicity:""},this.verified=!1,this.close()}}}},"tiR/":function(t,e){},toJX:function(t,e,n){"use strict";var s=n("R59Z"),i=n("hJnq"),a=n("VU/8"),o=a(s.a,i.a,null,null,null);e.a=o.exports},vKlE:function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-layout",{staticClass:"content",attrs:{row:"",wrap:""}},[n("v-flex",[n("h1",[t._v("Appointments")])])],1),t._v(" "),n("v-layout",{attrs:{row:"",wrap:""}},[n("v-flex",{attrs:{xs4:"","offset-xs4":""}},[n("v-card",[n("v-layout",[n("v-flex",{staticClass:"top",attrs:{xs5:""}},[n("v-select",{attrs:{items:t.doctorNames,"item-value":"value",overflow:""},model:{value:t.doctor,callback:function(e){t.doctor=e},expression:"doctor"}})],1),t._v(" "),n("v-flex",{staticClass:"top",attrs:{xs5:""}},[n("v-btn",{attrs:{primary:""},on:{click:function(e){t.updateStatus()}}},[t._v(t._s(t.statusText))])],1)],1),t._v(" "),t.arrived?n("v-divider"):t._e(),t._v(" "),t.arrived?n("v-list",{attrs:{subheader:""}},[n("v-subheader",[t._v("Arrived")]),t._v(" "),t._l(t.appointments.arrived,function(e,s){return n("v-list-tile",{key:s,on:{click:function(n){t.visit(e.id)}}},[n("v-list-tile-content",[n("v-list-tile-title",[t._v(t._s(e.patient.first)+" "+t._s(e.patient.last)+": "+t._s(e.reason))]),t._v(" "),n("v-list-tile-sub-title",[n("timer",{attrs:{start:e.arrival_date,status:e.status}})],1)],1)],1)})],2):t._e(),t._v(" "),t.confirmed?n("v-divider"):t._e(),t._v(" "),t.confirmed?n("v-list",{attrs:{subheader:""}},[n("v-subheader",[t._v("Confirmed")]),t._v(" "),t._l(t.appointments.confirmed,function(e,s){return n("v-list-tile",{key:s},[n("v-list-tile-content",[n("v-list-tile-title",[t._v(t._s(e.patient.first)+" "+t._s(e.patient.last)+": "+t._s(e.reason))]),t._v(" "),n("v-list-tile-sub-title",[t._v("\n                Scheduled at: "+t._s(e.scheduled_date)+"\n              ")])],1)],1)})],2):t._e(),t._v(" "),t.finished?n("v-divider"):t._e(),t._v(" "),t.finished?n("v-list",{attrs:{subheader:""}},[n("v-subheader",[t._v("Finished | Average wait-time: "+t._s((t.appointments.avg_wait/60).toFixed(2))+" minutes")]),t._v(" "),t._l(t.appointments.finished,function(e,s){return n("v-list-tile",{key:s},[n("v-list-tile-content",[n("v-list-tile-title",[t._v(t._s(e.patient.first)+" "+t._s(e.patient.last)+": "+t._s(e.reason))]),t._v(" "),n("v-list-tile-sub-title",[t._v("\n                Waited "+t._s((e.wait_time/60).toFixed(2))+" minutes\n              ")])],1)],1)})],2):t._e()],1)],1)],1)],1)},i=[],a={render:s,staticRenderFns:i};e.a=a},xJD8:function(t,e,n){"use strict";e.a={name:"app"}},yAaf:function(t,e,n){"use strict";function s(t){n("T20o")}var i=n("GQJu"),a=n("vKlE"),o=n("VU/8"),r=s,c=o(i.a,a.a,r,"data-v-4a60e2e8",null);e.a=c.exports},yK4V:function(t,e,n){"use strict";var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-app",[n("v-toolbar",{staticClass:"primary",attrs:{dark:""}},[n("v-toolbar-title",[t._v("DrChrono")]),t._v(" "),n("v-spacer"),t._v(" "),n("v-toolbar-side-icon",{staticClass:"hidden-md-and-up"}),t._v(" "),n("v-toolbar-items",{staticClass:"hidden-sm-and-down"},[n("v-btn",{attrs:{to:"/appointments/",flat:""}},[t._v("Doctors")]),t._v(" "),n("v-btn",{attrs:{to:"/kiosk/",flat:""}},[t._v("Kiosk")])],1)],1),t._v(" "),n("main",[n("v-container",{attrs:{fluid:""}},[n("router-view")],1)],1),t._v(" "),n("v-footer")],1)},i=[],a={render:s,staticRenderFns:i};e.a=a}},["NHnr"]);
//# sourceMappingURL=app.f8938186c695564c5b32.js.map