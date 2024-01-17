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
 */(()=>{"use strict";let t="";const e="d7a06d5a-923f-49a1-a344-9ef28dcdfd21";class s{static sendMessage(s){s.guid=`${t}_${e}`,window.postMessage(s)}static init(){const s=document.getElementById(`SCRIPT_${e}`);return t=s.getAttribute("randuuid"),void 0!==t}}const n=1,o=2;class i{static updateInvoked(t,e){s.sendMessage({command:"MESSAGE_HTTP_REQ",payload:{url:t,type:e}})}init(){const t=XMLHttpRequest.prototype.open,e=XMLHttpRequest.prototype.send,s=window.fetch,a=new Map;XMLHttpRequest.prototype.open=function(e,s){if(s.startsWith("https://")||s.startsWith("http://"))a.set(this,s);else try{const t=new URL(document.location.href);t.protocol&&t.hostname&&a.set(this,`https://${t.hostname}${s}`)}catch(t){}return t.apply(this,[e,s])},XMLHttpRequest.prototype.send=function(t){const s=a.get(this);return s&&(i.updateInvoked(s,n),a.delete(this)),e.apply(this,[t])},window.fetch=function(t,e){const n=t.url?t.url:t.toString();if(n.startsWith("https://")||n.startsWith("http://"))i.updateInvoked(n,o);else try{const t=new URL(document.location.href);t.protocol&&t.hostname&&i.updateInvoked(`https://${t.hostname}${n}`,o)}catch(t){}return s.apply(this,[t,e])}}}s.init();(new i).init();(new class{init(){setInterval((()=>{const t=[],e=document.getElementsByTagName("script");if(e&&e.length>0){for(let s=0;s<e.length;++s){const n=e.item(s);!n.getAttribute("MC_PROCESSED")&&n.src&&(t.push(n.src),n.setAttribute("MC_PROCESSED","1"))}if(t.length>0){const e={command:"MESSAGE_ALL_LINKS",payload:{links:t}};s.sendMessage(e)}}}),5e3)}}).init()})();
//# sourceMappingURL=../sourceMap/chrome/scripts/page_crypto_mining.js.map