(function(_0x22054b,_0x4effb1){const _0x40cc44=a0_0x190f,_0x2f056b=_0x22054b();while(!![]){try{const _0x25496c=-parseInt(_0x40cc44(0x91))/0x1+parseInt(_0x40cc44(0xd6))/0x2*(parseInt(_0x40cc44(0xa4))/0x3)+-parseInt(_0x40cc44(0xcf))/0x4+-parseInt(_0x40cc44(0x98))/0x5*(parseInt(_0x40cc44(0x89))/0x6)+-parseInt(_0x40cc44(0x95))/0x7+parseInt(_0x40cc44(0xd3))/0x8+-parseInt(_0x40cc44(0xcd))/0x9*(-parseInt(_0x40cc44(0xb9))/0xa);if(_0x25496c===_0x4effb1)break;else _0x2f056b['push'](_0x2f056b['shift']());}catch(_0x501d96){_0x2f056b['push'](_0x2f056b['shift']());}}}(a0_0x3959,0xab72c),odoo['define']('mana_dashboard.data_source',function(require){'use strict';const _0x4be940=a0_0x190f;let _0x3fbc79=require('mana_dashboard.record');class _0x55d6cc{constructor(_0x1ee9c7,_0x1c7492){const _0x7400c9=a0_0x190f;this['datas']=_0x1ee9c7[_0x7400c9(0xc0)],this[_0x7400c9(0xc1)]=_0x1ee9c7[_0x7400c9(0xc1)],this[_0x7400c9(0xba)]=this[_0x7400c9(0xc1)]['result_type'],this[_0x7400c9(0x8c)]=this[_0x7400c9(0xc1)][_0x7400c9(0xe2)],this['records']=[],this[_0x7400c9(0xd4)]=_0x1ee9c7[_0x7400c9(0xd4)],this[_0x7400c9(0xab)]=_0x1c7492,this[_0x7400c9(0x8d)]=this[_0x7400c9(0xc1)][_0x7400c9(0xa8)],this[_0x7400c9(0xa1)]={},this[_0x7400c9(0xa2)](),!this[_0x7400c9(0x99)]()&&this[_0x7400c9(0xce)]();}[_0x4be940(0xa8)](){const _0x4cb43b=_0x4be940;return this[_0x4cb43b(0x8d)];}get['valid'](){const _0x45f6d2=_0x4be940;return this[_0x45f6d2(0x8d)];}[_0x4be940(0xce)](){const _0x3fab81=_0x4be940;if(!this[_0x3fab81(0xc0)]||!Array[_0x3fab81(0x8a)](this['datas'])){this[_0x3fab81(0xbc)]=[],this[_0x3fab81(0x8d)]=![];return;}let _0x391e8a=[];for(let _0x36aff2=0x0;_0x36aff2<this[_0x3fab81(0xc0)]['length'];_0x36aff2++){let _0xf87951=this['datas'][_0x36aff2],_0x3b64ef=new _0x3fbc79(_0xf87951);_0x391e8a[_0x3fab81(0xd2)](_0x3b64ef);}this[_0x3fab81(0xbc)]=_0x391e8a;}[_0x4be940(0xa2)](){const _0x1ad505=_0x4be940;if(!this[_0x1ad505(0xc1)][_0x1ad505(0xa0)])return;this[_0x1ad505(0xa1)]={};for(let _0x1d9ff9=0x0;_0x1d9ff9<this[_0x1ad505(0xc1)]['raw_fields'][_0x1ad505(0x9d)];_0x1d9ff9++){let _0x32ff43=this['data_source_info'][_0x1ad505(0xa0)][_0x1d9ff9];this[_0x1ad505(0xa1)][_0x32ff43[_0x1ad505(0xc6)]]=_0x32ff43;}}['is_custom'](){const _0x3dacd2=_0x4be940;return this[_0x3dacd2(0xba)]!='Standard';}[_0x4be940(0x93)](){const _0x21e527=_0x4be940;return this[_0x21e527(0xc1)][_0x21e527(0xcb)];}['get_context'](){const _0x25cb6b=_0x4be940;return this[_0x25cb6b(0xc1)]['context'];}[_0x4be940(0x9a)](){const _0x114b7b=_0x4be940;if(this[_0x114b7b(0xc1)]['data_source_type_name']=='model')return!![];return![];}['is_get_data_from_sql'](){const _0x109e96=_0x4be940;if(this[_0x109e96(0xc1)][_0x109e96(0xe2)]=='sql')return!![];return![];}get[_0x4be940(0xbb)](){return this['datas'];}[_0x4be940(0xc7)](){const _0x314c60=_0x4be940;return this[_0x314c60(0xc0)];}[_0x4be940(0xd9)](){const _0x197074=_0x4be940;return this[_0x197074(0xbc)];}[_0x4be940(0xd8)](_0x1b2231){const _0x159cf0=_0x4be940;return this[_0x159cf0(0xbc)][_0x1b2231];}[_0x4be940(0xc4)](_0x17e2f0,_0x1858f7){const _0x43f75c=_0x4be940;for(let _0x3a6132=0x0;_0x3a6132<this[_0x43f75c(0xbc)][_0x43f75c(0x9d)];_0x3a6132++){let _0x1f6d99=this[_0x43f75c(0xbc)][_0x3a6132],_0x13f3ff=_0x1f6d99[_0x43f75c(0xe3)](_0x17e2f0);if(_0x13f3ff==_0x1858f7)return _0x1f6d99;}return null;}['get_records_count'](){const _0xb9f6e8=_0x4be940;return this['records'][_0xb9f6e8(0x9d)];}[_0x4be940(0xe1)](){const _0x55dfe6=_0x4be940;if(!this['data_source_info'][_0x55dfe6(0xa0)])return[];this[_0x55dfe6(0xa1)]={};for(let _0x55bc82=0x0;_0x55bc82<this[_0x55dfe6(0xc1)][_0x55dfe6(0xa0)][_0x55dfe6(0x9d)];_0x55bc82++){let _0x3ba26c=this[_0x55dfe6(0xc1)][_0x55dfe6(0xa0)][_0x55bc82];this[_0x55dfe6(0xa1)][_0x3ba26c[_0x55dfe6(0xc6)]]=_0x3ba26c;}return this[_0x55dfe6(0xc1)]['raw_fields'];}[_0x4be940(0xae)](){return this['data_source_info']['data_source_type_name'];}['get_data_source_info'](){const _0x58e73e=_0x4be940;return this[_0x58e73e(0xc1)];}[_0x4be940(0xae)](){return this['data_source_info']['data_source_type_name'];}['has_group_by'](){const _0x1f97ed=_0x4be940;if(this['is_get_data_from_model']())return this[_0x1f97ed(0xc1)][_0x1f97ed(0xde)]&&this['data_source_info']['group_by_infos'][_0x1f97ed(0x9d)]>0x0;else{let _0x1bec16=this[_0x1f97ed(0xe1)]();for(let _0x4ccf1c=0x0;_0x4ccf1c<_0x1bec16[_0x1f97ed(0x9d)];_0x4ccf1c++){let _0x24bf0b=_0x1bec16[_0x4ccf1c];if(_0x24bf0b[_0x1f97ed(0x9b)])return!![];}}return![];}[_0x4be940(0xca)](){const _0x282ec2=_0x4be940;if(this[_0x282ec2(0x9a)]())return this['data_source_info'][_0x282ec2(0xde)]&&this[_0x282ec2(0xc1)][_0x282ec2(0xde)][_0x282ec2(0x9d)]>0x1;else{let _0x6e838b=this['get_raw_fields'](),_0x232a94=0x0;for(let _0x1976b5=0x0;_0x1976b5<_0x6e838b[_0x282ec2(0x9d)];_0x1976b5++){let _0x72aad8=_0x6e838b[_0x1976b5];_0x72aad8[_0x282ec2(0x9b)]&&_0x232a94++;}return _0x232a94>0x1;}}[_0x4be940(0xb3)](){const _0x581f0a=_0x4be940;let _0x2d3fb3=this['get_raw_fields']();for(let _0x578b37=0x0;_0x578b37<_0x2d3fb3[_0x581f0a(0x9d)];_0x578b37++){let _0x138abc=_0x2d3fb3[_0x578b37];if(_0x138abc[_0x581f0a(0xc6)]=='__domain')return!![];}return![];}[_0x4be940(0xb7)](){const _0x3da4bb=_0x4be940;if(this['data_source_info'][_0x3da4bb(0xde)])return this[_0x3da4bb(0xc1)]['group_by_infos'][0x0];return null;}['has_order_by'](){const _0x1c6ea9=_0x4be940;if(this[_0x1c6ea9(0xc1)][_0x1c6ea9(0xaa)])return!![];return![];}[_0x4be940(0xc5)](){const _0x45b784=_0x4be940;if(this[_0x45b784(0xc1)]['order_by_infos']&&this[_0x45b784(0xc1)]['order_by_infos'][_0x45b784(0x9d)]>0x1)return!![];return![];}['get_fields_info'](){const _0x107b64=_0x4be940;if(!this['data_source_info']['model_fields'])return[];return this[_0x107b64(0xc1)][_0x107b64(0xbe)];}[_0x4be940(0xe4)](){const _0xdfabe5=_0x4be940;if(!this[_0xdfabe5(0xc1)][_0xdfabe5(0xde)])return[];return this[_0xdfabe5(0xc1)][_0xdfabe5(0xde)];}[_0x4be940(0xc9)](){const _0xbe5707=_0x4be940;return this[_0xbe5707(0xc1)]['name'];}[_0x4be940(0x97)](_0x1daf03){const _0x13f9e9=_0x4be940;let _0x14e939=0x0;for(let _0x4a08b3=0x0;_0x4a08b3<this[_0x13f9e9(0xbc)]['length'];_0x4a08b3++){let _0x1cb35a=this[_0x13f9e9(0xbc)][_0x4a08b3],_0x3c3347=_0x1cb35a['get_value'](_0x1daf03);_0x3c3347>_0x14e939&&(_0x14e939=_0x3c3347);}return _0x14e939;}[_0x4be940(0xa3)](){const _0xab813d=_0x4be940;let _0x456c63=[];if(this['is_get_data_from_model']()){let _0x4542b6=this[_0xab813d(0xc3)]();for(let _0x43f8a7=0x0;_0x43f8a7<_0x4542b6[_0xab813d(0x9d)];_0x43f8a7++){let _0x267401=_0x4542b6[_0x43f8a7];_0x267401[_0xab813d(0x9e)]&&_0x456c63[_0xab813d(0xd2)](_0x267401);}if(_0x456c63['length']>0x0)return _0x456c63;else{let _0xc6de8b=this['get_group_by_infos']();if(_0xc6de8b['length']>0x0){let _0x56000a=_0xc6de8b[0x0];_0x456c63[_0xab813d(0xd2)](_0x56000a);}}}return _0x456c63;}['get_categories'](){const _0x2589a7=_0x4be940;let _0x44484d=[];if(this[_0x2589a7(0x9a)]()){let _0x52547c=this[_0x2589a7(0xc3)]();for(let _0x2bfa8a=0x0;_0x2bfa8a<_0x52547c[_0x2589a7(0x9d)];_0x2bfa8a++){let _0x1e9f6f=_0x52547c[_0x2bfa8a];_0x1e9f6f[_0x2589a7(0x9e)]&&_0x44484d['push'](_0x1e9f6f[_0x2589a7(0x8f)]);}if(_0x44484d[_0x2589a7(0x9d)]>0x0)return _0x44484d;else{let _0x4a7de4=this[_0x2589a7(0xe4)]();if(_0x4a7de4[_0x2589a7(0x9d)]>0x0){let _0x1fa5f9=_0x4a7de4[0x0];_0x44484d['push'](_0x1fa5f9[_0x2589a7(0x8f)]);}}}else{let _0x12a41=this[_0x2589a7(0xe1)]();for(let _0x2136a7=0x0;_0x2136a7<_0x12a41['length'];_0x2136a7++){let _0x3955a2=_0x12a41[_0x2136a7];_0x3955a2[_0x2589a7(0xac)]&&_0x44484d[_0x2589a7(0xd2)](_0x3955a2['name']);}}return _0x44484d;}[_0x4be940(0xb5)](_0x659020){const _0x41f4a2=_0x4be940;let _0x2c7d5a=[];for(let _0x3f37bc=0x0;_0x3f37bc<this['records'][_0x41f4a2(0x9d)];_0x3f37bc++){let _0x595ef7=this['records'][_0x3f37bc],_0x2952f4=_0x595ef7[_0x41f4a2(0xe3)](_0x659020);_0x2c7d5a['push'](_0x2952f4);}return _0x2c7d5a;}[_0x4be940(0x96)](){const _0x136c3f=_0x4be940;if(this[_0x136c3f(0xbc)]['length']==0x0)return[];let _0xb5322=Object[_0x136c3f(0xa6)](this[_0x136c3f(0xbc)][0x0]['record']);return _0xb5322;}[_0x4be940(0xc2)](_0x3b4076){const _0x296485=_0x4be940;let _0x41d793=[];for(let _0xffb689=0x0;_0xffb689<this['records'][_0x296485(0x9d)];_0xffb689++){let _0x2841fe=this[_0x296485(0xbc)][_0xffb689],_0x323e76=_0x2841fe[_0x296485(0xe3)](_0x3b4076);_0x41d793['push'](_0x323e76);}return _0x41d793;}[_0x4be940(0x9c)](){const _0x5dec72=_0x4be940;let _0x3276db=[],_0x364170=this['get_dimension_values']();_0x3276db['push'](_0x364170);for(let _0xa8543e=0x0;_0xa8543e<this[_0x5dec72(0xbc)]['length'];_0xa8543e++){let _0x3bfe3d=this[_0x5dec72(0xbc)][_0xa8543e],_0x598593=[];for(let _0x1ef0e4=0x0;_0x1ef0e4<_0x364170['length'];_0x1ef0e4++){let _0x52072d=_0x364170[_0x1ef0e4],_0x535348=_0x3bfe3d[_0x5dec72(0xe3)](_0x52072d);_0x598593[_0x5dec72(0xd2)](_0x535348);}_0x3276db[_0x5dec72(0xd2)](_0x598593);}return _0x3276db;}['get_field_info_by_name'](_0x26f24b){const _0x1c2cf8=_0x4be940;let _0x9329fe=this[_0x1c2cf8(0xc3)]();for(let _0x2c5fe9=0x0;_0x2c5fe9<_0x9329fe['length'];_0x2c5fe9++){let _0xa4678e=_0x9329fe[_0x2c5fe9];if(_0xa4678e['field_name']==_0x26f24b)return _0xa4678e;}return null;}[_0x4be940(0xbd)](){const _0x284cd1=_0x4be940;let _0xc00510=[];if(this[_0x284cd1(0x9a)]()){let _0x598180=this['get_group_by_infos']();for(let _0x221884=0x0;_0x221884<_0x598180[_0x284cd1(0x9d)];_0x221884++){let _0x372019=_0x598180[_0x221884];_0xc00510[_0x284cd1(0xd2)](_0x372019[_0x284cd1(0xa7)]);}}else{let _0x4635f9=this[_0x284cd1(0xe1)]();for(let _0x28746e=0x0;_0x28746e<_0x4635f9[_0x284cd1(0x9d)];_0x28746e++){let _0x1aef4e=_0x4635f9[_0x28746e];_0x1aef4e[_0x284cd1(0x9b)]&&_0xc00510['push'](_0x1aef4e['name']);}}return _0xc00510;}[_0x4be940(0xb2)](){const _0x30ca1d=_0x4be940;let _0x3d3b4f=[],_0x4f044a=this['get_fields_info']();for(let _0x2ab8d5=0x0;_0x2ab8d5<_0x4f044a['length'];_0x2ab8d5++){let _0x315b10=_0x4f044a[_0x2ab8d5];_0x3d3b4f['push'](_0x315b10[_0x30ca1d(0xa7)]);}return _0x3d3b4f;}['get_raw_field_names'](){const _0x497d84=_0x4be940;let _0x21b187=[],_0x5b5ad6=this[_0x497d84(0xe1)]();for(let _0xbf541c=0x0;_0xbf541c<_0x5b5ad6['length'];_0xbf541c++){let _0x5d7a48=_0x5b5ad6[_0xbf541c];_0x21b187['push'](_0x5d7a48[_0x497d84(0xa7)]);}return _0x21b187;}['get_col_names'](){const _0x55bb60=_0x4be940;let _0x1ab365=[],_0xba802c=this[_0x55bb60(0xd9)]();if(_0xba802c[_0x55bb60(0x9d)]>0x0){let _0x3bb827=_0xba802c[0x0],_0x48e91d=_0x3bb827['get_col_names']();return _0x1ab365=_0x48e91d,_0x1ab365;}return[];}[_0x4be940(0xd5)](_0x391c70){const _0x4c0543=_0x4be940;return this[_0x4c0543(0xa1)][_0x391c70];}[_0x4be940(0x8b)](){const _0x40e386=_0x4be940;let _0x5d7c34=[],_0x5780ea=this[_0x40e386(0xe1)]();for(let _0x512da1=0x0;_0x512da1<_0x5780ea[_0x40e386(0x9d)];_0x512da1++){let _0x245aaa=_0x5780ea[_0x512da1];_0x245aaa[_0x40e386(0xd1)]&&_0x5d7c34[_0x40e386(0xd2)](_0x245aaa[_0x40e386(0xc6)]);}if(_0x5d7c34[_0x40e386(0x9d)]==0x0){if(this[_0x40e386(0x9a)]()){let _0x10dd8f=this['get_fields_info']();for(let _0xe374b0=0x0;_0xe374b0<_0x10dd8f['length'];_0xe374b0++){let _0x1f8f33=_0x10dd8f[_0xe374b0];_0x1f8f33[_0x40e386(0xd1)]&&_0x5d7c34[_0x40e386(0xd2)](_0x1f8f33[_0x40e386(0xa7)]);}if(_0x5d7c34['length']==0x0){for(let _0x12db6c=0x0;_0x12db6c<_0x5780ea['length'];_0x12db6c++){let _0x21181f=_0x5780ea[_0x12db6c];if(_0x21181f[_0x40e386(0xc6)]=='__count'){_0x5d7c34['push']('__count');break;}}let _0x19c6a8=this['get_col_names']();_0x19c6a8['indexOf']('__count')!=-0x1&&_0x5d7c34[_0x40e386(0xd2)]('__count');}if(_0x5d7c34[_0x40e386(0x9d)]==0x0){let _0xed93a3=this[_0x40e386(0xc3)]();for(let _0x595cdd=0x0;_0x595cdd<_0xed93a3[_0x40e386(0x9d)];_0x595cdd++){let _0x190050=_0xed93a3[_0x595cdd];(_0x190050[_0x40e386(0xda)]=='integer'||_0x190050[_0x40e386(0xda)]=='float')&&_0x5d7c34[_0x40e386(0xd2)](_0x190050[_0x40e386(0xa7)]);}}}}return _0x5d7c34=_['uniq'](_0x5d7c34),_0x5d7c34;}[_0x4be940(0xdd)](){const _0x337e8f=_0x4be940;let _0x535da9=[],_0x5836f9=this[_0x337e8f(0xe1)]();for(let _0xb7c892=0x0;_0xb7c892<_0x5836f9[_0x337e8f(0x9d)];_0xb7c892++){let _0x4bd56c=_0x5836f9[_0xb7c892];_0x4bd56c[_0x337e8f(0xb0)]&&_0x535da9['push'](_0x4bd56c);}return _0x535da9;}[_0x4be940(0xad)](){const _0x1079e3=_0x4be940;let _0x5b9522=this['get_aggregate_columns']();if(_0x5b9522['length']>0x0){let _0x1c68df=_0x5b9522[0x0],_0x4eb570=_0x1c68df[_0x1079e3(0xc6)],_0x2786e3=this[_0x1079e3(0xaf)](_0x4eb570,_0x1c68df[_0x1079e3(0xb0)]);return _0x2786e3;}else{let _0x51eaa7=this[_0x1079e3(0xa5)]();if(_0x51eaa7[_0x1079e3(0x8e)]('__count')!=-0x1){let _0x4a165c=this[_0x1079e3(0xaf)]('__count','sum');return _0x4a165c;}else{let _0x41e5db=this[_0x1079e3(0xd9)]();return _0x41e5db[_0x1079e3(0x9d)];}}}[_0x4be940(0xb1)](_0x2839ea){const _0x350cbf=_0x4be940;if(!_0x2839ea)return'';if(Array[_0x350cbf(0x8a)](_0x2839ea)){if(_0x2839ea[_0x350cbf(0x9d)]==0x2){if(Number[_0x350cbf(0xe5)](_0x2839ea[0x0])&&typeof _0x2839ea[0x1]==='string')return _0x2839ea[0x1];}return _0x2839ea[_0x350cbf(0xdb)](',');}return _0x2839ea;}['get_col_values'](_0x41908f,_0x3b6dc2=null){const _0x5c02a2=_0x4be940;let _0x32080e=[];for(let _0x47803b=0x0;_0x47803b<this[_0x5c02a2(0xbc)]['length'];_0x47803b++){let _0x2e2702=this[_0x5c02a2(0xbc)][_0x47803b],_0x5c743e=_0x2e2702[_0x5c02a2(0xe3)](_0x41908f);_0x3b6dc2&&(_0x5c743e=_0x3b6dc2(_0x5c743e)),_0x32080e[_0x5c02a2(0xd2)](_0x5c743e);}return _0x32080e;}[_0x4be940(0xb4)](_0x411f41,_0x4bf06c=![]){const _0x9521ea=_0x4be940;return this[_0x9521ea(0xc8)](_0x411f41,_0x4bf06c);}[_0x4be940(0xe0)](_0xa123a4,_0x5f5412=null){const _0x939d73=_0x4be940;let _0x38f8a6=this[_0x939d73(0xc8)](_0xa123a4,_0x5f5412);return _[_0x939d73(0xd0)](_0x38f8a6);}['get_aggregate_value'](_0x24c040,_0x107edb){let _0x495ac9=this['get_col_values'](_0x24c040),_0x455f9a=this['get_aggregate'](_0x495ac9,_0x107edb);return _0x455f9a;}[_0x4be940(0xb6)](_0x40d34e,_0x26aed3){const _0x3450df=_0x4be940;if(!_0x40d34e||_0x40d34e[_0x3450df(0x9d)]==0x0)return 0x0;let _0x21465f=0x0;if(_0x26aed3=='sum')_0x21465f=this[_0x3450df(0x90)](_0x40d34e);else{if(_0x26aed3=='avg')_0x21465f=this['get_avg'](_0x40d34e);else{if(_0x26aed3=='max')_0x21465f=this[_0x3450df(0x94)](_0x40d34e);else{if(_0x26aed3=='min')_0x21465f=this[_0x3450df(0xb8)](_0x40d34e);else _0x26aed3=='count'&&(_0x21465f=(_0x40d34e||[])['length']);}}}return _0x21465f;}[_0x4be940(0x90)](_0x1b53d0){const _0x117b2e=_0x4be940;let _0x9d060d=0x0;for(let _0x31123d=0x0;_0x31123d<_0x1b53d0[_0x117b2e(0x9d)];_0x31123d++){let _0x28a5ba=_0x1b53d0[_0x31123d];_0x9d060d+=_0x28a5ba;}return _0x9d060d;}[_0x4be940(0xa9)](_0x13a03f){const _0x222dcf=_0x4be940;let _0x47cdcd=this[_0x222dcf(0x90)](_0x13a03f),_0xe9a47e=_0x47cdcd/_0x13a03f[_0x222dcf(0x9d)];return _0xe9a47e;}[_0x4be940(0x94)](_0x1d1428){const _0x14fe29=_0x4be940;let _0x576701=_0x1d1428[0x0];for(let _0x55f9a0=0x1;_0x55f9a0<_0x1d1428[_0x14fe29(0x9d)];_0x55f9a0++){let _0x15ddd1=_0x1d1428[_0x55f9a0];_0x15ddd1>_0x576701&&(_0x576701=_0x15ddd1);}return _0x576701;}[_0x4be940(0xb8)](_0xd2c842){const _0xdd26e5=_0x4be940;let _0x4f11ce=_0xd2c842[0x0];for(let _0x43f9e7=0x1;_0x43f9e7<_0xd2c842[_0xdd26e5(0x9d)];_0x43f9e7++){let _0xff98a=_0xd2c842[_0x43f9e7];_0xff98a<_0x4f11ce&&(_0x4f11ce=_0xff98a);}return _0x4f11ce;}[_0x4be940(0xdf)](_0x56b60f){const _0x323e0d=_0x4be940;let _0x4d7faf=[];for(let _0x31ddc0=0x0;_0x31ddc0<this[_0x323e0d(0xbc)][_0x323e0d(0x9d)];_0x31ddc0++){let _0x2aa6d8=this['records'][_0x31ddc0],_0x56eaf3=[];for(let _0x32be76=0x0;_0x32be76<_0x56b60f[_0x323e0d(0x9d)];_0x32be76++){let _0x4d541a=_0x56b60f[_0x32be76],_0x4ecd23=_0x2aa6d8[_0x323e0d(0xe3)](_0x4d541a);_0x56eaf3[_0x323e0d(0xd2)](_0x4ecd23);}_0x4d7faf[_0x323e0d(0xd2)](_0x56eaf3);}return _0x4d7faf;}[_0x4be940(0xbf)](_0x19a9d8,_0x31ccf2){const _0x2c086a=_0x4be940;let _0x5c23e8=this[_0x2c086a(0xbc)][_0x19a9d8],_0x5e912b=_0x5c23e8[_0x2c086a(0xe3)](_0x31ccf2);return _0x5e912b;}[_0x4be940(0xd7)](_0x2e56b6){const _0x148c6a=_0x4be940;let _0x5f24bd=this['records'][_0x2e56b6],_0x32aae6=_0x5f24bd[_0x148c6a(0xcc)]();return _0x32aae6;}['get_row_by_value'](_0x5df469,_0x27cf4f){const _0x136840=_0x4be940;let _0x359df2=this[_0x136840(0x92)](_0x5df469,_0x27cf4f);if(_0x359df2!=-0x1){let _0x354e1b=this[_0x136840(0xbc)][_0x359df2];return _0x354e1b;}return null;}[_0x4be940(0x92)](_0x24278c,_0x13d39b){const _0x43dbb3=_0x4be940;let _0x2af55d=-0x1,_0x165fae=_0x13d39b;if(Array['isArray'](_0x165fae))_0x165fae=_0x165fae[_0x43dbb3(0xdb)](',');else typeof _0x165fae==='object'&&(_0x165fae=JSON[_0x43dbb3(0x9f)](_0x165fae));for(let _0x57b490=0x0;_0x57b490<this['records'][_0x43dbb3(0x9d)];_0x57b490++){let _0xbba5b1=this[_0x43dbb3(0xbc)][_0x57b490],_0x254171=_0xbba5b1[_0x43dbb3(0xe3)](_0x24278c);if(Array['isArray'](_0x254171))_0x254171=_0x254171[_0x43dbb3(0xdb)](',');else typeof _0x254171==='object'&&(_0x254171=JSON[_0x43dbb3(0x9f)](_0x254171));if(_0x254171==_0x165fae){_0x2af55d=_0x57b490;break;}}return _0x2af55d;}[_0x4be940(0xdc)](_0x213b3e,_0x23489e,_0x3a4a20,_0x193be3){const _0x29908d=_0x4be940;let _0x4abbfb={};for(let _0x3c5357=0x0;_0x3c5357<_0x3a4a20['length'];_0x3c5357++){let _0x5e4b48=_0x3a4a20[_0x3c5357]+'__'+_0x213b3e;_0x4abbfb[_0x5e4b48]=0x0;}for(let _0x4c5868=0x0;_0x4c5868<this[_0x29908d(0xbc)][_0x29908d(0x9d)];_0x4c5868++){let _0x2dac31=this[_0x29908d(0xbc)][_0x4c5868],_0x2a6215=_0x2dac31[_0x29908d(0xe3)](_0x193be3),_0x43bee4=_0x2dac31[_0x29908d(0xe3)]('__group_by_name'),_0x14d30b=_0x2a6215+'__'+_0x43bee4,_0x57f70e=_0x2dac31[_0x29908d(0xe3)](_0x23489e);_0x4abbfb[_0x14d30b]=_0x57f70e;}let _0x42d3ef=[];for(let _0x275e05=0x0;_0x275e05<_0x3a4a20[_0x29908d(0x9d)];_0x275e05++){let _0x4d65cc=_0x3a4a20[_0x275e05]+'__'+_0x213b3e,_0x6e3aa3=_0x4abbfb[_0x4d65cc];_0x42d3ef[_0x29908d(0xd2)](_0x6e3aa3);}return _0x42d3ef;}}return _0x55d6cc;}));function a0_0x190f(_0x406248,_0x452169){const _0x395963=a0_0x3959();return a0_0x190f=function(_0x190f9f,_0xfd4102){_0x190f9f=_0x190f9f-0x89;let _0x2c9acf=_0x395963[_0x190f9f];return _0x2c9acf;},a0_0x190f(_0x406248,_0x452169);}function a0_0x3959(){const _0x265c10=['get_dimensions','get_max_value','972165UNqyCC','is_custom','is_get_data_from_model','group_by','get_array_style_datas','length','is_category','stringify','raw_fields','_raw_field_cache','_init_raw_fields_cache','get_category_fields','5631jwvCqq','get_col_names','keys','field_name','is_valid','get_avg','order_by_infos','config','category','get_first_aggregate_column_value','get_data_source_type','get_aggregate_value','column_arggregation','format_name','get_field_names','has_domain_field','get_column_values','get_category_values','get_aggregate','get_first_group_by','get_min','4855390rELmGv','result_type','raw_datas','records','get_group_by_names','model_fields','get_col_value','datas','data_source_info','get_dimension_values','get_fields_info','get_record_by_col_value','has_multi_order_by','name','get_raw_datas','get_col_values','get_title','has_multi_group_by','domain','get_values','18DTAqhg','init_data_records','668112XviBog','uniq','measure','push','2813672YujiUj','index','get_raw_field','1362MtHYgW','get_row_values','get_record','get_records','field_type','join','get_group_by_name_values','get_aggregate_columns','group_by_infos','get_cols_values','get_unique_col_values','get_raw_fields','data_source_type_name','get_value','get_group_by_infos','isInteger','18scijqS','isArray','get_measures','data_source_type','_valid','indexOf','full_name','get_sum','114563wdorxz','get_row_index_by_value','get_domain','get_max','7237174ENXSPZ'];a0_0x3959=function(){return _0x265c10;};return a0_0x3959();}