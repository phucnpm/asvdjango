//>>built
define("dojox/mobile/compat",["dojo/_base/lang","dojo/_base/sniff"],function(_1,_2){
var dm=_1.getObject("dojox.mobile",true);
if(!_2("webkit")){
var s="dojox/mobile/_compat";
require([s]);
}
return dm;
});
