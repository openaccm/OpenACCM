function a0_0x4966(_0x3406c2,_0x41d4a7){const _0x3ac9f7=a0_0x3ac9();return a0_0x4966=function(_0x496626,_0x3da4f3){_0x496626=_0x496626-0x86;let _0x2e7e5a=_0x3ac9f7[_0x496626];return _0x2e7e5a;},a0_0x4966(_0x3406c2,_0x41d4a7);}const a0_0x4810ff=a0_0x4966;(function(_0x2221e2,_0xde27d2){const _0x9f6ea6=a0_0x4966,_0x3d9e1b=_0x2221e2();while(!![]){try{const _0x20a5aa=-parseInt(_0x9f6ea6(0x8c))/0x1+parseInt(_0x9f6ea6(0xa6))/0x2+-parseInt(_0x9f6ea6(0xad))/0x3*(parseInt(_0x9f6ea6(0xa7))/0x4)+parseInt(_0x9f6ea6(0xa8))/0x5*(parseInt(_0x9f6ea6(0x87))/0x6)+parseInt(_0x9f6ea6(0x8d))/0x7*(-parseInt(_0x9f6ea6(0x93))/0x8)+parseInt(_0x9f6ea6(0xa9))/0x9+-parseInt(_0x9f6ea6(0x92))/0xa*(-parseInt(_0x9f6ea6(0x99))/0xb);if(_0x20a5aa===_0xde27d2)break;else _0x3d9e1b['push'](_0x3d9e1b['shift']());}catch(_0x331d46){_0x3d9e1b['push'](_0x3d9e1b['shift']());}}}(a0_0x3ac9,0x61c88),odoo[a0_0x4810ff(0x8a)]('mana_dashboard.search_tab',function(require){'use strict';const _0x967ec8=a0_0x4810ff;const _0x508fc9=require('mana_dashboard.block_registry'),_0x391f07=require('mana_dashboard.icons'),_0x2353a9=require('web.core'),_0x355e5d=_0x2353a9['_t'],_0x55681c=_0x2353a9['qweb'],_0x536337=require('mana_dashboard.search_item_base'),_0x3c65b0=_0x536337[_0x967ec8(0xb1)],_0x4ed85e=_0x536337[_0x967ec8(0xa4)];let _0x35b7ef=[{'value':'=','name':'='},{'value':'!=','name':'!='},{'value':'ilike','name':'ilike'},{'value':'like','name':'like'},{'value':'not ilike','name':'not ilike'},{'value':'not like','name':'not like'}];function _0x3ec792(_0x31d5cb,_0x60d78d){const _0x3e217b=_0x967ec8,_0x5b62bb=_0x31d5cb[_0x3e217b(0x88)];_0x31d5cb[_0x3e217b(0x89)][_0x3e217b(0xa1)]('search_tab',{'label':_0x355e5d('Search Tab'),'category':_0x355e5d('Search'),'select':!![],'render':()=>{const _0x5f5967=_0x3e217b;return'<div\x20class=\x22d-flex\x20flex-column\x20align-items-center\x20justify-content-center\x22><div\x20class=\x22chart-icon\x22>'+_0x391f07[_0x5f5967(0xa2)]+'</div><div\x20class=\x27anita-block-label\x27>Tab</div></div>';},'content':{'type':'search_tab'}}),_0x5b62bb[_0x3e217b(0xa3)]('search_tab',{'model':_0x3c65b0[_0x3e217b(0xae)]({'defaults':{..._0x3c65b0[_0x3e217b(0x91)][_0x3e217b(0x86)],'name':_0x355e5d('Search Tab'),'droppable':'.search_group','operators':_0x35b7ef,'default_operator':'ilike','search_template':'mana_dashboard.search_tab','classes':_0x3c65b0[_0x3e217b(0x91)][_0x3e217b(0x86)][_0x3e217b(0x8b)]['concat'](['search_tab']),'traits':_0x3c65b0[_0x3e217b(0x91)][_0x3e217b(0x86)][_0x3e217b(0x9a)]['concat']([{'type':'select','label':'Operator','name':'operator','options':_0x35b7ef},{'type':'text','textarea':!![],'label':'Options','name':'options'},{'type':'class_select','label':'Tab Style','name':'tab_style','options':[{'value':'nav-tabs','name':'Tabs'},{'value':'nav-pills','name':'Pills'},{'value':'nav-line','name':'Line'}]}]),'attributes':_[_0x3e217b(0xae)]({},_0x3c65b0['prototype'][_0x3e217b(0x86)][_0x3e217b(0x90)],{'operator':'=','submit_empty':![],'tab_style':'nav-line','options':'key1,val1\nkey2,val2\nkey3,val3'}),'operators':_0x35b7ef},'initialize'(){const _0x43d47f=_0x3e217b;_0x3c65b0[_0x43d47f(0x91)][_0x43d47f(0x9d)]['apply'](this,arguments);},'reset_search':function(){const _0x59ed7d=_0x3e217b;this[_0x59ed7d(0x9b)]();},'getSearchInfo'(){const _0x3efcd6=_0x3e217b;if(this['view']){let _0x54cdc9=this['view']['el'][_0x3efcd6(0x9e)]('.nav-link.active');if(!_0x54cdc9)return null;let _0x32c7d1=_0x54cdc9&&_0x54cdc9[_0x3efcd6(0x95)]('value');const _0xf70a84=this[_0x3efcd6(0x8f)]('attributes');let _0x5a75fe=_0xf70a84&&_0xf70a84['key'];if(!_0x5a75fe||_0x5a75fe=='')return null;let _0x3ad9b7=_0xf70a84[_0x3efcd6(0x9f)]||this['model']['get']('default_operator'),_0x208302=_0xf70a84[_0x3efcd6(0xa0)]=='true'?!![]:![];if(_0x32c7d1){if(!_0x208302&&(_0x32c7d1==''||_0x32c7d1==null))return null;return{'key':_0x5a75fe,'operator':_0x3ad9b7,'value':_0x32c7d1,'type':'search_tab','logic_type':this[_0x3efcd6(0x8f)]('attributes')[_0x3efcd6(0x9c)]||'and'};}}return null;}},{'isComponent':_0x44089e=>{const _0x4404ea=_0x3e217b;if(_0x44089e&&_0x44089e['classList']&&_0x44089e['classList'][_0x4404ea(0xac)]('search_tab'))return{'type':'search_tab'};}}),'view':_0x4ed85e[_0x3e217b(0xae)]({'events':{'click .nav-item':'handleClick'},'handleClick'(_0x24c6f9){const _0x46c546=_0x3e217b;let _0x42cd6c=_0x24c6f9[_0x46c546(0xab)];$(_0x42cd6c)[_0x46c546(0x97)]('show'),_0x24c6f9[_0x46c546(0x96)](),this['trigger_change']();},'init'(){const _0xaa33b9=_0x3e217b;_0x4ed85e[_0xaa33b9(0x91)][_0xaa33b9(0xb0)]['apply'](this,arguments),this[_0xaa33b9(0xaf)](this[_0xaa33b9(0xa5)],'change:attributes:options',this[_0xaa33b9(0x8e)]),this['listenTo'](this['model'],'change:attributes:operator',this[_0xaa33b9(0x8e)]);},'removed'(){const _0x12dfd6=_0x3e217b;_0x4ed85e[_0x12dfd6(0x91)][_0x12dfd6(0x94)][_0x12dfd6(0xaa)](this,arguments);},'render'(..._0x12a29c){const _0x5c463b=_0x3e217b;return _0x4ed85e[_0x5c463b(0x91)]['render']['apply'](this,_0x12a29c),this[_0x5c463b(0xa5)][_0x5c463b(0x8f)]('components')[_0x5c463b(0x98)]==0x0&&this[_0x5c463b(0xa5)]['updateContent'](),this;}})});}return _0x508fc9['add']('search_tab',_0x3ec792),_0x3ec792;}));function a0_0x3ac9(){const _0x5ebc71=['DomComponents','BlockManager','define','classes','721956XtrCgU','392KjpPAc','render','get','attributes','prototype','9018250NQtLOp','92744suwaDw','removed','getAttribute','preventDefault','tab','length','11rtFxDY','traits','resetOperator','logic_type','initialize','querySelector','operator','submit_empty','add','tab_svg','addType','SearchItemView','model','829702VfXqIe','4RgkkiA','5FClKlf','6208659DQCaAs','apply','target','contains','839199rBYPhc','extend','listenTo','init','SearchItemModel','defaults','269340PcvvSJ'];a0_0x3ac9=function(){return _0x5ebc71;};return a0_0x3ac9();}