const a0_0x5751f3=a0_0x31b6;function a0_0x31b6(_0xcbc7cf,_0x4437d7){const _0x3b71e3=a0_0x3b71();return a0_0x31b6=function(_0x31b6fe,_0x3fd8b0){_0x31b6fe=_0x31b6fe-0x1b0;let _0x1004aa=_0x3b71e3[_0x31b6fe];return _0x1004aa;},a0_0x31b6(_0xcbc7cf,_0x4437d7);}(function(_0x9c6b98,_0x42171d){const _0x1af415=a0_0x31b6,_0x4eab5a=_0x9c6b98();while(!![]){try{const _0x2ce2ce=parseInt(_0x1af415(0x1b9))/0x1+parseInt(_0x1af415(0x1ce))/0x2+parseInt(_0x1af415(0x1cb))/0x3+parseInt(_0x1af415(0x1f8))/0x4*(-parseInt(_0x1af415(0x1da))/0x5)+-parseInt(_0x1af415(0x203))/0x6+-parseInt(_0x1af415(0x1ff))/0x7+parseInt(_0x1af415(0x1c6))/0x8;if(_0x2ce2ce===_0x42171d)break;else _0x4eab5a['push'](_0x4eab5a['shift']());}catch(_0xb9ac71){_0x4eab5a['push'](_0x4eab5a['shift']());}}}(a0_0x3b71,0x4aa14),odoo[a0_0x5751f3(0x1bc)]('mana_dashboard.dashboard',function(require){'use strict';const _0x24e856=a0_0x5751f3;const _0x10a478=require('web.AbstractAction'),_0x5426e1=require('web.core'),_0x1acab2=require('mana_dashboard.block_registry'),_0x37ff95=require('mana_dashboard.content_block'),_0x5980e8=require('mana_dashboard.form_trait'),_0x505271=require('web.py_utils'),_0x4b9d8e=require('web.session'),_0x11dca4=require('mana_dashboard.editor_preset'),_0x574e8b=require('mana_dashboard.icons'),_0x17040f=require('web.ajax'),_0x47b4a1=require('mana_dashboard.theme_builder_widget'),_0x2331d2=_0x5426e1['_t'],_0x3afac4=_0x24e856(0x1e2);var _0x53b306=_0x10a478[_0x24e856(0x208)]({'jsLibs':['/web/static/lib/daterangepicker/daterangepicker.js','/mana_dashboard/static/libs/apexcharts/apexcharts.min.js'],'events':_[_0x24e856(0x208)]({},_0x10a478['prototype']['events'],{'click .btn':'_onButtonClick'}),'custom_events':_[_0x24e856(0x208)]({},_0x10a478[_0x24e856(0x1df)]['custom_events'],{'mana_dashboard.drill_down':'_on_drill_down','mana_dashboard.drill_up':'_on_drill_up','mana_dashboard.view_chart_data':'_on_view_chart_data','mana_dashboard.linked_actions':'_on_linked_actions','mana_dashboard.change_default_template':'_on_change_default_template','mana_dashboard.do_search':'_do_search'}),'init':function(_0x4af057,_0x5080bd){const _0x2156a8=_0x24e856;return this['dashboard_id']=_0x5080bd[_0x2156a8(0x224)]&&_0x5080bd[_0x2156a8(0x224)][_0x2156a8(0x1e7)],this[_0x2156a8(0x1e3)]=_0x5080bd[_0x2156a8(0x224)]&&_0x5080bd[_0x2156a8(0x224)][_0x2156a8(0x1e3)],this[_0x2156a8(0x224)]=_0x5080bd[_0x2156a8(0x224)],this[_0x2156a8(0x1ba)]=[],this['default_template_cache']={},this._super.apply(this,arguments);},'start':function(){const _0x3e612d=_0x24e856;this._super.apply(this,arguments)[_0x3e612d(0x1ed)](()=>{const _0x356b2e=_0x3e612d;this[_0x356b2e(0x1e3)]=='view'&&this[_0x356b2e(0x22d)]['addClass']('o_mana_view_mode');this[_0x356b2e(0x1b6)]();var _0x299283=['blocks-bootstrap4',_0x37ff95];this[_0x356b2e(0x1e3)]!='view'&&_0x299283[_0x356b2e(0x228)](_0x11dca4);var _0x1e5f44=_0x1acab2[_0x356b2e(0x1b3)]();for(var _0x1d99ff=0x0;_0x1d99ff<_0x1e5f44[_0x356b2e(0x21a)];_0x1d99ff++){_0x299283[_0x356b2e(0x228)](_0x1e5f44[_0x1d99ff]);}let _0x2abd70=_0x4b9d8e[_0x356b2e(0x1eb)][_0x356b2e(0x23d)],_0x47a505=grapesjs[_0x356b2e(0x1d8)];if(_0x2abd70=='zh_CN')_0x2abd70='zh';else _0x2abd70=='zh_TW'?_0x2abd70='zh-tw':_0x2abd70=_0x2abd70[_0x356b2e(0x239)]('_')[0x0];let _0xfbfa3c={'showOffsets':0x1,'noticeOnUnload':0x0,'container':this[_0x356b2e(0x22d)][_0x356b2e(0x1e5)](0x0),'height':'100%','fromElement':![],'jsInHtml':![],'cssInHtml':![],'editor_mode':this[_0x356b2e(0x1e3)],'storageManager':{'autoload':0x0,'autosave':0x0},'plugins':_0x299283,'allowScripts':0x0,'storageManager':![],'widget':this,'i18n':{'locale':_0x2abd70,'localeFallback':'en','messages':{'zh':_['extend'](grapesjs['zh'],{}),'en':_[_0x356b2e(0x208)](grapesjs['en'],{})}}};this[_0x356b2e(0x1e3)]=='view'&&(_0xfbfa3c['panels']={'defaults':[]});if(this[_0x356b2e(0x1d2)][_0x356b2e(0x1b5)]){_0xfbfa3c[_0x356b2e(0x20b)]=this['dashboard_data']['dashboard_html'];let _0x4ae83a=this['dashboard_data']['dashboard_css'];_0x4ae83a&&(_0x4ae83a=_0x4ae83a[_0x356b2e(0x1c1)](/body\s*\{/g,'[data-gjs-type="wrapper"]{'));_0xfbfa3c[_0x356b2e(0x1b4)]=_0x4ae83a,_0xfbfa3c[_0x356b2e(0x232)]=this[_0x356b2e(0x1d2)]['dashboard_js'];let _0x4c9723={};this[_0x356b2e(0x1d2)][_0x356b2e(0x215)]&&(_0x4c9723['styles']=this[_0x356b2e(0x1d2)][_0x356b2e(0x215)]),this[_0x356b2e(0x1d2)][_0x356b2e(0x222)]&&(_0x4c9723['scripts']=this[_0x356b2e(0x1d2)][_0x356b2e(0x222)]),Object[_0x356b2e(0x211)](_0x4c9723)[_0x356b2e(0x21a)]>0x0&&(_0xfbfa3c['canvas']=_0x4c9723);}else _0xfbfa3c[_0x356b2e(0x20b)]=_0x3afac4;this[_0x356b2e(0x201)]=grapesjs['init'](_0xfbfa3c),this['editor'][_0x356b2e(0x1ee)][_0x356b2e(0x20a)]('views',{'id':'theme-builder','className':'fa fa-adjust','command':'open-theme-builder','attributes':{'title':'Theme'}}),this['mode']=='view'?this[_0x356b2e(0x23e)]():(_0x5980e8(this[_0x356b2e(0x201)],{'widget':this}),this[_0x356b2e(0x1de)](),this[_0x356b2e(0x1e4)](),this[_0x356b2e(0x1c3)]()),this['editor'][_0x356b2e(0x1ca)](()=>{const _0xcea46=_0x356b2e;this[_0xcea46(0x1e3)]=='view'&&setTimeout(()=>{const _0x56d6c2=_0xcea46;this[_0x56d6c2(0x201)][_0x56d6c2(0x1c2)]('preview');},0x0),this[_0xcea46(0x218)]();});});},'set_cavas_preview':function(){const _0x25d922=_0x24e856,_0x57a2a8=editor[_0x25d922(0x225)][_0x25d922(0x1cc)](),_0x18aca5=_0x57a2a8[_0x25d922(0x1b4)];_0x18aca5[_0x25d922(0x223)]='100%',_0x18aca5[_0x25d922(0x216)]='100%',_0x18aca5[_0x25d922(0x229)]='0',_0x18aca5['left']='0',_0x18aca5[_0x25d922(0x1f5)]='0',_0x18aca5[_0x25d922(0x1be)]='0';},'get_dashboard_id':function(){const _0x312a15=_0x24e856;return this[_0x312a15(0x1e7)];},'_on_editor_ready':function(){const _0x33bf0d=_0x24e856;this[_0x33bf0d(0x1d2)][_0x33bf0d(0x220)]&&!this[_0x33bf0d(0x1d2)][_0x33bf0d(0x209)]&&_0x5426e1[_0x33bf0d(0x1c8)][_0x33bf0d(0x22c)]('mana_dashboard.init_config',this[_0x33bf0d(0x1e7)]);},'_on_change_default_template':function(_0x4f288d){const _0xd7846f=_0x24e856;let _0x1edb10=_0x4f288d[_0xd7846f(0x1f1)];this[_0xd7846f(0x1fd)][_0x1edb10[_0xd7846f(0x1c4)]]=_0x1edb10[_0xd7846f(0x20e)];},'_bind_editor_events':function(){const _0x455bb4=_0x24e856;this['editor']['on']('canvas:drop',this['_on_component_drop']['bind'](this),this),this[_0x455bb4(0x201)]['on']('component:remove:before',this[_0x455bb4(0x1dc)],this);},'on_component_remove':function(_0x38e084){const _0x3d08e1=_0x24e856;if(this[_0x3d08e1(0x205)])return;let _0x470232=_0x38e084[_0x3d08e1(0x1e5)]('attributes');if(!_0x470232)return;let _0x282e8=parseInt(_0x470232['config_id']),_0x292b43=_0x38e084[_0x3d08e1(0x1e5)]('config_model'),_0x328203=[_0x282e8],_0x86258b=_0x38e084[_0x3d08e1(0x1e5)]('components')||[],_0x3cf93a=function(_0x40e737){const _0x317401=_0x3d08e1;_0x40e737[_0x317401(0x1fe)](function(_0x13e000){const _0x50f987=_0x317401;let _0xa91e9b=_0x13e000[_0x50f987(0x1e5)]('attributes');if(_0xa91e9b){let _0x474953=_0xa91e9b['config_id'];_0x474953&&(_0x474953=parseInt(_0x474953),_0x328203[_0x50f987(0x228)](_0x474953));}let _0x3b83f1=_0x13e000[_0x50f987(0x1e5)]('components');_0x3b83f1&&_0x3cf93a(_0x3b83f1);});};_0x3cf93a(_0x86258b),_0x282e8&&this[_0x3d08e1(0x1d7)]({'model':'mana_dashboard.any_config','method':'unlink','args':[_0x328203]},{'shadow':!![]});},'get_default_template':function(_0x4fccea){const _0x3d8b4a=_0x24e856;return this[_0x3d8b4a(0x1fd)][_0x4fccea];},'_on_component_drop':function(_0x978b3,_0x11076e){const _0x47b052=_0x24e856;let _0x2e6eb6=_0x11076e[_0x47b052(0x1e5)]('config_model');if(_0x11076e[_0x47b052(0x1e5)]('has_config')){let _0x2fb2b6=_0x11076e[_0x47b052(0x1e5)]('type'),_0x3f24da=_0x11076e[_0x47b052(0x1e5)]('attributes')[_0x47b052(0x219)];!_0x3f24da&&(_0x3f24da=this[_0x47b052(0x1fd)][_0x2fb2b6]||_0x11076e[_0x47b052(0x1e5)]('default_template')),this[_0x47b052(0x1d7)]({'model':'mana_dashboard.any_config','method':'create_config','args':[this[_0x47b052(0x1e7)],_0x2e6eb6,{'default_template':_0x3f24da,'template_category':_0x11076e[_0x47b052(0x1e5)]('template_category'),'template_type':_0x11076e[_0x47b052(0x1e5)]('template_type')}]})[_0x47b052(0x1ed)](_0x22db8d=>{const _0x55f2b2=_0x47b052;_0x11076e[_0x55f2b2(0x1fc)]({'config_id':_0x22db8d[_0x55f2b2(0x202)]});})[_0x47b052(0x1ed)](()=>{this['save_dashboard'](this['editor'],![]);});}},'get_theme_info':function(){const _0x3e0b44=_0x24e856;return this[_0x3e0b44(0x1f7)];},'get_theme_data':function(){const _0x354cb0=_0x24e856;return this[_0x354cb0(0x233)];},'set_theme':function(_0x5005f6,_0x4b10c2=![]){const _0x5e9753=_0x24e856;this[_0x5e9753(0x233)]=_0x5005f6['themeData'],this[_0x5e9753(0x238)]=_0x5005f6[_0x5e9753(0x238)],this['theme_info']=_0x5005f6,echarts[_0x5e9753(0x1f9)](this[_0x5e9753(0x230)](),this[_0x5e9753(0x238)]),!_0x4b10c2&&_0x5426e1[_0x5e9753(0x1c8)]['trigger']('mana_dashboard.theme_changed',this[_0x5e9753(0x238)]);},'get_theme_name':function(){return'mana_dashboard.theme_'+this['dashboard_id'];},'save_dashboard':function(_0x33c1a8,_0x1cc43c=!![]){const _0x1a0ddb=_0x24e856;var _0x52b3b1=_0x33c1a8['getHtml'](),_0x8999b0=_0x33c1a8[_0x1a0ddb(0x1d6)]();return this[_0x1a0ddb(0x1d7)]({'model':'mana_dashboard.dashboard','method':'write','args':[this['dashboard_id'],{'dashboard_html':_0x52b3b1,'dashboard_css':_0x8999b0,'default_template_info':JSON['stringify'](this['default_template_cache']||{})}]},{'shadow':!![]})[_0x1a0ddb(0x1ed)](()=>{const _0x542835=_0x1a0ddb;_0x1cc43c&&this[_0x542835(0x1c5)]({'title':_0x2331d2('Success'),'message':_0x2331d2('Save Success'),'type':'success','sticky':![]});});},'registCommonds':function(){const _0x43ba6d=_0x24e856;let self=this;const _0x3df33d=this[_0x43ba6d(0x201)]['Commands'];_0x3df33d[_0x43ba6d(0x234)]('save-html',_0xb69c7b=>{const _0x3fed55=_0x43ba6d;this[_0x3fed55(0x226)](_0xb69c7b,!![]);}),_0x3df33d['add']('open-theme-builder',{'run'(_0x293518){const _0x867d6e=_0x43ba6d,_0x55e4bb=_0x293518['Panels'];if(!this[_0x867d6e(0x1c9)]){const _0x6ca36a='views-container',_0x39e0f2=document['createElement']('div'),_0x33e9ac=_0x55e4bb['getPanel'](_0x6ca36a)||_0x55e4bb[_0x867d6e(0x1b7)]({'id':_0x6ca36a});let _0x12e61f=new _0x47b4a1(self),_0xafc6d6=$('<div style="wdith:100%; height:100%"/>');_0x39e0f2[_0x867d6e(0x1d5)](_0xafc6d6[0x0]),_0x33e9ac[_0x867d6e(0x1db)]('appendContent',_0x39e0f2)['trigger']('change:appendContent'),_0x12e61f['appendTo'](_0xafc6d6),this['theme_builder']=_0x39e0f2;}this[_0x867d6e(0x1c9)]['style']['display']='block';},'stop'(){const _0x5da410=_0x43ba6d,{theme_builder:_0x2752e5}=this;_0x2752e5&&(_0x2752e5[_0x5da410(0x1b4)]['display']='none');}}),_0x3df33d[_0x43ba6d(0x234)]('history-back',_0x1a1b18=>{const _0xb30eba=_0x43ba6d;this[_0xb30eba(0x1f3)]({'type':'ir.actions.act_window','name':_0x2331d2('Dashboard'),'res_model':'mana_dashboard.dashboard','views':[[![],'list'],[![],'form']],'target':'current'},{'clear_breadcrumbs':!![]});}),_0x3df33d['add']('view-code',_0xc1a980=>{}),_0x3df33d['add']('edit_config',(_0xaa81f,_0xec956e,_0x5854a7)=>{const _0x4ec9ac=_0x43ba6d;let _0xde4c78=_0xaa81f['getSelected'](),_0x3cefe9=_0xde4c78[_0x4ec9ac(0x1e5)]('attributes')['config_id'];_0x3cefe9=parseInt(_0x3cefe9);let _0x1b1abc=_0xde4c78[_0x4ec9ac(0x1e5)]('config_model'),_0x51f47=_0xde4c78['get']('config_form_res_id'),_0x36eae5=null;if(!_0x3cefe9)_0x36eae5=this[_0x4ec9ac(0x1d7)]({'model':'mana_dashboard.any_config','method':'create_config','args':[this[_0x4ec9ac(0x1e7)],_0x1b1abc,{'default_template':_0xde4c78[_0x4ec9ac(0x1e5)]('default_template'),'template_category':_0xde4c78['get']('template_category'),'template_type':_0xde4c78['get']('template_type')}]})[_0x4ec9ac(0x1ed)](_0x1becec=>{const _0x184108=_0x4ec9ac;return _0xde4c78[_0x184108(0x1fc)]({'config_id':_0x1becec[_0x184108(0x202)]}),_0x1becec[_0x184108(0x1bf)];});else{let _0x4b26d5=_0xde4c78[_0x4ec9ac(0x1e5)]('config'),_0x907a7e=_0x4b26d5[_0x4ec9ac(0x1c7)]();_0x36eae5=Promise[_0x4ec9ac(0x22b)](_0x907a7e);}_0x36eae5[_0x4ec9ac(0x1ed)](_0x245c5e=>{const _0x52c518=_0x4ec9ac;let _0x20bbf9=_0xde4c78[_0x52c518(0x231)]();_0x20bbf9=_0x20bbf9[_0x52c518(0x1c1)](/\s+id="[^"]*"/g,''),this[_0x52c518(0x1f3)]({'type':'ir.actions.act_window','res_model':_0x1b1abc,'res_id':_0x245c5e,'views':[[![],'form']],'context':{'dialog_size':'max-width-90','form_view_ref':_0x51f47,'content':_0x20bbf9,'theme_name':this[_0x52c518(0x230)](),'fullscreen':!![]},'target':'new'},{'on_close':_0x21c34c=>{const _0x485cf9=_0x52c518;if(!_0x21c34c||_0x21c34c['special']==!![])return;let _0x3eef86=_0xde4c78[_0x485cf9(0x22f)];_0x3eef86&&_0xde4c78[_0x485cf9(0x22e)]();let _0x10853d=_0x21c34c['data']['link_to_config'];if(_0x10853d){let _0xacaca5=_0x10853d['data']['id'];_0x5426e1['bus'][_0x485cf9(0x22c)]('mana_dashboard.reload_config',_0xacaca5);}}});});}),_0x3df33d[_0x43ba6d(0x234)]('edit_svg',(_0x475a86,_0x116484,_0x27ebde)=>{const _0x23d212=_0x43ba6d;let _0xdc27ac=_0x475a86[_0x23d212(0x1e0)](),_0xd80e31=_0xdc27ac['toHTML']();this[_0x23d212(0x1f3)]({'type':'ir.actions.act_window','res_model':'mana_dashboard.content_editor','target':'new','context':{'default_content':_0xd80e31,'form_view_ref':'mana_dashboard.content_editor_form'},'views':[[![],'form']]},{'on_close':_0x1094cb=>{const _0x504bd1=_0x23d212;if(!_0x1094cb||_0x1094cb['special'])return;let _0x3b101f=_0x1094cb[_0x504bd1(0x1f1)][_0x504bd1(0x1ec)],_0x10d504=_0xdc27ac[_0x504bd1(0x1d1)](),_0x4fbf18=_0xdc27ac[_0x504bd1(0x1d9)]();_0xdc27ac[_0x504bd1(0x20d)](),_0x10d504['append'](_0x3b101f,{'at':_0x4fbf18});}});}),_0x3df33d[_0x43ba6d(0x234)]('drill_down',(_0x576ae1,_0x547432,_0x5684a6)=>{const _0x80f59d=_0x43ba6d;let _0x421ea5=_0x576ae1[_0x80f59d(0x1e0)](),_0x5564f3=_0x421ea5['get']('attributes')['config_id'];_0x5564f3=parseInt(_0x5564f3);let _0x3b1fab=_0x421ea5['get']('config_model'),_0x1cbfa3=_0x421ea5[_0x80f59d(0x1e5)]('config_form_res_id'),_0x4b8bcd=_0x421ea5[_0x80f59d(0x1e5)]('config');if(!_0x4b8bcd){this[_0x80f59d(0x1c5)]({'title':_0x2331d2('Error'),'message':_0x2331d2('No config found'),'type':'danger','sticky':![]});return;}let _0x4e9ca9=_0x4b8bcd[_0x80f59d(0x236)]();if(!_0x4e9ca9){this[_0x80f59d(0x1c5)]({'title':_0x2331d2('Error'),'message':_0x2331d2('No data source found'),'type':'danger','sticky':![]});return;}let _0x2bacbd=_0x4e9ca9[_0x80f59d(0x227)]();if(!_0x2bacbd||_0x2bacbd['length']==0x0){this['displayNotification']({'title':_0x2331d2('Error'),'message':_0x2331d2('No category found'),'type':'danger','sticky':![]});return;}let _0x56511f=_0x2bacbd[0x0]['name'];this[_0x80f59d(0x1d7)]({'model':'mana_dashboard.any_config','method':'get_drill_down_config','args':[_0x5564f3,{'config_form_res_id':_0x1cbfa3,'config_model':_0x3b1fab,'config_id':_0x5564f3,'dialog_size':'max-width-90','category_names':_0x56511f}]})[_0x80f59d(0x1ed)](_0x2dfebb=>{const _0x53e112=_0x80f59d;if(!_0x2dfebb){this[_0x53e112(0x1c5)]({'title':_0x2331d2('Error'),'message':_0x2331d2('No drill down config'),'type':'danger','sticky':![]});return;}let _0x4e6e40=_0x421ea5[_0x53e112(0x231)]();_0x4e6e40=_0x4e6e40['replace'](/\s+id="[^"]*"/g,''),_0x2dfebb[_0x53e112(0x1c0)]=_['extend'](_0x2dfebb[_0x53e112(0x1c0)]||{},{'content':_0x4e6e40}),this['do_action'](_0x2dfebb,{'on_close':_0x562128=>{const _0x512af4=_0x53e112;if(!_0x562128||_0x562128[_0x512af4(0x23f)])return;_0x421ea5[_0x512af4(0x1fc)]({'drill_down_config_id':_0x562128['id']});}});});});},'get_custom_css_id':function(){const _0x2b2523=_0x24e856;return'mana_dashboard_custom_css_'+this[_0x2b2523(0x1e7)];},'load_custom_css':function(){const _0x1ef9b0=_0x24e856;let _0x5a7172=this[_0x1ef9b0(0x1b2)](),_0x25eee=document['getElementById'](_0x5a7172);_0x25eee&&_0x25eee[_0x1ef9b0(0x20d)]();let _0x12adfe=this[_0x1ef9b0(0x1d2)][_0x1ef9b0(0x1d0)];if(_0x12adfe){let _0x3c3e2e=document['createElement']('style');_0x3c3e2e[_0x1ef9b0(0x217)]='text/css',_0x3c3e2e[_0x1ef9b0(0x1f0)]=_0x12adfe,_0x3c3e2e['id']=_0x5a7172,document[_0x1ef9b0(0x1dd)]('head')[0x0][_0x1ef9b0(0x1d5)](_0x3c3e2e);}},'willStart':function(){return this._super.apply(this,arguments)['then'](()=>{const _0x152e01=a0_0x31b6;return this[_0x152e01(0x1d3)]();});},'_loaDashboard':function(){const _0x14942e=_0x24e856;return this['_rpc']({'model':'mana_dashboard.dashboard','method':'load_dashboard','args':[this[_0x14942e(0x1e7)]]})['then'](_0x1eb488=>{const _0x5642fd=_0x14942e;this[_0x5642fd(0x1d2)]=_0x1eb488;let _0x192c48=_0x1eb488[_0x5642fd(0x1f7)];_0x192c48&&(_0x192c48=JSON[_0x5642fd(0x207)](_0x192c48),this[_0x5642fd(0x212)](_0x192c48,!![])),this[_0x5642fd(0x1d2)][_0x5642fd(0x21e)]&&(this[_0x5642fd(0x1fd)]=JSON[_0x5642fd(0x207)](this[_0x5642fd(0x1d2)][_0x5642fd(0x21e)]||'{}'));});},'load_favorite_blocks':function(){const _0x1c5221=_0x24e856;this[_0x1c5221(0x1d7)]({'model':'mana_dashboard.action_blocks','method':'load_action_blocks','args':[]})[_0x1c5221(0x1ed)](_0x5a9d47=>{const _0x3b102a=_0x1c5221;this[_0x3b102a(0x1bd)]=_0x5a9d47||[],this[_0x3b102a(0x20c)]();});},'init_action_blocks':function(){const _0x1d5147=_0x24e856;for(let _0x38760c=0x0;_0x38760c<this[_0x1d5147(0x1bd)][_0x1d5147(0x21a)];_0x38760c++){let _0x1f80d9=this[_0x1d5147(0x1bd)][_0x38760c];this[_0x1d5147(0x1f4)](_0x1f80d9);}},'init_action_block':function(_0x2eeb55){const _0x1ba365=_0x24e856;let _0x34d373=this[_0x1ba365(0x201)],_0x553028=_0x2eeb55[_0x1ba365(0x1f6)];!_0x553028&&(_0x553028=_0x574e8b[_0x1ba365(0x21d)]),_0x34d373[_0x1ba365(0x23b)][_0x1ba365(0x234)](_0x2eeb55[_0x1ba365(0x23a)],{'label':_0x2eeb55['name'],'render':()=>{const _0x40be95=_0x1ba365;return _0x40be95(0x22a)+_0x553028+'</div><div\x20class=\x27anita-block-label\x27>'+_0x2eeb55[_0x40be95(0x23a)]+_0x40be95(0x1cf);},'category':{'label':_0x2eeb55['category'][0x1]},'content':()=>{var _0x169d54={'type':'action_block','props':{'action_info':_0x2eeb55},'attributes':{'block_id':_0x2eeb55['id']}};return _0x169d54;},'select':!![]});},'canBeRemoved':function(){const _0xfc7440=_0x24e856;if(this[_0xfc7440(0x201)])return this[_0xfc7440(0x226)](this['editor'],![]);},'_on_view_chart_data':function(_0x555713){const _0x33a74e=_0x24e856;let _0x1c56a3=_0x555713[_0x33a74e(0x1f1)],_0x5cdbef=_0x1c56a3['model'],_0x1f83ca=_0x1c56a3['category'],_0x3bd600=_0x1c56a3[_0x33a74e(0x1f2)],_0x247118=_0x5cdbef[_0x33a74e(0x1e5)]('config'),_0x3d6a5e=_0x247118['raw_config'];if(_0x3d6a5e[_0x33a74e(0x204)]=='model'){let _0x5402c4=_0x247118[_0x33a74e(0x236)](),_0xa81091=_0x5402c4['get_category_fields']()||[];if(_0xa81091[_0x33a74e(0x21a)]==0x0)return;let _0x1000f0=_0xa81091[0x0],_0x3da294=_0x3d6a5e['context']||{};_0x3da294=_0x505271[_0x33a74e(0x1e6)]('context',_0x3da294,_0x4b9d8e[_0x33a74e(0x1eb)]);let _0xf20fd8=_0x3d6a5e[_0x33a74e(0x23c)]||'[]';_0xf20fd8=_0x505271[_0x33a74e(0x1e6)]('domain',_0xf20fd8,_0x3da294);if(_0x5402c4[_0x33a74e(0x21b)]()){let _0x478c8c=_0x5402c4['get_row_by_value'](_0x1000f0['full_name'],_0x1f83ca),_0x510d6d=_0x478c8c['get_value']('__domain');if(_0x510d6d){let _0x490bdc=_0x505271[_0x33a74e(0x1e6)]('domain',_0x510d6d,_0x3da294);_0xf20fd8=_0xf20fd8['concat'](_0x490bdc);}}else{if(_0x1f83ca&&_0x3bd600){let _0x1519cb=_0x1000f0[_0x33a74e(0x21f)]['split'](':');if(_0x1519cb[_0x33a74e(0x21a)]>0x1){_0x1f83ca=_0x1519cb[0x0];let _0x145a05=_0x1519cb[0x1];if(['year','quarter','month','week','day'][_0x33a74e(0x237)](_0x145a05)){_0x3bd600=moment(_0x3bd600);switch(_0x145a05){case'year':_0xf20fd8[_0x33a74e(0x228)]([_0x1000f0[_0x33a74e(0x1b1)],'>=',_0x3bd600['startOf']('year')[_0x33a74e(0x210)]('YYYY-MM-DD'),(_0x1000f0['field_name'],'<=',_0x3bd600[_0x33a74e(0x1cd)]('year')['format']('YYYY-MM-DD'))]);break;case'quarter':_0xf20fd8[_0x33a74e(0x228)]([_0x1000f0[_0x33a74e(0x1b1)],'>=',_0x3bd600[_0x33a74e(0x1e8)]('quarter')['format']('YYYY-MM-DD'),(_0x1000f0[_0x33a74e(0x1b1)],'<=',_0x3bd600['endOf']('quarter')[_0x33a74e(0x210)]('YYYY-MM-DD'))]);break;case'month':_0xf20fd8['push']([_0x1000f0[_0x33a74e(0x1b1)],'>=',_0x3bd600[_0x33a74e(0x1e8)]('month')[_0x33a74e(0x210)]('YYYY-MM-DD'),(_0x1000f0[_0x33a74e(0x1b1)],'<=',_0x3bd600[_0x33a74e(0x1cd)]('month')[_0x33a74e(0x210)]('YYYY-MM-DD'))]);break;case'week':_0xf20fd8[_0x33a74e(0x228)]([_0x1000f0[_0x33a74e(0x1b1)],'>=',_0x3bd600[_0x33a74e(0x1e8)]('week')['format']('YYYY-MM-DD'),(_0x1000f0[_0x33a74e(0x1b1)],'<=',_0x3bd600[_0x33a74e(0x1cd)]('week')[_0x33a74e(0x210)]('YYYY-MM-DD'))]);break;case'day':_0xf20fd8[_0x33a74e(0x228)]([_0x1000f0[_0x33a74e(0x1b1)],'>=',_0x3bd600[_0x33a74e(0x1e8)]('day')[_0x33a74e(0x210)]('YYYY-MM-DD'),(_0x1000f0[_0x33a74e(0x1b1)],'<=',_0x3bd600['endOf']('day')[_0x33a74e(0x210)]('YYYY-MM-DD'))]);break;}}else _0xf20fd8[_0x33a74e(0x228)]([_0x1000f0[_0x33a74e(0x1b1)],'=',_0x1f83ca]);}else _0xf20fd8[_0x33a74e(0x228)]([_0x1000f0[_0x33a74e(0x1b1)],'=',_0x1f83ca]);}}let _0x50c3f2={'name':_0x3d6a5e[_0x33a74e(0x1b8)]||'Chart Data','type':'ir.actions.act_window','res_model':_0x3d6a5e[_0x33a74e(0x1d4)],'views':[[![],'list'],[![],'form']],'domain':_0xf20fd8,'context':{}};this[_0x33a74e(0x1f3)](_0x50c3f2);}},'_on_drill_up':function(_0x5f16ae){const _0x526fc6=_0x24e856;let _0xd5ca98=_0x5f16ae[_0x526fc6(0x1f1)],_0x474a1c=_0xd5ca98[_0x526fc6(0x202)];this[_0x526fc6(0x1d7)]({'model':'mana_dashboard.any_config','method':'get_config','args':[_0x474a1c,{'fetch_data':![]}]})['then'](_0x4ab38a=>{const _0x39f1df=_0x526fc6;let _0x401b86=_0x4ab38a[_0x39f1df(0x1fa)],_0x153863=_0xd5ca98[_0x39f1df(0x235)],_0x414a39=_0x153863['parent'](),_0x36dab4=_0x153863['index']();this[_0x39f1df(0x205)]=!![],_0x153863[_0x39f1df(0x20d)](),this[_0x39f1df(0x205)]=![],_0x414a39['append']({'type':_0x401b86[_0x39f1df(0x1c4)],'attributes':{'config_id':_0x4ab38a['id']}},{'at':_0x36dab4});});},'_on_drill_down':function(_0x1f7c82){const _0x3c9a4e=_0x24e856;let _0x351a17=_0x1f7c82[_0x3c9a4e(0x1f1)],_0x2e263c=_0x351a17[_0x3c9a4e(0x202)];this[_0x3c9a4e(0x1d7)]({'model':'mana_dashboard.any_config','method':'get_config','args':[_0x2e263c,{'fetch_data':![]}]})[_0x3c9a4e(0x1ed)](_0x430ee5=>{const _0x42af56=_0x3c9a4e;let _0x3725c3=_0x430ee5['ref_config'],_0x38c26c=_0x351a17['model'],_0xb49f39=_0x38c26c[_0x42af56(0x1d1)](),_0x23f4d0=_0x38c26c[_0x42af56(0x1d9)]();this[_0x42af56(0x205)]=!![],_0x38c26c[_0x42af56(0x20d)](),this['drilling']=![],_0xb49f39[_0x42af56(0x1bb)]({'type':_0x3725c3[_0x42af56(0x1c4)],'attributes':{'config_id':_0x430ee5['id']},'drill_down_context':{'$drill_value':_0x351a17[_0x42af56(0x1f2)],'$drill_field':_0x351a17[_0x42af56(0x200)]}},{'at':_0x23f4d0});});},'_on_linked_actions':function(_0x4d69ad){const _0x3d482c=_0x24e856;let _0x53ddf3=_0x4d69ad[_0x3d482c(0x1f1)];_0x5426e1['bus'][_0x3d482c(0x22c)]('mana_dashboard.linked_block_changed',_0x53ddf3);},'load_css':function(_0x322861){const _0x453969=_0x24e856;return _0x17040f[_0x453969(0x1e1)](_0x322861);},'load_js':function(_0x55557c){const _0x6d525d=_0x24e856;return _0x17040f[_0x6d525d(0x1ea)](_0x55557c);},'getSession':function(){return _0x4b9d8e;},'_onButtonClick':function(_0x14e2fa){const _0x5ecad1=_0x24e856;let _0x1eeede=$(_0x14e2fa[_0x5ecad1(0x1b0)]),_0x634c75=_0x1eeede[_0x5ecad1(0x221)]('type'),_0x5c395f=_0x1eeede[_0x5ecad1(0x221)]('target')||'_self';switch(_0x634c75){case'action':let _0x4e4b60=_0x1eeede[_0x5ecad1(0x221)]('name');if(!_0x4e4b60)return;this['do_action'](_0x4e4b60);break;case'object':let _0x58e6e2=_0x1eeede[_0x5ecad1(0x221)]('model'),_0x210e31=_0x1eeede['attr']('name'),_0x272032=_0x1eeede[_0x5ecad1(0x221)]('context')||'{}';if(!_0x58e6e2||!_0x210e31)return;_0x272032&&(_0x272032=_0x505271[_0x5ecad1(0x206)](_0x272032));_0x272032=_[_0x5ecad1(0x208)]({'dashboard_id':this[_0x5ecad1(0x1e7)]},this[_0x5ecad1(0x1e9)]()[_0x5ecad1(0x1eb)],_0x272032),this['_rpc']({'model':_0x58e6e2,'method':_0x210e31,'context':_0x272032,'args':[]})[_0x5ecad1(0x1ed)](_0x913ae4=>{_0x913ae4&&this['do_action'](_0x913ae4);});break;}},'_do_search':function(_0x51d52e){const _0x2364f9=_0x24e856;_0x51d52e['stopPropagation']();let _0x3be64a=this[_0x2364f9(0x22d)][_0x2364f9(0x214)]('.search_group'),_0x632787=[];_0x3be64a['each']((_0x5ab1e8,_0x30b14c)=>{const _0x169246=_0x2364f9;let _0x5b7f99=grapesjs['$'](_0x30b14c),_0x56fdbd=_0x5b7f99[_0x169246(0x1f1)]('model'),_0x2ebb7d=_0x56fdbd[_0x169246(0x21c)]();_0x2ebb7d&&_0x632787[_0x169246(0x228)](_0x2ebb7d);}),_0x632787=_[_0x2364f9(0x1ef)](_0x632787,_0x22cba4=>{const _0x48ee39=_0x2364f9;return _0x22cba4[_0x48ee39(0x217)]=='global'?0x0:0x1;}),_0x5426e1[_0x2364f9(0x1c8)]['trigger']('mana_dashboard.do_search',_0x632787);},'destroy':function(){const _0x134ca8=_0x24e856;if(this[_0x134ca8(0x201)]){this['editor']['select']();let _super=this._super;setTimeout(()=>{const _0x478d13=_0x134ca8;this[_0x478d13(0x201)][_0x478d13(0x20f)](),this[_0x478d13(0x201)]=null,_super[_0x478d13(0x213)](this,arguments);},0x0);}}});return _0x5426e1[_0x24e856(0x1fb)]['add']('mana_dashboard',_0x53b306),_0x53b306;}));function a0_0x3b71(){const _0x386fce=['addAttributes','default_template_cache','forEach','454895FJbYUj','category','editor','config_id','1595022HRJdMD','data_source_type_name','drilling','py_eval','parse','extend','template_inited','addButton','components','init_action_blocks','remove','template_external_id','destroy','format','keys','set_theme','apply','find','style_urls','height','type','_on_editor_ready','template','length','has_domain_field','get_search_group_info','action_block_svg','default_template_info','full_name','template_id','attr','js_urls','width','params','Canvas','save_dashboard','get_categories','push','top','<div\x20class=\x22d-flex\x20flex-column\x20align-items-center\x20justify-content-center\x22><div\x20class=\x22chart-icon\x22>','resolve','trigger','$el','reload_config','view','get_theme_name','toHTML','scripts','themeData','add','model','get_data_source','includes','theme','split','name','BlockManager','domain','lang','set_cavas_preview','special','currentTarget','field_name','get_custom_css_id','values','style','dashboard_html','load_custom_css','addPanel','config_name','209402WNHhZx','loaded_libs','append','define','action_blocks','margin','ref_config_id','context','replace','runCommand','load_favorite_blocks','component_type','displayNotification','3483032sgxEIy','get_config_id','bus','theme_builder','onReady','435870rmQkXY','getElement','endOf','75326OFvMoD','</div></div>','custom_css','parent','dashboard_data','_loaDashboard','model_name','appendChild','getCss','_rpc','i18n','index','239035CiTEVa','set','on_component_remove','getElementsByTagName','_bind_editor_events','prototype','getSelected','loadCSS','\x0a\x20\x20\x20\x20<div\x20class=\x22o_content\x22\x20data-gjs-type=\x22content\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22container\x22\x20class=\x22container-fluid\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22bsrow\x22\x20class=\x22row\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22bsrow\x22\x20class=\x22row\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22bsrow\x22\x20class=\x22row\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22bsrow\x22\x20class=\x22row\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22column\x22\x20class=\x22col\x20col-md-4\x20col-sm-12\x22>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<div\x20data-gjs-type=\x22empty_card\x22\x20draggable=\x22true\x22\x20class=\x22card\x22></div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20\x20\x20\x20\x20</div>\x0a\x20\x20\x20\x20</div>','mode','registCommonds','get','eval','dashboard_id','startOf','getSession','loadJS','user_context','content','then','Panels','sortBy','innerHTML','data','value','do_action','init_action_block','padding','svg_icon','theme_info','16AGMQCR','registerTheme','ref_config','action_registry'];a0_0x3b71=function(){return _0x386fce;};return a0_0x3b71();}