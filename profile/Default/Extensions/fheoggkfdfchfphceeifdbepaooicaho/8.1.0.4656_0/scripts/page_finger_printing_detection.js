/*!
 * 
 *     MCAFEE RESTRICTED CONFIDENTIAL
 *     Copyright (c) 2024 McAfee, LLC
 *
 *     The source code contained or described herein and all documents related
 *     to the source code ("Material") are owned by McAfee or its
 *     suppliers or licensors. Title to the Material remains with McAfee
 *     or its suppliers and licensors. The Material contains trade
 *     secrets and proprietary and confidential information of McAfee or its
 *     suppliers and licensors. The Material is protected by worldwide copyright
 *     and trade secret laws and treaty provisions. No part of the Material may
 *     be used, copied, reproduced, modified, published, uploaded, posted,
 *     transmitted, distributed, or disclosed in any way without McAfee's prior
 *     express written permission.
 *
 *     No license under any patent, copyright, trade secret or other intellectual
 *     property right is granted to or conferred upon you by disclosure or
 *     delivery of the Materials, either expressly, by implication, inducement,
 *     estoppel or otherwise. Any license under such intellectual property rights
 *     must be expressed and approved by McAfee in writing.
 *
 */(()=>{class a{static sendMessage(a){window.postMessage(a)}}(new class{updateInvoked(e){a.sendMessage({command:"FINGERPRINT_ATTEMPTED",invokedName:e})}updateObject({windoObj:a,param:e,val:t,name:o=null}){Object.defineProperty(a,e,{get:()=>(this.updateInvoked(o??e),t)})}setProxyData(){HTMLCanvasElement.prototype.toDataURL=new Proxy(HTMLCanvasElement.prototype.toDataURL,{apply:(a,e,t)=>(this.updateInvoked("toDataURL"),a.apply(e,t))}),HTMLCanvasElement.prototype.toBlob=new Proxy(HTMLCanvasElement.prototype.toBlob,{apply:(a,e,t)=>(this.updateInvoked("toBlob"),a.apply(e,t))});const a={apply:(a,e,t)=>(this.updateInvoked("webglBufferData"),a.apply(e,t))};WebGLRenderingContext.prototype.bufferData=new Proxy(WebGLRenderingContext.prototype.bufferData,a),WebGL2RenderingContext.prototype.bufferData=new Proxy(WebGL2RenderingContext.prototype.bufferData,a),navigator.geolocation.getCurrentPosition=new Proxy(navigator.geolocation.getCurrentPosition,{apply:(a,e,t)=>(this.updateInvoked("getCurrentPosition"),a.apply(e,t))}),toolbar=new Proxy(toolbar,{get(a,e){return this.updateInvoked("toolbar"),a[e]}}),statusbar=new Proxy(statusbar,{get(a,e){return this.updateInvoked("statusbar"),a[e]}}),personalbar=new Proxy(personalbar,{get(a,e){return this.updateInvoked("personalbar"),a[e]}}),menubar=new Proxy(menubar,{get(a,e){return this.updateInvoked("menubar"),a[e]}}),locationbar=new Proxy(locationbar,{get(a,e){return this.updateInvoked("locationbar"),a[e]}})}init(){const{hardwareConcurrency:a="",deviceMemory:e="",doNotTrack:t="",platform:o="",plugins:n=[],languages:r=""}=navigator,p=[{windoObj:navigator,param:"hardwareConcurrency",val:a},{windoObj:navigator,param:"deviceMemory",val:e},{windoObj:navigator,param:"doNotTrack",val:t},{windoObj:navigator,param:"platform",val:o}];navigator.languages.includes(";q")||p.push({windoObj:navigator,param:"languages",val:r}),n&&p.push({windoObj:navigator,param:"plugins",val:n}),p.forEach((a=>this.updateObject(a))),this.setProxyData()}}).init()})();
//# sourceMappingURL=../sourceMap/chrome/scripts/page_finger_printing_detection.js.map