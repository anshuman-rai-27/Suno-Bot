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
 */(()=>{"use strict";const t=0,e=0,n=1,o=2,r=3,c=4,a=1,i=2,s=3,d=4,l={BACKGROUND:"BACKGROUND",CONTENT:"CONTENT",TELEMETRY:"TELEMETRY"},m={DEFAULT:"color: #000000; font-weight: normal; font-style:normal; background: #FFFFFF;",BACKGROUND:"color: #8D0DBA; font-weight: bold; background: #FFFFFF;",CONTENT:"color: #F54A26; font-weight: bold; background: #FFFFFF;",TELEMETRY:"color: #147831; font-weight: bold; background: #FFFFFF;"};class u{static log(t,e=null){F(t,a,e)}static error(t,e=null){F(t,i,e)}static warn(t,e=null){F(t,s,e)}static debug(t,e=null){F(t,d,e)}}const F=(u,F,g)=>{const f=t;if(f===e)return;let E="chrome-extension:"===location.protocol?l.BACKGROUND:l.CONTENT;g&&l[g]&&(E=g);const w=new Date,h=F===i?u:`%c[${E} ${w.toLocaleString([],{hour:"2-digit",minute:"2-digit",hour12:!0})}]: %c${u}`,T=m.DEFAULT;let b=m[E];if(b||(b=T),f>=o&&F===i&&console.error(u),f>=n&&F===a&&console.log(h,b,T),f>=r&&F===s){const t="color: #FFA500; font-family: sans-serif; font-weight: bolder; text-shadow: #000 1px 1px;";console.log(`%cWARN - ${h}`,t,b,T)}if(f>=c&&F===d){const t="color: #FF33D7; font-family: sans-serif; font-weight: bolder; text-shadow: #000 1px 1px;";console.log(`%cDEBUG - ${h}`,t,b,T)}},g=async(t,e,n,o)=>{try{return await f(t,e,n,o),!0}catch(t){return u.warn(`[broadcast] Unexpected error when calling command: "${e}", err: ${t.message}`),null}},f=(t,e,n,o,r=null)=>{if(!chrome.tabs)throw new Error('"tabs" permission not set in manifest.');return chrome.tabs.sendMessage(o,{ipcId:t,command:e,...n},{frameId:r})},E=(t,e={},n)=>(async(t,e,n={},o={})=>{try{if(o?.tabId){const{tabId:r,frameId:c}=o;return await f(t,e,n,r,c)}if(o?.broadcast){const r=await chrome.tabs.query({}),{broadcastIgnoreId:c=[]}=o;return r.filter((({id:t})=>!c.includes(t))).forEach((({id:o})=>{g(t,e,n,o)})),!0}return await chrome.runtime.sendMessage({ipcId:t,command:e,...n})}catch(t){return u.warn(`Unexpected error when calling command: "${e}", err: ${t.message}`),null}})("WA",t,e,n);(new class{init(){var t;t=()=>{const t=chrome.runtime.getURL("scripts/page_finger_printing_detection.js"),e=document.createElement("script");e.src=t,e.id="WA_FP_SCAN_SCRIPT",e.type="text/javascript",document.body.appendChild(e),this.initEvents()},"undefined"!=typeof document&&null!==document&&("complete"===document.readyState||"loading"!==document.readyState&&!document.documentElement.doScroll?t():document.addEventListener("DOMContentLoaded",t))}initEvents(){window.addEventListener("message",(({source:t,data:e})=>{t===window&&e&&e.command&&"FINGERPRINT_ATTEMPTED"===e.command&&E(e.command,e)}))}}).init()})();
//# sourceMappingURL=../sourceMap/chrome/scripts/content_finger_printing_detection.js.map