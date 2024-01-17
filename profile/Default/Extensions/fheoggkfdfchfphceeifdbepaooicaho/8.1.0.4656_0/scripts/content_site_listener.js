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
 */(()=>{"use strict";const e="FOCUS_OR_CREATE_TAB",n="SHOW_SIDEBAR_MAIN",t="PING_CONTENT_SITE_LISTENER",o=0,r=23,s=24,i=0,a=0,c=0,l=1,d=2,u=3,m=4,g=1,f=2,F=3,h=4,p={BACKGROUND:"BACKGROUND",CONTENT:"CONTENT",TELEMETRY:"TELEMETRY"},w={DEFAULT:"color: #000000; font-weight: normal; font-style:normal; background: #FFFFFF;",BACKGROUND:"color: #8D0DBA; font-weight: bold; background: #FFFFFF;",CONTENT:"color: #F54A26; font-weight: bold; background: #FFFFFF;",TELEMETRY:"color: #147831; font-weight: bold; background: #FFFFFF;"};class E{static log(e,n=null){b(e,g,n)}static error(e,n=null){b(e,f,n)}static warn(e,n=null){b(e,F,n)}static debug(e,n=null){b(e,h,n)}}const b=(e,n,t)=>{const o=a;if(o===c)return;let r="chrome-extension:"===location.protocol?p.BACKGROUND:p.CONTENT;t&&p[t]&&(r=t);const s=new Date,i=n===f?e:`%c[${r} ${s.toLocaleString([],{hour:"2-digit",minute:"2-digit",hour12:!0})}]: %c${e}`,E=w.DEFAULT;let b=w[r];if(b||(b=E),o>=d&&n===f&&console.error(e),o>=l&&n===g&&console.log(i,b,E),o>=u&&n===F){const e="color: #FFA500; font-family: sans-serif; font-weight: bolder; text-shadow: #000 1px 1px;";console.log(`%cWARN - ${i}`,e,b,E)}if(o>=m&&n===h){const e="color: #FF33D7; font-family: sans-serif; font-weight: bolder; text-shadow: #000 1px 1px;";console.log(`%cDEBUG - ${i}`,e,b,E)}};class T{constructor(e){this.pingCommand=e,this.basePingListener()}basePingListener(e=null){((e,n=null,t)=>{"function"==typeof t?chrome.runtime.onMessage.addListener(((o,r,s)=>{if(r.id===chrome.runtime.id&&"object"==typeof o&&!Array.isArray(o)&&o?.ipcId===e)return t({promises:n,request:o,sender:r,sendResponse:s})})):E.error("Provided with invalid callback function")})("WA",null,(({request:n,sendResponse:t})=>{const{command:o}=n;if(o===this.pingCommand)return E.debug(`File Injection [pinged]: Received ${o} command`),t({content:!0}),"function"==typeof e&&e(),!0}))}}const A=async(e,n,t,o)=>{try{return await N(e,n,t,o),!0}catch(e){return E.warn(`[broadcast] Unexpected error when calling command: "${n}", err: ${e.message}`),null}},N=(e,n,t,o,r=null)=>{if(!chrome.tabs)throw new Error('"tabs" permission not set in manifest.');return chrome.tabs.sendMessage(o,{ipcId:e,command:n,...t},{frameId:r})},y=(e,n={},t)=>(async(e,n,t={},o={})=>{try{if(o?.tabId){const{tabId:r,frameId:s}=o;return await N(e,n,t,r,s)}if(o?.broadcast){const r=await chrome.tabs.query({}),{broadcastIgnoreId:s=[]}=o;return r.filter((({id:e})=>!s.includes(e))).forEach((({id:o})=>{A(e,n,t,o)})),!0}return await chrome.runtime.sendMessage({ipcId:e,command:n,...t})}catch(e){return E.warn(`Unexpected error when calling command: "${n}", err: ${e.message}`),null}})("WA",e,n,t);(new class extends T{constructor(){super(t)}main(){window.addEventListener("message",(t=>{if(!t)return;const{data:a}=t;if(!a)return;const{request_type:c,payload:l}=a;if(void 0!==c&&void 0!==l){if(c!==o||l.done||window.postMessage({request_type:i,payload:{done:!0}},t.origin),c===r){const n=chrome.runtime.getURL("html/settings.html");y(e,{url:n})}c===s&&y(n)}}),!1)}}).main()})();
//# sourceMappingURL=../sourceMap/chrome/scripts/content_site_listener.js.map