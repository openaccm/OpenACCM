function a0_0x94f0(_0x1b405a,_0x386eb1){const _0x5aac02=a0_0x5aac();return a0_0x94f0=function(_0x94f06e,_0x9a6dfd){_0x94f06e=_0x94f06e-0x1cf;let _0x1eb5b2=_0x5aac02[_0x94f06e];return _0x1eb5b2;},a0_0x94f0(_0x1b405a,_0x386eb1);}(function(_0x1f4241,_0x591752){const _0x3db3ee=a0_0x94f0,_0x5b8260=_0x1f4241();while(!![]){try{const _0x209184=-parseInt(_0x3db3ee(0x1f9))/0x1*(parseInt(_0x3db3ee(0x1db))/0x2)+parseInt(_0x3db3ee(0x1e2))/0x3+parseInt(_0x3db3ee(0x1da))/0x4*(parseInt(_0x3db3ee(0x1d3))/0x5)+-parseInt(_0x3db3ee(0x1fa))/0x6*(-parseInt(_0x3db3ee(0x1ec))/0x7)+parseInt(_0x3db3ee(0x1d9))/0x8+-parseInt(_0x3db3ee(0x1ea))/0x9*(-parseInt(_0x3db3ee(0x1e0))/0xa)+-parseInt(_0x3db3ee(0x1cf))/0xb*(parseInt(_0x3db3ee(0x1d0))/0xc);if(_0x209184===_0x591752)break;else _0x5b8260['push'](_0x5b8260['shift']());}catch(_0x3aa5b0){_0x5b8260['push'](_0x5b8260['shift']());}}}(a0_0x5aac,0x5ff9f),odoo['define']('mana_dashboard.search_select',function(require){'use strict';const _0x4c10e0=a0_0x94f0;const _0x4d6c91=require('mana_dashboard.block_registry'),_0x2c0c43=require('mana_dashboard.icons'),_0x4fe9bf=require('web.core'),_0x275d0b=_0x4fe9bf['_t'],_0x3fee78=_0x4fe9bf[_0x4c10e0(0x1e8)],_0x193157=require('mana_dashboard.search_item_base'),_0x50192e=_0x193157[_0x4c10e0(0x1f2)],_0x3e0535=_0x193157[_0x4c10e0(0x1ee)];let _0x4e0955=[{'value':'=','name':'='},{'value':'!=','name':'!='},{'value':'ilike','name':'ilike'},{'value':'like','name':'like'},{'value':'not ilike','name':'not ilike'},{'value':'not like','name':'not like'}];function _0x533fcf(_0x2b6c71,_0x3015ff){const _0x57eb0b=_0x4c10e0,_0x55418c=_0x2b6c71[_0x57eb0b(0x1d1)];_0x2b6c71[_0x57eb0b(0x1de)]['add']('search_select',{'label':_0x275d0b('Search Input'),'category':_0x275d0b('Search'),'select':!![],'render':()=>{const _0x468682=_0x57eb0b;return _0x468682(0x1e3)+_0x2c0c43[_0x468682(0x1f5)]+_0x468682(0x1f3);},'content':{'type':'search_select'}}),_0x55418c[_0x57eb0b(0x1ed)]('search_select',{'model':_0x50192e[_0x57eb0b(0x1d7)]({'defaults':{'tagName':'div',..._0x50192e[_0x57eb0b(0x1e1)][_0x57eb0b(0x1fb)],'name':_0x275d0b('Search Select'),'operators':_0x4e0955,'default_operator':'ilike','search_template':'mana_dashboard.search_select','classes':_0x50192e[_0x57eb0b(0x1e1)][_0x57eb0b(0x1fb)][_0x57eb0b(0x1f1)]['concat'](['search_select']),'traits':_0x50192e[_0x57eb0b(0x1e1)][_0x57eb0b(0x1fb)][_0x57eb0b(0x1fd)][_0x57eb0b(0x1fc)]([{'type':'select','label':'Operator','name':'operator','options':_0x4e0955},{'type':'text','textarea':!![],'label':'Options','name':'options'}]),'attributes':_[_0x57eb0b(0x1d7)]({},_0x50192e[_0x57eb0b(0x1e1)][_0x57eb0b(0x1fb)]['attributes'],{'operator':'ilike','submit_empty':'false','options':'key1,val1\nkey2,val2\nkey3,val3'})},'initialize'(){const _0x267a23=_0x57eb0b;_0x50192e['prototype'][_0x267a23(0x1d5)][_0x267a23(0x1df)](this,arguments);},'resetSearch':function(){const _0x2f1cd1=_0x57eb0b;this['view']&&(this[_0x2f1cd1(0x1f8)]['el']['value']=''),this['resetOperator']();},'getSearchInfo'(){const _0xad982=_0x57eb0b;if(this[_0xad982(0x1f8)]){const _0x191fa9=this[_0xad982(0x1f8)]['el'][_0xad982(0x1e7)],_0x1d4f0e=this['get']('attributes');let _0x2f2fb3=_0x1d4f0e&&_0x1d4f0e[_0xad982(0x1d2)];if(!_0x2f2fb3||_0x2f2fb3=='')return null;let _0x3ab88e=_0x1d4f0e[_0xad982(0x1f0)]||this[_0xad982(0x1eb)][_0xad982(0x1e4)]('default_operator'),_0x4eb6cc=_0x1d4f0e['submit_empty']=='true'?!![]:![];if(_0x191fa9){if(!_0x4eb6cc&&(_0x191fa9==''||_0x191fa9==null))return null;return{'key':_0x2f2fb3,'operator':_0x3ab88e,'value':_0x191fa9,'type':'search_select','logic_type':'and'};}}return null;}},{'isComponent':_0x4cb2ae=>{const _0x45dd2e=_0x57eb0b;if(_0x4cb2ae&&_0x4cb2ae[_0x45dd2e(0x1d8)]&&_0x4cb2ae['classList'][_0x45dd2e(0x1dc)]('search_select'))return{'type':'search_select'};}}),'view':_0x3e0535[_0x57eb0b(0x1d7)]({'events':{'change select':'onChange'},'onChange'(_0x189829){const _0x14fdc6=_0x57eb0b;this[_0x14fdc6(0x1e6)]();},'init'(){const _0x323808=_0x57eb0b;_0x3e0535[_0x323808(0x1e1)]['init']['apply'](this,arguments),this[_0x323808(0x1f4)](this[_0x323808(0x1eb)],'change:attributes:options',this['render']),this['listenTo'](this[_0x323808(0x1eb)],'change:attributes:operator',this[_0x323808(0x1f6)]);},'removed'(){const _0x16e988=_0x57eb0b;_0x3e0535[_0x16e988(0x1e1)][_0x16e988(0x1ef)]['apply'](this,arguments);},'render'(..._0x525d9c){const _0xc2d86f=_0x57eb0b;return _0x3e0535['prototype']['render'][_0xc2d86f(0x1df)](this,_0x525d9c),this['model'][_0xc2d86f(0x1e4)]('components')[_0xc2d86f(0x1e9)]==0x0&&this[_0xc2d86f(0x1eb)][_0xc2d86f(0x1e5)](),$(this[_0xc2d86f(0x1d4)][_0xc2d86f(0x1d6)]('select'))[_0xc2d86f(0x1f7)]({'width':'100%'}),this;}})});}return _0x4d6c91[_0x4c10e0(0x1dd)]('search_select',_0x533fcf),_0x533fcf;}));function a0_0x5aac(){const _0x5aa701=['404BLyWVV','contains','add','BlockManager','apply','152070PwtQyu','prototype','933657zkgVuc','<div\x20class=\x22d-flex\x20flex-column\x20align-items-center\x20justify-content-center\x22><div\x20class=\x22chart-icon\x22>','get','updateContent','trigger_change','value','qweb','length','360qIOETr','model','844235muXhgU','addType','SearchItemView','removed','operator','classes','SearchItemModel','</div><div\x20class=\x27anita-block-label\x27>Select</div></div>','listenTo','select_svg','render','select2','view','2793ZOarZy','30ntuzzV','defaults','concat','traits','165GoGTmG','1483140nPyOfp','DomComponents','key','3807905iWhMSm','$el','initialize','find','extend','classList','4217000UkKKHq','4RnYvwg'];a0_0x5aac=function(){return _0x5aa701;};return a0_0x5aac();}