const a0_0x5b284e=a0_0x2630;function a0_0x2630(_0x48e63e,_0x3788ac){const _0x3d4422=a0_0x3d44();return a0_0x2630=function(_0x2630e5,_0x2ab58d){_0x2630e5=_0x2630e5-0x1ed;let _0xa1c48e=_0x3d4422[_0x2630e5];return _0xa1c48e;},a0_0x2630(_0x48e63e,_0x3788ac);}function a0_0x3d44(){const _0x4ca29f=['record','stringify','bus','str','571971fCngdP','get_data_from_method','get_data_model','538716ryPIHV','define','trim','4SGVfBx','datas','group_by_infos','res_id','get_parameter_infos','node','get','json_data','data_source_type_name','sql','get_data_from_json','setColumns','result_type','parse','then','name','render','limit','42XIJjYZ','do_query','json_data_format','order_by_infos','model_fields','get_model_fields','handle','77270aDSief','default_value','get_controller','6848520jVBfIk','method','push','_setValue','167104jeMrQa','311816AeDCnH','81WPFmHO','55OvABfh','setData','getParent','resolve','extend','data','code','$el','147hALUKp','model','domain','on_changing','add','field_infos','length','_rpc','get_data_from_code','1402753LZeYQL','get_data','get_data_from_sql','table'];a0_0x3d44=function(){return _0x4ca29f;};return a0_0x3d44();}(function(_0x7fb75,_0xca051f){const _0x34fab7=a0_0x2630,_0x3f2b13=_0x7fb75();while(!![]){try{const _0x5210ac=-parseInt(_0x34fab7(0x21a))/0x1*(parseInt(_0x34fab7(0x220))/0x2)+parseInt(_0x34fab7(0x1f0))/0x3*(parseInt(_0x34fab7(0x1fe))/0x4)+-parseInt(_0x34fab7(0x201))/0x5*(-parseInt(_0x34fab7(0x21d))/0x6)+parseInt(_0x34fab7(0x209))/0x7*(parseInt(_0x34fab7(0x1ff))/0x8)+-parseInt(_0x34fab7(0x200))/0x9*(-parseInt(_0x34fab7(0x1f7))/0xa)+parseInt(_0x34fab7(0x212))/0xb+-parseInt(_0x34fab7(0x1fa))/0xc;if(_0x5210ac===_0xca051f)break;else _0x3f2b13['push'](_0x3f2b13['shift']());}catch(_0x39972d){_0x3f2b13['push'](_0x3f2b13['shift']());}}}(a0_0x3d44,0xd53e1),odoo[a0_0x5b284e(0x21e)]('mana_dashboard.grid_widget',function(require){'use strict';const _0x424c98=a0_0x5b284e;var _0x446ac0=require('web.widget_registry'),_0x168fa5=require('web.Widget'),_0x4b05e1=require('web.core'),_0x318703=_0x168fa5[_0x424c98(0x205)]({'init':function(_0xf546f0,_0x1c16c4,_0x12d05e){const _0x54e0f3=_0x424c98;this._super.apply(this,arguments),this[_0x54e0f3(0x216)]=_0x1c16c4,this[_0x54e0f3(0x225)]=_0x12d05e;},'start':function(){const _0x2434e9=_0x424c98;this._super.apply(this,arguments)[_0x2434e9(0x22e)](()=>{const _0x485927=_0x2434e9;this[_0x485927(0x1ee)](),_0x4b05e1['bus']['on']('mana_dashboard.do_query',this,this[_0x485927(0x1f1)]);});},'updateState':function(_0x3d9bf6){const _0x5714b5=_0x424c98;this[_0x5714b5(0x216)]=_0x3d9bf6,this[_0x5714b5(0x20c)]&&(_0x4b05e1[_0x5714b5(0x218)]['trigger']('DOM_updated'),this[_0x5714b5(0x20c)]=![]);},'get_data':function(_0x54a6d1){const _0x5e3bb7=_0x424c98;let _0x13fe29=this[_0x5e3bb7(0x216)][_0x5e3bb7(0x206)][_0x5e3bb7(0x228)];switch(_0x13fe29){case'sql':return this[_0x5e3bb7(0x214)]();case'model':return this['get_data_from_model']();case'method':return this[_0x5e3bb7(0x21b)]();case'json':return this[_0x5e3bb7(0x22a)]();case'code':return this[_0x5e3bb7(0x211)]();default:return Promise[_0x5e3bb7(0x204)]([]);}},'get_data_model':function(){const _0x113e1f=_0x424c98;let _0x3e874a=this[_0x113e1f(0x203)](),_0x36248e=_0x3e874a['getParent'](),_0x5a59ac=_0x36248e[_0x113e1f(0x20a)];return _0x5a59ac;},'get_controller':function(){const _0x39ece4=_0x424c98;let _0x1229a2=this[_0x39ece4(0x203)](),_0x3a25c7=_0x1229a2[_0x39ece4(0x203)]();return _0x3a25c7;},'do_query':function(){const _0xaef4db=_0x424c98;let _0xe6f8f1=this['record'][_0xaef4db(0x223)];this[_0xaef4db(0x213)]({'fetch_data':!![],'fetch_sql_data':!![],'fetch_model_data':!![],'fetch_model_method_data':!![],'fetch_json_data':!![],'fetch_code_data':!![]})[_0xaef4db(0x22e)](_0x1bb1ab=>{const _0x17c042=_0xaef4db;let _0x52c76f=_0x1bb1ab[_0x17c042(0x221)];return this[_0x17c042(0x215)][_0x17c042(0x202)](_0x52c76f),_0x1bb1ab[_0x17c042(0x20e)];})[_0xaef4db(0x22e)](_0x5d68bf=>{const _0x16ddfd=_0xaef4db;return this[_0x16ddfd(0x210)]({'model':this[_0x16ddfd(0x216)][_0x16ddfd(0x20a)],'method':'combine_raw_fields','args':[_0xe6f8f1,_0x5d68bf]});})['then'](_0xd9cd9e=>{const _0x1a4d79=_0xaef4db;this['table'][_0x1a4d79(0x22b)](_0xd9cd9e);let _0x2be5c8=this[_0x1a4d79(0x203)](),_0x5442f=_0x2be5c8['allFieldWidgets'];for(let _0x160f9c in _0x5442f){let _0x3bd2eb=_0x5442f[_0x160f9c];for(let _0xcd82c0=0x0;_0xcd82c0<_0x3bd2eb[_0x1a4d79(0x20f)];_0xcd82c0++){let _0x14f5f2=_0x3bd2eb[_0xcd82c0];if(_0x14f5f2[_0x1a4d79(0x1ed)]=='fake_field'){_0x14f5f2[_0x1a4d79(0x1fd)](JSON[_0x1a4d79(0x217)](_0xd9cd9e)),this[_0x1a4d79(0x20c)]=!![];break;}}}});},'get_model_fields':function(){const _0x5e12cd=_0x424c98;let _0x5a0ab4=this[_0x5e12cd(0x21c)](),_0x2568cf=_0x5a0ab4[_0x5e12cd(0x226)](this[_0x5e12cd(0x216)]['data'][_0x5e12cd(0x1f4)]['id'],{'raw':!![]}),_0x22e7ac=_0x2568cf[_0x5e12cd(0x206)],_0x3d63aa=[];for(let _0x5bb2ec=0x0;_0x5bb2ec<_0x22e7ac['length'];_0x5bb2ec++){let _0x15fb80=_0x22e7ac[_0x5bb2ec],_0x46f339=_0x15fb80['data'];_0x3d63aa['push'](_0x46f339);}return _0x3d63aa;},'get_order_by_infos':function(){const _0x2786c9=_0x424c98;let _0x171883=this[_0x2786c9(0x21c)](),_0xbb06c=_0x171883[_0x2786c9(0x226)](this['record'][_0x2786c9(0x206)][_0x2786c9(0x1f3)]['id'],{'raw':!![]}),_0x309b44=_0xbb06c[_0x2786c9(0x206)],_0x2b4993=[];for(let _0x1d3b02=0x0;_0x1d3b02<_0x309b44[_0x2786c9(0x20f)];_0x1d3b02++){let _0x6e5297=_0x309b44[_0x1d3b02],_0x577250=_0x6e5297['data'];_0x2b4993[_0x2786c9(0x1fc)](_0x577250);}return _0x2b4993;},'get_group_by_infos':function(){const _0x5edc08=_0x424c98;let _0x4404=this[_0x5edc08(0x21c)](),_0x261a30=_0x4404[_0x5edc08(0x226)](this['record'][_0x5edc08(0x206)][_0x5edc08(0x222)]['id'],{'raw':!![]}),_0x1790ae=_0x261a30[_0x5edc08(0x206)],_0x33a4fc=[];for(let _0x1fa696=0x0;_0x1fa696<_0x1790ae[_0x5edc08(0x20f)];_0x1fa696++){let _0x358669=_0x1790ae[_0x1fa696],_0x2c85bb=_0x358669['data'];_0x33a4fc[_0x5edc08(0x1fc)](_0x2c85bb);}return _0x33a4fc;},'get_parameter_infos':function(){const _0x3f7cfb=_0x424c98;let _0x42eba6=this[_0x3f7cfb(0x21c)](),_0x286e80=_0x42eba6[_0x3f7cfb(0x226)](this[_0x3f7cfb(0x216)][_0x3f7cfb(0x206)]['parameter_ids']['id'],{'raw':!![]}),_0x2317d0=_0x286e80['data'],_0x32a8f0={};for(let _0x2785aa=0x0;_0x2785aa<_0x2317d0[_0x3f7cfb(0x20f)];_0x2785aa++){let _0xe5b01f=_0x2317d0[_0x2785aa],_0x3cada4=_0xe5b01f[_0x3f7cfb(0x206)],_0x5bd313=_0x3cada4['type'],_0x4f081d=undefined;if(_0x5bd313=='int')_0x4f081d=parseInt(_0x3cada4[_0x3f7cfb(0x1f8)]);else{if(_0x5bd313=='float')_0x4f081d=parseFloat(_0x3cada4['default_value']);else{if(_0x5bd313=='bool')_0x4f081d=_0x3cada4[_0x3f7cfb(0x1f8)]=='True'?!![]:![];else{if(_0x5bd313=='date')_0x4f081d=moment(_0x3cada4[_0x3f7cfb(0x1f8)])['format']('YYYY-MM-DD');else _0x5bd313=='datetime'?_0x4f081d=moment(_0x3cada4['default_value'])['format']('YYYY-MM-DD HH:mm:ss'):_0x4f081d=_0x3cada4[_0x3f7cfb(0x1f8)];}}}_0x32a8f0[_0x3cada4[_0x3f7cfb(0x1ed)]]=_0x4f081d;}return _0x32a8f0;},'get_order_by_infos':function(){const _0x382bd8=_0x424c98;let _0xd925c6=this[_0x382bd8(0x21c)](),_0x5ded70=_0xd925c6[_0x382bd8(0x226)](this[_0x382bd8(0x216)][_0x382bd8(0x206)][_0x382bd8(0x1f3)]['id'],{'raw':!![]}),_0x359bf8=_0x5ded70['data'],_0xf9028e=[];for(let _0x237b9f=0x0;_0x237b9f<_0x359bf8[_0x382bd8(0x20f)];_0x237b9f++){let _0x3e521e=_0x359bf8[_0x237b9f],_0x3ab791=_0x3e521e['data'];_0xf9028e[_0x382bd8(0x1fc)](_0x3ab791);}return _0xf9028e;},'get_data_from_model':function(){const _0x2f9e42=_0x424c98;let _0x102446=this[_0x2f9e42(0x21c)](),_0x4b333f=this[_0x2f9e42(0x1f9)](),_0x44d601=_0x102446[_0x2f9e42(0x226)](_0x4b333f[_0x2f9e42(0x1f6)],{'raw':!![]}),_0x2070ae=_0x44d601['data'][_0x2f9e42(0x20a)],_0x91b08c=_0x44d601['data'][_0x2f9e42(0x20b)]||[],_0xdd5d03=_0x44d601[_0x2f9e42(0x206)]['context']||{},_0x1822d5=_0x44d601[_0x2f9e42(0x206)][_0x2f9e42(0x1ef)]||0x0,_0x196594=this['get_order_by_infos'](),_0x3985a5=this['get_group_by_infos'](),_0x49c2fb=this[_0x2f9e42(0x1f5)]();if(!_0x2070ae)return Promise[_0x2f9e42(0x204)]([]);return this[_0x2f9e42(0x210)]({'model':'mana_dashboard.data_source_base','method':'get_data_from_model','args':[{'model_id':_0x2070ae,'domain':_0x91b08c,'context':_0xdd5d03,'model_fields':_0x49c2fb,'limit':_0x1822d5,'group_by_infos':_0x3985a5,'order_by_infos':_0x196594}]});},'get_data_from_sql':function(){const _0x88208e=_0x424c98;let _0x1c0927=this[_0x88208e(0x216)][_0x88208e(0x206)][_0x88208e(0x229)];if(!_0x1c0927)return Promise[_0x88208e(0x204)]([]);return this[_0x88208e(0x210)]({'model':'mana_dashboard.data_source_base','method':'get_data_from_sql','args':[_0x1c0927,{'preview':!![],'params':this[_0x88208e(0x224)](),'result_type':this[_0x88208e(0x216)][_0x88208e(0x206)][_0x88208e(0x22c)][0x1]}]});},'get_data_from_method':function(){const _0x596630=_0x424c98;let _0xf019a4=this[_0x596630(0x216)][_0x596630(0x206)]['model']&&this[_0x596630(0x216)][_0x596630(0x206)][_0x596630(0x20a)]['data']['id'],_0x274b49=this['record'][_0x596630(0x206)][_0x596630(0x1fb)];_0x274b49=_0x274b49&&_[_0x596630(0x219)][_0x596630(0x21f)](_0x274b49);if(!_0xf019a4||!_0x274b49||_0x274b49=='')return Promise[_0x596630(0x204)]([]);return this['_rpc']({'model':'mana_dashboard.data_source_base','method':'get_data_from_model_method','args':[_0xf019a4,_0x274b49,{'preview':!![],'params':this['get_parameter_infos'](),'result_type':this[_0x596630(0x216)][_0x596630(0x206)]['result_type'][0x1]}],'kwargs':{}});},'get_data_from_json':function(){const _0x421455=_0x424c98;let _0x32e3fe=this[_0x421455(0x216)][_0x421455(0x206)][_0x421455(0x227)],_0x3dd8ec=this[_0x421455(0x216)][_0x421455(0x206)][_0x421455(0x1f2)];return this[_0x421455(0x210)]({'model':'mana_dashboard.data_source_base','method':'get_data_from_json','args':[_0x32e3fe,{'json_data_format':_0x3dd8ec,'params':this[_0x421455(0x224)](),'result_type':this[_0x421455(0x216)][_0x421455(0x206)][_0x421455(0x22c)][0x1]}]});},'get_data_from_code':function(){const _0x24170f=_0x424c98;let _0x3a8982=this[_0x24170f(0x216)][_0x24170f(0x206)][_0x24170f(0x207)];if(!_0x3a8982)return Promise[_0x24170f(0x204)]([]);return this[_0x24170f(0x210)]({'model':'mana_dashboard.data_source_base','method':'get_data_from_code','args':[_0x3a8982,{'preview':!![],'params':this[_0x24170f(0x224)]()}]});},'render':function(){const _0x9ebd6e=_0x424c98;if(!this['record'])return;!this['table']&&(this['table']=new Tabulator(this[_0x9ebd6e(0x208)]['get'](0x0),{'pagination':!![],'layout':'fitDataStretch','tooltipsHeader':![],'paginationSize':0xa,'paginationSizeSelector':[0xa,0x19,0x32,0x64],'autoColumns':!![],'layout':'fitColumns','dataSourceCallback':()=>{const _0x297e09=_0x9ebd6e;if(this[_0x297e09(0x216)][_0x297e09(0x206)]['fake_field']){let _0x42b073=JSON[_0x297e09(0x22d)](this['record'][_0x297e09(0x206)]['fake_field'][_0x297e09(0x206)]);return Promise[_0x297e09(0x204)](_0x42b073);}else return Promise[_0x297e09(0x204)]([]);}}));}});return _0x446ac0[_0x424c98(0x20d)]('grid_widget',_0x318703),_0x318703;}));