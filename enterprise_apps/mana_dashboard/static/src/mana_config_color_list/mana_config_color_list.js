/** @odoo-module alias=mana_dashboard.config_color_list **/
var a0_0x528831=a0_0x2bd8;(function(_0x5985dd,_0x1fe667){var _0x6d0b3d=a0_0x2bd8,_0x1ca3df=_0x5985dd();while(!![]){try{var _0x14fd20=-parseInt(_0x6d0b3d(0x10e))/0x1*(-parseInt(_0x6d0b3d(0x10f))/0x2)+parseInt(_0x6d0b3d(0x111))/0x3+-parseInt(_0x6d0b3d(0x115))/0x4+-parseInt(_0x6d0b3d(0x10a))/0x5+parseInt(_0x6d0b3d(0x10c))/0x6+parseInt(_0x6d0b3d(0x109))/0x7*(-parseInt(_0x6d0b3d(0x10b))/0x8)+parseInt(_0x6d0b3d(0x114))/0x9;if(_0x14fd20===_0x1fe667)break;else _0x1ca3df['push'](_0x1ca3df['shift']());}catch(_0x5bae84){_0x1ca3df['push'](_0x1ca3df['shift']());}}}(a0_0x5c6a,0xcb0e0));
 import {_lt}  from '@web/core/l10n/translation';
 import {Component,useEffect,useState,useRef,onMounted}  from '@odoo/owl';
 function a0_0x2bd8(_0x40f958,_0x4b02a0){var _0x5c6a16=a0_0x5c6a();return a0_0x2bd8=function(_0x2bd856,_0x523d97){_0x2bd856=_0x2bd856-0x109;var _0x222255=_0x5c6a16[_0x2bd856];return _0x222255;},a0_0x2bd8(_0x40f958,_0x4b02a0);}
 function a0_0x5c6a(){var _0x254ea9=['662193YrjwXr','4071350RBnCcL','120FVUdHW','9152154rTdyFP','props','7vJLvBc','234548QqjvnQ','defaultProps','4259712OFgBpg','components','setup','4603941yqOGgS','4851052skaAJt'];a0_0x5c6a=function(){return _0x254ea9;};return a0_0x5c6a();}
 import  ManaColorPickerList  from 'mana_dashboard.color_picker_list';
export  default class ManaConfigColorList extends Component{[a0_0x528831(0x113)](){}};ManaConfigColorList[a0_0x528831(0x10d)]={'title':{'type':String,'optional':0x1},'canDisable':{'type':Boolean,'optional':0x1},'enabled':{'type':Boolean,'optional':0x1},'colors':{'type':Array,'optional':0x1},'onChange':{'type':Function,'optional':!![]},'onChangeEnabled':{'type':Function,'optional':!![]}},ManaConfigColorList[a0_0x528831(0x110)]={'canDisable':![],'enabled':!![],'onChange':()=>{},'onChangeEnabled':()=>{}},ManaConfigColorList[a0_0x528831(0x112)]={'ManaColorPickerList':ManaColorPickerList},ManaConfigColorList['template']='mana_dashboard.color_list_config';