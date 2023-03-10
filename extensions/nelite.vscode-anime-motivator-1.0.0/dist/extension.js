(()=>{"use strict";var t={686:(t,e)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.getNonce=void 0,e.getNonce=function(){let t="";const e="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";for(let i=0;i<32;i++)t+=e.charAt(Math.floor(Math.random()*e.length));return t}},69:(t,e,i)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.Motivator=void 0;const n=i(549);e.Motivator=class{constructor(t,e){this.lastHeartbeat=0,this.gifShown=!1,this.gifTimeout=setTimeout((function(){}),0),this.lastHeartbeat=Date.now(),this.setupEventListeners(),this.sidebar=t,this.webViewView=e}onEvent(){let t=n.window.activeTextEditor;if(t){let e=t.document;e&&e.fileName&&(console.log("Heartbeat updated."),this.lastHeartbeat=Date.now(),this.gifShown&&this.closeGif(),console.log("Gif delayed."),clearTimeout(this.gifTimeout),this.gifTimeout=setTimeout((()=>this.delayGif()),12500))}}setupEventListeners(){n.window.onDidChangeTextEditorSelection(this.onEvent,this),n.window.onDidChangeActiveTextEditor(this.onEvent,this),n.workspace.onDidSaveTextDocument(this.onEvent,this),n.window.onDidChangeTextEditorVisibleRanges(this.onEvent,this)}enoughTimePassed(t){return this.lastHeartbeat+11e3<t}closeGif(){this.gifShown=!1,this.webViewView.webview.html=this.sidebar.getEmptyHtml(this.webViewView.webview)}delayGif(){console.log("Gif delay ended."),this.enoughTimePassed(Date.now())&&!this.gifShown&&this.showGif()}showGif(){this.gifShown=!0,console.log("Gif show."),this.webViewView.webview.html=this.sidebar.getGifHtml(this.webViewView.webview)}delay(t){return new Promise((e=>setTimeout(e,t)))}}},922:(t,e,i)=>{Object.defineProperty(e,"__esModule",{value:!0}),e.SidebarProvider=void 0;const n=i(549),s=i(686),o=i(69);e.SidebarProvider=class{constructor(t){this._extensionUri=t}resolveWebviewView(t){this._view=t,t.webview.options={enableScripts:!0,localResourceRoots:[this._extensionUri]},t.webview.html=this.getEmptyHtml(t.webview),new o.Motivator(this,t)}revive(t){this._view=t}getGifHtml(t){const e=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"media","reset.css")),i=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"out","compiled/afk.js")),o=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"out","compiled/afk.css")),r=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"media","vscode.css")),a=s.getNonce();return`<!DOCTYPE html>\n\t\t\t<html lang="en">\n\t\t\t<head>\n\t\t\t\t<meta charset="UTF-8">\n\t\t\t\t\x3c!--\n\t\t\t\t\tUse a content security policy to only allow loading images from https or from our extension directory,\n\t\t\t\t\tand only allow scripts that have a specific nonce.\n        --\x3e\n        <meta http-equiv="Content-Security-Policy" content=" img-src https: data:; style-src 'unsafe-inline' ${t.cspSource}; script-src 'nonce-${a}';">\n\t\t\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t\t\t<link href="${e}" rel="stylesheet">\n\t\t\t\t<link href="${r}" rel="stylesheet">\n        <link href="${o}" rel="stylesheet">\n\t\t\t</head>\n      <body>\n\t\t\t\t<script nonce="${a}" src="${i}"><\/script>\n\t\t\t</body>\n\t\t\t</html>`}getEmptyHtml(t){const e=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"media","reset.css")),i=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"out","compiled/working.js")),o=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"out","compiled/working.css")),r=t.asWebviewUri(n.Uri.joinPath(this._extensionUri,"media","vscode.css")),a=s.getNonce();return`<!DOCTYPE html>\n\t\t\t<html lang="en">\n\t\t\t<head>\n\t\t\t\t<meta charset="UTF-8">\n\t\t\t\t\x3c!--\n\t\t\t\t\tUse a content security policy to only allow loading images from https or from our extension directory,\n\t\t\t\t\tand only allow scripts that have a specific nonce.\n        --\x3e\n        <meta http-equiv="Content-Security-Policy" content=" img-src https: data:; style-src 'unsafe-inline' ${t.cspSource}; script-src 'nonce-${a}';">\n\t\t\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t\t\t<link href="${e}" rel="stylesheet">\n\t\t\t\t<link href="${r}" rel="stylesheet">\n        <link href="${o}" rel="stylesheet">\n\t\t\t</head>\n      <body>\n\t\t\t\t<script nonce="${a}" src="${i}"><\/script>\n\t\t\t</body>\n\t\t\t</html>`}}},549:t=>{t.exports=require("vscode")}},e={};function i(n){var s=e[n];if(void 0!==s)return s.exports;var o=e[n]={exports:{}};return t[n](o,o.exports,i),o.exports}var n={};(()=>{var t=n;Object.defineProperty(t,"__esModule",{value:!0}),t.deactivate=t.activate=void 0;const e=i(549),s=i(922);t.activate=function(t){const i=new s.SidebarProvider(t.extensionUri);t.subscriptions.push(e.window.registerWebviewViewProvider("amotivator-sidebar",i))},t.deactivate=function(){}})(),module.exports=n})();