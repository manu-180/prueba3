(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[391],{2546:function(e,t,n){"use strict";n.d(t,{Z:function(){return o}});var r=n(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,r.Z)("AlignJustify",[["line",{x1:"3",x2:"21",y1:"6",y2:"6",key:"4m8b97"}],["line",{x1:"3",x2:"21",y1:"12",y2:"12",key:"10d38w"}],["line",{x1:"3",x2:"21",y1:"18",y2:"18",key:"kwyyxn"}]])},8971:function(e,t,n){"use strict";n.d(t,{Z:function(){return o}});var r=n(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,r.Z)("ChevronDown",[["path",{d:"m6 9 6 6 6-6",key:"qrunsl"}]])},116:function(e,t,n){"use strict";n.d(t,{Z:function(){return o}});var r=n(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,r.Z)("TriangleAlert",[["path",{d:"m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3",key:"wmoenq"}],["path",{d:"M12 9v4",key:"juzpu7"}],["path",{d:"M12 17h.01",key:"p32p05"}]])},7498:function(e,t){"use strict";var n,r;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var n in t)Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}(t,{PrefetchKind:function(){return n},ACTION_REFRESH:function(){return o},ACTION_NAVIGATE:function(){return i},ACTION_RESTORE:function(){return l},ACTION_SERVER_PATCH:function(){return a},ACTION_PREFETCH:function(){return u},ACTION_FAST_REFRESH:function(){return s},ACTION_SERVER_ACTION:function(){return c}});let o="refresh",i="navigate",l="restore",a="server-patch",u="prefetch",s="fast-refresh",c="server-action";(r=n||(n={})).AUTO="auto",r.FULL="full",r.TEMPORARY="temporary",("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},30:function(e,t,n){"use strict";function getDomainLocale(e,t,n,r){return!1}Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"getDomainLocale",{enumerable:!0,get:function(){return getDomainLocale}}),n(2866),("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},5170:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return w}});let r=n(8754),o=r._(n(7294)),i=n(4450),l=n(2227),a=n(4364),u=n(109),s=n(3607),c=n(1823),d=n(9031),f=n(920),p=n(30),m=n(7192),h=n(7498),g=new Set;function prefetch(e,t,n,r,o,i){if(!i&&!(0,l.isLocalURL)(t))return;if(!r.bypassPrefetchedCheck){let o=void 0!==r.locale?r.locale:"locale"in e?e.locale:void 0,i=t+"%"+n+"%"+o;if(g.has(i))return;g.add(i)}let a=i?e.prefetch(t,o):e.prefetch(t,n,r);Promise.resolve(a).catch(e=>{})}function isModifiedEvent(e){let t=e.currentTarget,n=t.getAttribute("target");return n&&"_self"!==n||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}function linkClicked(e,t,n,r,i,a,u,s,c,d){let{nodeName:f}=e.currentTarget,p="A"===f.toUpperCase();if(p&&(isModifiedEvent(e)||!c&&!(0,l.isLocalURL)(n)))return;e.preventDefault();let navigate=()=>{let e=null==u||u;"beforePopState"in t?t[i?"replace":"push"](n,r,{shallow:a,locale:s,scroll:e}):t[i?"replace":"push"](r||n,{forceOptimisticNavigation:!d,scroll:e})};c?o.default.startTransition(navigate):navigate()}function formatStringOrUrl(e){return"string"==typeof e?e:(0,a.formatUrl)(e)}let v=o.default.forwardRef(function(e,t){let n,r;let{href:l,as:a,children:g,prefetch:v=null,passHref:w,replace:b,shallow:y,scroll:E,locale:R,onClick:C,onMouseEnter:x,onTouchStart:S,legacyBehavior:D=!1,...T}=e;n=g,D&&("string"==typeof n||"number"==typeof n)&&(n=o.default.createElement("a",null,n));let P=o.default.useContext(c.RouterContext),O=o.default.useContext(d.AppRouterContext),$=null!=P?P:O,A=!P,M=!1!==v,I=null===v?h.PrefetchKind.AUTO:h.PrefetchKind.FULL,{href:k,as:N}=o.default.useMemo(()=>{if(!P){let e=formatStringOrUrl(l);return{href:e,as:a?formatStringOrUrl(a):e}}let[e,t]=(0,i.resolveHref)(P,l,!0);return{href:e,as:a?(0,i.resolveHref)(P,a):t||e}},[P,l,a]),_=o.default.useRef(k),j=o.default.useRef(N);D&&(r=o.default.Children.only(n));let V=D?r&&"object"==typeof r&&r.ref:t,[L,U,B]=(0,f.useIntersection)({rootMargin:"200px"}),H=o.default.useCallback(e=>{(j.current!==N||_.current!==k)&&(B(),j.current=N,_.current=k),L(e),V&&("function"==typeof V?V(e):"object"==typeof V&&(V.current=e))},[N,V,k,B,L]);o.default.useEffect(()=>{$&&U&&M&&prefetch($,k,N,{locale:R},{kind:I},A)},[N,k,U,R,M,null==P?void 0:P.locale,$,A,I]);let z={ref:H,onClick(e){D||"function"!=typeof C||C(e),D&&r.props&&"function"==typeof r.props.onClick&&r.props.onClick(e),$&&!e.defaultPrevented&&linkClicked(e,$,k,N,b,y,E,R,A,M)},onMouseEnter(e){D||"function"!=typeof x||x(e),D&&r.props&&"function"==typeof r.props.onMouseEnter&&r.props.onMouseEnter(e),$&&(M||!A)&&prefetch($,k,N,{locale:R,priority:!0,bypassPrefetchedCheck:!0},{kind:I},A)},onTouchStart(e){D||"function"!=typeof S||S(e),D&&r.props&&"function"==typeof r.props.onTouchStart&&r.props.onTouchStart(e),$&&(M||!A)&&prefetch($,k,N,{locale:R,priority:!0,bypassPrefetchedCheck:!0},{kind:I},A)}};if((0,u.isAbsoluteUrl)(N))z.href=N;else if(!D||w||"a"===r.type&&!("href"in r.props)){let e=void 0!==R?R:null==P?void 0:P.locale,t=(null==P?void 0:P.isLocaleDomain)&&(0,p.getDomainLocale)(N,e,null==P?void 0:P.locales,null==P?void 0:P.domainLocales);z.href=t||(0,m.addBasePath)((0,s.addLocale)(N,e,null==P?void 0:P.defaultLocale))}return D?o.default.cloneElement(r,z):o.default.createElement("a",{...T,...z},n)}),w=v;("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},920:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useIntersection",{enumerable:!0,get:function(){return useIntersection}});let r=n(7294),o=n(3436),i="function"==typeof IntersectionObserver,l=new Map,a=[];function createObserver(e){let t;let n={root:e.root||null,margin:e.rootMargin||""},r=a.find(e=>e.root===n.root&&e.margin===n.margin);if(r&&(t=l.get(r)))return t;let o=new Map,i=new IntersectionObserver(e=>{e.forEach(e=>{let t=o.get(e.target),n=e.isIntersecting||e.intersectionRatio>0;t&&n&&t(n)})},e);return t={id:n,observer:i,elements:o},a.push(n),l.set(n,t),t}function observe(e,t,n){let{id:r,observer:o,elements:i}=createObserver(n);return i.set(e,t),o.observe(e),function(){if(i.delete(e),o.unobserve(e),0===i.size){o.disconnect(),l.delete(r);let e=a.findIndex(e=>e.root===r.root&&e.margin===r.margin);e>-1&&a.splice(e,1)}}}function useIntersection(e){let{rootRef:t,rootMargin:n,disabled:l}=e,a=l||!i,[u,s]=(0,r.useState)(!1),c=(0,r.useRef)(null),d=(0,r.useCallback)(e=>{c.current=e},[]);(0,r.useEffect)(()=>{if(i){if(a||u)return;let e=c.current;if(e&&e.tagName){let r=observe(e,e=>e&&s(e),{root:null==t?void 0:t.current,rootMargin:n});return r}}else if(!u){let e=(0,o.requestIdleCallback)(()=>s(!0));return()=>(0,o.cancelIdleCallback)(e)}},[a,n,t,u,c.current]);let f=(0,r.useCallback)(()=>{s(!1)},[]);return[d,u,f]}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},1664:function(e,t,n){e.exports=n(5170)},7630:function(e,t,n){"use strict";n.d(t,{SV:function(){return ErrorBoundary}});var r=n(7294);let o=(0,r.createContext)(null),i={didCatch:!1,error:null};let ErrorBoundary=class ErrorBoundary extends r.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=i}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,n,r=arguments.length,o=Array(r),l=0;l<r;l++)o[l]=arguments[l];null===(t=(n=this.props).onReset)||void 0===t||t.call(n,{args:o,reason:"imperative-api"}),this.setState(i)}}componentDidCatch(e,t){var n,r;null===(n=(r=this.props).onError)||void 0===n||n.call(r,e,t)}componentDidUpdate(e,t){let{didCatch:n}=this.state,{resetKeys:r}=this.props;if(n&&null!==t.error&&hasArrayChanged(e.resetKeys,r)){var o,l;null===(o=(l=this.props).onReset)||void 0===o||o.call(l,{next:r,prev:e.resetKeys,reason:"keys"}),this.setState(i)}}render(){let{children:e,fallbackRender:t,FallbackComponent:n,fallback:i}=this.props,{didCatch:l,error:a}=this.state,u=e;if(l){let e={error:a,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)u=t(e);else if(n)u=(0,r.createElement)(n,e);else if(null===i||(0,r.isValidElement)(i))u=i;else throw a}return(0,r.createElement)(o.Provider,{value:{didCatch:l,error:a,resetErrorBoundary:this.resetErrorBoundary}},u)}};function hasArrayChanged(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,n)=>!Object.is(e,t[n]))}},3916:function(e,t,n){"use strict";n.d(t,{M:function(){return c}});var r=n(5059),o=n(296),i=n(5893),l=(0,r.G)(function(e,t){let{templateAreas:n,gap:r,rowGap:l,columnGap:a,column:u,row:s,autoFlow:c,autoRows:d,templateRows:f,autoColumns:p,templateColumns:m,...h}=e;return(0,i.jsx)(o.m.div,{ref:t,__css:{display:"grid",gridTemplateAreas:n,gridGap:r,gridRowGap:l,gridColumnGap:a,gridAutoColumns:p,gridColumn:u,gridRow:s,gridAutoFlow:c,gridAutoRows:d,gridTemplateRows:f,gridTemplateColumns:m},...h})});l.displayName="Grid";var a=n(7323),u=n(4629),s=n(5432);function mapResponsive(e,t){return Array.isArray(e)?e.map(e=>null===e?null:t(e)):(0,s.Kn)(e)?Object.keys(e).reduce((n,r)=>(n[r]=t(e[r]),n),{}):null!=e?t(e):null}Object.freeze(["base","sm","md","lg","xl","2xl"]);var c=(0,r.G)(function(e,t){let{columns:n,spacingX:r,spacingY:o,spacing:u,minChildWidth:s,...c}=e,d=(0,a.F)(),f=s?widthToColumns(s,d):countToColumns(n);return(0,i.jsx)(l,{ref:t,gap:u,columnGap:r,rowGap:o,templateColumns:f,...c})});function toPx(e){return"number"==typeof e?`${e}px`:e}function widthToColumns(e,t){return mapResponsive(e,e=>{let n=(0,u.LP)("sizes",e,toPx(e))(t);return null===e?null:`repeat(auto-fit, minmax(${n}, 1fr))`})}function countToColumns(e){return mapResponsive(e,e=>null===e?null:`repeat(${e}, minmax(0, 1fr))`)}c.displayName="SimpleGrid"},3798:function(e,t,n){"use strict";let r;n.d(t,{d:function(){return w}});var o=n(7494),i=n(7294);function __insertCSS(e){if(!e||"undefined"==typeof document)return;let t=document.head||document.getElementsByTagName("head")[0],n=document.createElement("style");n.type="text/css",t.appendChild(n),n.styleSheet?n.styleSheet.cssText=e:n.appendChild(document.createTextNode(e))}let l=i.createContext({drawerRef:{current:null},overlayRef:{current:null},scaleBackground:()=>{},onPress:()=>{},onRelease:()=>{},onDrag:()=>{},onNestedDrag:()=>{},onNestedOpenChange:()=>{},onNestedRelease:()=>{},openProp:void 0,dismissible:!1,handleOnly:!1,isOpen:!1,isDragging:!1,keyboardIsOpen:{current:!1},snapPointsOffset:null,snapPoints:null,modal:!1,shouldFade:!1,activeSnapPoint:null,onOpenChange:()=>{},setActiveSnapPoint:()=>{},visible:!1,closeDrawer:()=>{},setVisible:()=>{},direction:"bottom"}),useDrawerContext=()=>{let e=i.useContext(l);if(!e)throw Error("useDrawerContext must be used within a Drawer.Root");return e};__insertCSS("[vaul-drawer]{touch-action:none;will-change:transform;transition:transform .5s cubic-bezier(.32, .72, 0, 1)}[vaul-drawer][vaul-drawer-direction=bottom]{transform:translate3d(0,100%,0)}[vaul-drawer][vaul-drawer-direction=top]{transform:translate3d(0,-100%,0)}[vaul-drawer][vaul-drawer-direction=left]{transform:translate3d(-100%,0,0)}[vaul-drawer][vaul-drawer-direction=right]{transform:translate3d(100%,0,0)}.vaul-dragging .vaul-scrollable [vault-drawer-direction=top]{overflow-y:hidden!important}.vaul-dragging .vaul-scrollable [vault-drawer-direction=bottom]{overflow-y:hidden!important}.vaul-dragging .vaul-scrollable [vault-drawer-direction=left]{overflow-x:hidden!important}.vaul-dragging .vaul-scrollable [vault-drawer-direction=right]{overflow-x:hidden!important}[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=top]{transform:translate3d(0,var(--snap-point-height,0),0)}[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=bottom]{transform:translate3d(0,var(--snap-point-height,0),0)}[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=left]{transform:translate3d(var(--snap-point-height,0),0,0)}[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=right]{transform:translate3d(var(--snap-point-height,0),0,0)}[vaul-overlay]{opacity:0;transition:opacity .5s cubic-bezier(.32, .72, 0, 1)}[vaul-overlay][vaul-drawer-visible=true]{opacity:1}[vaul-drawer]::after{content:'';position:absolute;background:inherit;background-color:inherit}[vaul-drawer][vaul-drawer-direction=top]::after{top:initial;bottom:100%;left:0;right:0;height:200%}[vaul-drawer][vaul-drawer-direction=bottom]::after{top:100%;bottom:initial;left:0;right:0;height:200%}[vaul-drawer][vaul-drawer-direction=left]::after{left:initial;right:100%;top:0;bottom:0;width:200%}[vaul-drawer][vaul-drawer-direction=right]::after{left:100%;right:initial;top:0;bottom:0;width:200%}[vaul-handle]{display:block;position:relative;opacity:.8;margin-left:auto;margin-right:auto;height:5px;width:56px;border-radius:1rem;touch-action:pan-y;cursor:grab}[vaul-handle]:active,[vaul-handle]:hover{opacity:1}[vaul-handle]:active{cursor:grabbing}[vaul-handle-hitarea]{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:max(100%,2.75rem);height:max(100%,2.75rem);touch-action:inherit}[vaul-overlay][vaul-snap-points=true]:not([vaul-snap-points-overlay=true]):not([data-state=closed]){opacity:0}[vaul-overlay][vaul-snap-points-overlay=true]:not([vaul-drawer-visible=false]){opacity:1}@media (hover:hover) and (pointer:fine){[vaul-drawer]{user-select:none}}@media (pointer:fine){[vaul-handle-hitarea]:{width:100%;height:100%}}");let a="undefined"!=typeof window?i.useLayoutEffect:i.useEffect;function chain(...e){return(...t)=>{for(let n of e)"function"==typeof n&&n(...t)}}function isMac(){return testPlatform(/^Mac/)}function isIPhone(){return testPlatform(/^iPhone/)}function isIPad(){return testPlatform(/^iPad/)||isMac()&&navigator.maxTouchPoints>1}function testPlatform(e){return"undefined"!=typeof window&&null!=window.navigator?e.test(window.navigator.platform):void 0}let u="undefined"!=typeof document&&window.visualViewport;function isScrollable(e){let t=window.getComputedStyle(e);return/(auto|scroll)/.test(t.overflow+t.overflowX+t.overflowY)}function getScrollParent(e){for(isScrollable(e)&&(e=e.parentElement);e&&!isScrollable(e);)e=e.parentElement;return e||document.scrollingElement||document.documentElement}let s=new Set(["checkbox","radio","range","color","file","image","button","submit","reset"]),c=0;function usePreventScroll(e={}){let{isDisabled:t}=e;a(()=>{if(!t)return 1==++c&&(r=isIPhone()||isIPad()?preventScrollMobileSafari():preventScrollStandard()),()=>{0==--c&&r()}},[t])}function preventScrollStandard(){return chain(setStyle(document.documentElement,"paddingRight",`${window.innerWidth-document.documentElement.clientWidth}px`))}function preventScrollMobileSafari(){let e;let t=0,n=window.pageXOffset,r=window.pageYOffset,o=chain(setStyle(document.documentElement,"paddingRight",`${window.innerWidth-document.documentElement.clientWidth}px`));window.scrollTo(0,0);let i=chain(addEvent(document,"touchstart",n=>{((e=getScrollParent(n.target))!==document.documentElement||e!==document.body)&&(t=n.changedTouches[0].pageY)},{passive:!1,capture:!0}),addEvent(document,"touchmove",n=>{if(!e||e===document.documentElement||e===document.body){n.preventDefault();return}let r=n.changedTouches[0].pageY,o=e.scrollTop,i=e.scrollHeight-e.clientHeight;0!==i&&((o<=0&&r>t||o>=i&&r<t)&&n.preventDefault(),t=r)},{passive:!1,capture:!0}),addEvent(document,"touchend",e=>{let t=e.target;isInput(t)&&t!==document.activeElement&&(e.preventDefault(),t.style.transform="translateY(-2000px)",t.focus(),requestAnimationFrame(()=>{t.style.transform=""}))},{passive:!1,capture:!0}),addEvent(document,"focus",e=>{let t=e.target;isInput(t)&&(t.style.transform="translateY(-2000px)",requestAnimationFrame(()=>{t.style.transform="",u&&(u.height<window.innerHeight?requestAnimationFrame(()=>{scrollIntoView(t)}):u.addEventListener("resize",()=>scrollIntoView(t),{once:!0}))}))},!0),addEvent(window,"scroll",()=>{window.scrollTo(0,0)}));return()=>{o(),i(),window.scrollTo(n,r)}}function setStyle(e,t,n){let r=e.style[t];return e.style[t]=n,()=>{e.style[t]=r}}function addEvent(e,t,n,r){return e.addEventListener(t,n,r),()=>{e.removeEventListener(t,n,r)}}function scrollIntoView(e){let t=document.scrollingElement||document.documentElement;for(;e&&e!==t;){let t=getScrollParent(e);if(t!==document.documentElement&&t!==document.body&&t!==e){let n=t.getBoundingClientRect().top,r=e.getBoundingClientRect().top,o=e.getBoundingClientRect().bottom,i=t.getBoundingClientRect().bottom;o>i&&(t.scrollTop+=r-n)}e=t.parentElement}}function isInput(e){return e instanceof HTMLInputElement&&!s.has(e.type)||e instanceof HTMLTextAreaElement||e instanceof HTMLElement&&e.isContentEditable}function setRef(e,t){"function"==typeof e?e(t):null!=e&&(e.current=t)}function composeRefs(...e){return t=>e.forEach(e=>setRef(e,t))}function useComposedRefs(...e){return i.useCallback(composeRefs(...e),e)}let d=null;function usePositionFixed({isOpen:e,modal:t,nested:n,hasBeenOpened:r,preventScrollRestoration:o,noBodyStyles:l}){let[a,u]=i.useState(()=>"undefined"!=typeof window?window.location.href:""),s=i.useRef(0),c=i.useCallback(()=>{if(null===d&&e&&!l){d={position:document.body.style.position,top:document.body.style.top,left:document.body.style.left,height:document.body.style.height,right:"unset"};let{scrollX:e,innerHeight:t}=window;document.body.style.setProperty("position","fixed","important"),Object.assign(document.body.style,{top:`${-s.current}px`,left:`${-e}px`,right:"0px",height:"auto"}),window.setTimeout(()=>window.requestAnimationFrame(()=>{let e=t-window.innerHeight;e&&s.current>=t&&(document.body.style.top=`${-(s.current+e)}px`)}),300)}},[e]),f=i.useCallback(()=>{if(null!==d&&!l){let e=-parseInt(document.body.style.top,10),t=-parseInt(document.body.style.left,10);Object.assign(document.body.style,d),window.requestAnimationFrame(()=>{if(o&&a!==window.location.href){u(window.location.href);return}window.scrollTo(t,e)}),d=null}},[a]);return i.useEffect(()=>{function onScroll(){s.current=window.scrollY}return onScroll(),window.addEventListener("scroll",onScroll),()=>{window.removeEventListener("scroll",onScroll)}},[]),i.useEffect(()=>{if(!n&&r){if(e){let e=window.matchMedia("(display-mode: standalone)").matches;e||c(),t||window.setTimeout(()=>{f()},500)}else f()}},[e,r,a,t,n,c,f]),{restorePositionSetting:f}}let f=new WeakMap;function set(e,t,n=!1){if(!e||!(e instanceof HTMLElement))return;let r={};Object.entries(t).forEach(([t,n])=>{if(t.startsWith("--")){e.style.setProperty(t,n);return}r[t]=e.style[t],e.style[t]=n}),n||f.set(e,r)}function reset(e,t){if(!e||!(e instanceof HTMLElement))return;let n=f.get(e);n&&(t?e.style[t]=n[t]:Object.entries(n).forEach(([t,n])=>{e.style[t]=n}))}let isVertical=e=>{switch(e){case"top":case"bottom":return!0;case"left":case"right":return!1;default:return e}};function getTranslate(e,t){if(!e)return null;let n=window.getComputedStyle(e),r=n.transform||n.webkitTransform||n.mozTransform,o=r.match(/^matrix3d\((.+)\)$/);return o?parseFloat(o[1].split(", ")[isVertical(t)?13:12]):(o=r.match(/^matrix\((.+)\)$/))?parseFloat(o[1].split(", ")[isVertical(t)?5:4]):null}function dampenValue(e){return 8*(Math.log(e+1)-2)}let p={DURATION:.5,EASE:[.32,.72,0,1]};function useCallbackRef(e){let t=i.useRef(e);return i.useEffect(()=>{t.current=e}),i.useMemo(()=>(...e)=>null==t.current?void 0:t.current.call(t,...e),[])}function useUncontrolledState({defaultProp:e,onChange:t}){let n=i.useState(e),[r]=n,o=i.useRef(r),l=useCallbackRef(t);return i.useEffect(()=>{o.current!==r&&(l(r),o.current=r)},[r,o,l]),n}function useControllableState({prop:e,defaultProp:t,onChange:n=()=>{}}){let[r,o]=useUncontrolledState({defaultProp:t,onChange:n}),l=void 0!==e,a=l?e:r,u=useCallbackRef(n),s=i.useCallback(t=>{if(l){let n="function"==typeof t?t(e):t;n!==e&&u(n)}else o(t)},[l,e,o,u]);return[a,s]}function useSnapPoints({activeSnapPointProp:e,setActiveSnapPointProp:t,snapPoints:n,drawerRef:r,overlayRef:o,fadeFromIndex:l,onSnapPointChange:a,direction:u="bottom"}){let[s,c]=useControllableState({prop:e,defaultProp:null==n?void 0:n[0],onChange:t}),d=i.useMemo(()=>s===(null==n?void 0:n[n.length-1])||null,[n,s]),f=n&&n.length>0&&(l||0===l)&&!Number.isNaN(l)&&n[l]===s||!n,m=i.useMemo(()=>null==n?void 0:n.findIndex(e=>e===s),[n,s]),h=i.useMemo(()=>{var e;return null!=(e=null==n?void 0:n.map(e=>{let t="undefined"!=typeof window,n="string"==typeof e,r=0;if(n&&(r=parseInt(e,10)),isVertical(u)){let o=n?r:t?e*window.innerHeight:0;return t?"bottom"===u?window.innerHeight-o:-window.innerHeight+o:o}let o=n?r:t?e*window.innerWidth:0;return t?"right"===u?window.innerWidth-o:-window.innerWidth+o:o}))?e:[]},[n]),g=i.useMemo(()=>null!==m?null==h?void 0:h[m]:null,[h,m]),v=i.useCallback(e=>{var t;let i=null!=(t=null==h?void 0:h.findIndex(t=>t===e))?t:null;a(i),set(r.current,{transition:`transform ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`,transform:isVertical(u)?`translate3d(0, ${e}px, 0)`:`translate3d(${e}px, 0, 0)`}),h&&i!==h.length-1&&i!==l?set(o.current,{transition:`opacity ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`,opacity:"0"}):set(o.current,{transition:`opacity ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`,opacity:"1"}),c(null!==i?null==n?void 0:n[i]:null)},[r.current,n,h,l,o,c]);function onRelease({draggedDistance:e,closeDrawer:t,velocity:r,dismissible:i}){if(void 0===l)return;let a="bottom"===u||"right"===u?(null!=g?g:0)-e:(null!=g?g:0)+e,s=m===l-1,c=0===m,f=e>0;if(s&&set(o.current,{transition:`opacity ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`}),r>2&&!f){i?t():v(h[0]);return}if(r>2&&f&&h&&n){v(h[n.length-1]);return}let w=null==h?void 0:h.reduce((e,t)=>"number"!=typeof e||"number"!=typeof t?e:Math.abs(t-a)<Math.abs(e-a)?t:e),b=isVertical(u)?window.innerHeight:window.innerWidth;if(r>.4&&Math.abs(e)<.4*b){let e=f?1:-1;if(e>0&&d){v(h[n.length-1]);return}if(c&&e<0&&i&&t(),null===m)return;v(h[m+e]);return}v(w)}function getPercentageDragged(e,t){if(!n||"number"!=typeof m||!h||void 0===l)return null;let r=m===l-1,o=m>=l;if(o&&t)return 0;if(r&&!t)return 1;if(!f&&!r)return null;let i=r?m+1:m-1,a=r?h[i]-h[i-1]:h[i+1]-h[i],u=e/Math.abs(a);return r?1-u:u}return i.useEffect(()=>{if(s||e){var t;let r=null!=(t=null==n?void 0:n.findIndex(t=>t===e||t===s))?t:-1;h&&-1!==r&&"number"==typeof h[r]&&v(h[r])}},[s,e,n,h,v]),{isLastSnapPoint:d,activeSnapPoint:s,shouldFade:f,getPercentageDragged,setActiveSnapPoint:c,activeSnapPointIndex:m,onRelease,onDrag:function({draggedDistance:e}){if(null===g)return;let t="bottom"===u||"right"===u?g-e:g+e;("bottom"===u||"right"===u)&&t<h[h.length-1]||("top"===u||"left"===u)&&t>h[h.length-1]||set(r.current,{transform:isVertical(u)?`translate3d(0, ${t}px, 0)`:`translate3d(${t}px, 0, 0)`})},snapPointsOffset:h}}let m="vaul-dragging";function Root({open:e,onOpenChange:t,children:n,shouldScaleBackground:r,onDrag:a,onRelease:u,snapPoints:s,nested:c=!1,setBackgroundColorOnScale:d=!0,closeThreshold:f=.25,scrollLockTimeout:h=100,dismissible:g=!0,handleOnly:v=!1,fadeFromIndex:w=s&&s.length-1,activeSnapPoint:b,setActiveSnapPoint:y,fixed:E,modal:R=!0,onClose:C,noBodyStyles:x,direction:S="bottom",preventScrollRestoration:D=!0,disablePreventScroll:T=!1}){var P;let[O=!1,$]=i.useState(!1),[A,M]=i.useState(!1),[I,k]=i.useState(!1),[N,_]=i.useState(!1),[j,V]=i.useState(!1),[L,U]=i.useState(!1),B=i.useRef(null),H=i.useRef(null),z=i.useRef(null),F=i.useRef(null),W=i.useRef(null),Y=i.useRef(!1),q=i.useRef(null),K=i.useRef(0),G=i.useRef(!1),X=i.useRef(0),Z=i.useRef(null),J=i.useRef((null==(P=Z.current)?void 0:P.getBoundingClientRect().height)||0),Q=i.useRef(0),ee=i.useCallback(e=>{s&&e===ei.length-1&&(H.current=new Date)},[]),{activeSnapPoint:et,activeSnapPointIndex:en,setActiveSnapPoint:er,onRelease:eo,snapPointsOffset:ei,onDrag:el,shouldFade:ea,getPercentageDragged:eu}=useSnapPoints({snapPoints:s,activeSnapPointProp:b,setActiveSnapPointProp:y,drawerRef:Z,fadeFromIndex:w,overlayRef:B,onSnapPointChange:ee,direction:S});usePreventScroll({isDisabled:!O||j||!R||L||!A||T});let{restorePositionSetting:es}=usePositionFixed({isOpen:O,modal:R,nested:c,hasBeenOpened:A,preventScrollRestoration:D,noBodyStyles:x});function getScale(){return(window.innerWidth-26)/window.innerWidth}function onPress(e){var t;(g||s)&&(!Z.current||Z.current.contains(e.target))&&(J.current=(null==(t=Z.current)?void 0:t.getBoundingClientRect().height)||0,V(!0),z.current=new Date,(isIPhone()||isIPad())&&window.addEventListener("touchend",()=>Y.current=!1,{once:!0}),e.target.setPointerCapture(e.pointerId),K.current=isVertical(S)?e.clientY:e.clientX)}function shouldDrag(e,t){var n;let r=e,o=null==(n=window.getSelection())?void 0:n.toString(),i=Z.current?getTranslate(Z.current,S):null,l=new Date;if(r.hasAttribute("data-vaul-no-drag")||r.closest("[data-vaul-no-drag]"))return!1;if("right"===S||"left"===S)return!0;if(H.current&&l.getTime()-H.current.getTime()<500)return!1;if(null!==i&&("bottom"===S?i>0:i<0))return!0;if(o&&o.length>0)return!1;if(W.current&&l.getTime()-W.current.getTime()<h&&0===i||t)return W.current=l,!1;for(;r;){if(r.scrollHeight>r.clientHeight){if(0!==r.scrollTop)return W.current=new Date,!1;if("dialog"===r.getAttribute("role"))break}r=r.parentNode}return!0}function onDrag(e){if(Z.current&&j){let t="bottom"===S||"right"===S?1:-1,n=(K.current-(isVertical(S)?e.clientY:e.clientX))*t,o=n>0,i=s&&!g&&!o;if(i&&0===en)return;let l=Math.abs(n),u=document.querySelector("[vaul-drawer-wrapper]"),c=l/J.current,d=eu(l,o);if(null!==d&&(c=d),i&&c>=1||!Y.current&&!shouldDrag(e.target,o))return;if(Z.current.classList.add(m),Y.current=!0,set(Z.current,{transition:"none"}),set(B.current,{transition:"none"}),s&&el({draggedDistance:n}),o&&!s){let e=dampenValue(n),r=Math.min(-1*e,0)*t;set(Z.current,{transform:isVertical(S)?`translate3d(0, ${r}px, 0)`:`translate3d(${r}px, 0, 0)`});return}let f=1-c;if((ea||w&&en===w-1)&&(null==a||a(e,c),set(B.current,{opacity:`${f}`,transition:"none"},!0)),u&&B.current&&r){let e=Math.min(getScale()+c*(1-getScale()),1),t=8-8*c,n=Math.max(0,14-14*c);set(u,{borderRadius:`${t}px`,transform:isVertical(S)?`scale(${e}) translate3d(0, ${n}px, 0)`:`scale(${e}) translate3d(${n}px, 0, 0)`,transition:"none"},!0)}if(!s){let e=l*t;set(Z.current,{transform:isVertical(S)?`translate3d(0, ${e}px, 0)`:`translate3d(${e}px, 0, 0)`})}}}function closeDrawer(){Z.current&&(cancelDrag(),null==C||C(),set(Z.current,{transform:isVertical(S)?`translate3d(0, ${"bottom"===S?"100%":"-100%"}, 0)`:`translate3d(${"right"===S?"100%":"-100%"}, 0, 0)`,transition:`transform ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`}),set(B.current,{opacity:"0",transition:`opacity ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`}),scaleBackground(!1),setTimeout(()=>{k(!1),$(!1)},300),setTimeout(()=>{s&&er(s[0])},1e3*p.DURATION))}function resetDrawer(){if(!Z.current)return;let e=document.querySelector("[vaul-drawer-wrapper]"),t=getTranslate(Z.current,S);set(Z.current,{transform:"translate3d(0, 0, 0)",transition:`transform ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`}),set(B.current,{transition:`opacity ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`,opacity:"1"}),r&&t&&t>0&&O&&set(e,{borderRadius:"8px",overflow:"hidden",...isVertical(S)?{transform:`scale(${getScale()}) translate3d(0, calc(env(safe-area-inset-top) + 14px), 0)`,transformOrigin:"top"}:{transform:`scale(${getScale()}) translate3d(calc(env(safe-area-inset-top) + 14px), 0, 0)`,transformOrigin:"left"},transitionProperty:"transform, border-radius",transitionDuration:`${p.DURATION}s`,transitionTimingFunction:`cubic-bezier(${p.EASE.join(",")})`},!0)}function cancelDrag(){j&&Z.current&&(Z.current.classList.remove(m),Y.current=!1,V(!1),F.current=new Date)}function onRelease(e){var t;if(!j||!Z.current)return;Z.current.classList.remove(m),Y.current=!1,V(!1),F.current=new Date;let n=getTranslate(Z.current,S);if(!shouldDrag(e.target,!1)||!n||Number.isNaN(n)||null===z.current)return;let r=F.current.getTime()-z.current.getTime(),o=K.current-(isVertical(S)?e.clientY:e.clientX),i=Math.abs(o)/r;if(i>.05&&(U(!0),setTimeout(()=>{U(!1)},200)),s){let t="bottom"===S||"right"===S?1:-1;eo({draggedDistance:o*t,closeDrawer,velocity:i,dismissible:g}),null==u||u(e,!0);return}if("bottom"===S||"right"===S?o>0:o<0){resetDrawer(),null==u||u(e,!0);return}if(i>.4){closeDrawer(),null==u||u(e,!1);return}let l=Math.min(null!=(t=Z.current.getBoundingClientRect().height)?t:0,window.innerHeight);if(n>=l*f){closeDrawer(),null==u||u(e,!1);return}null==u||u(e,!0),resetDrawer()}function scaleBackground(e){let t=document.querySelector("[vaul-drawer-wrapper]");t&&r&&(e?(d&&!x&&(set(document.body,{background:document.body.style.backgroundColor||document.body.style.background}),set(document.body,{background:"black"},!0)),set(t,{borderRadius:"8px",overflow:"hidden",...isVertical(S)?{transform:`scale(${getScale()}) translate3d(0, calc(env(safe-area-inset-top) + 14px), 0)`,transformOrigin:"top"}:{transform:`scale(${getScale()}) translate3d(calc(env(safe-area-inset-top) + 14px), 0, 0)`,transformOrigin:"left"},transitionProperty:"transform, border-radius",transitionDuration:`${p.DURATION}s`,transitionTimingFunction:`cubic-bezier(${p.EASE.join(",")})`})):(reset(t,"overflow"),reset(t,"transform"),reset(t,"borderRadius"),set(t,{transitionProperty:"transform, border-radius",transitionDuration:`${p.DURATION}s`,transitionTimingFunction:`cubic-bezier(${p.EASE.join(",")})`})))}function onNestedOpenChange(e){let t=e?(window.innerWidth-16)/window.innerWidth:1;q.current&&window.clearTimeout(q.current),set(Z.current,{transition:`transform ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`,transform:`scale(${t}) translate3d(0, ${e?-16:0}px, 0)`}),!e&&Z.current&&(q.current=setTimeout(()=>{let e=getTranslate(Z.current,S);set(Z.current,{transition:"none",transform:isVertical(S)?`translate3d(0, ${e}px, 0)`:`translate3d(${e}px, 0, 0)`})},500))}function onNestedDrag(e,t){if(t<0)return;let n=isVertical(S)?window.innerHeight:window.innerWidth,r=(n-16)/n,o=r+t*(1-r),i=-16+16*t;set(Z.current,{transform:isVertical(S)?`scale(${o}) translate3d(0, ${i}px, 0)`:`scale(${o}) translate3d(${i}px, 0, 0)`,transition:"none"})}function onNestedRelease(e,t){let n=isVertical(S)?window.innerHeight:window.innerWidth,r=t?(n-16)/n:1,o=t?-16:0;t&&set(Z.current,{transition:`transform ${p.DURATION}s cubic-bezier(${p.EASE.join(",")})`,transform:isVertical(S)?`scale(${r}) translate3d(0, ${o}px, 0)`:`scale(${r}) translate3d(${o}px, 0, 0)`})}return i.useEffect(()=>()=>{scaleBackground(!1),es()},[]),i.useEffect(()=>{var e;function onVisualViewportChange(){if(!Z.current)return;let e=document.activeElement;if(isInput(e)||G.current){var t;let e=(null==(t=window.visualViewport)?void 0:t.height)||0,n=window.innerHeight-e,r=Z.current.getBoundingClientRect().height||0;Q.current||(Q.current=r);let o=Z.current.getBoundingClientRect().top;if(Math.abs(X.current-n)>60&&(G.current=!G.current),s&&s.length>0&&ei&&en){let e=ei[en]||0;n+=e}if(X.current=n,r>e||G.current){let t=Z.current.getBoundingClientRect().height,r=t;t>e&&(r=e-26),E?Z.current.style.height=`${t-Math.max(n,0)}px`:Z.current.style.height=`${Math.max(r,e-o)}px`}else Z.current.style.height=`${Q.current}px`;s&&s.length>0&&!G.current?Z.current.style.bottom="0px":Z.current.style.bottom=`${Math.max(n,0)}px`}}return null==(e=window.visualViewport)||e.addEventListener("resize",onVisualViewportChange),()=>{var e;return null==(e=window.visualViewport)?void 0:e.removeEventListener("resize",onVisualViewportChange)}},[en,s,ei]),i.useEffect(()=>{if(!O&&r){let e=setTimeout(()=>{reset(document.body)},200);return()=>clearTimeout(e)}},[O,r]),i.useLayoutEffect(()=>{e?($(!0),M(!0)):closeDrawer()},[e]),i.useEffect(()=>{N&&(null==t||t(O))},[O]),i.useEffect(()=>{_(!0)},[]),i.useEffect(()=>{O&&(set(document.documentElement,{scrollBehavior:"auto"}),H.current=new Date,scaleBackground(!0))},[O]),i.useEffect(()=>{if(Z.current&&I){var e;let t=null==Z?void 0:null==(e=Z.current)?void 0:e.querySelectorAll("*");null==t||t.forEach(e=>{(e.scrollHeight>e.clientHeight||e.scrollWidth>e.clientWidth)&&e.classList.add("vaul-scrollable")})}},[I]),i.createElement(o.fC,{modal:R,onOpenChange:n=>{if(void 0!==e){null==t||t(n);return}n?(M(!0),$(n)):closeDrawer()},open:O},i.createElement(l.Provider,{value:{visible:I,activeSnapPoint:et,snapPoints:s,setActiveSnapPoint:er,drawerRef:Z,overlayRef:B,scaleBackground,onOpenChange:t,onPress,setVisible:k,onRelease,onDrag,dismissible:g,handleOnly:v,isOpen:O,isDragging:j,shouldFade:ea,closeDrawer,onNestedDrag,onNestedOpenChange,onNestedRelease,keyboardIsOpen:G,openProp:e,modal:R,snapPointsOffset:ei,direction:S}},n))}let h=i.forwardRef(function({preventCycle:e=!1,children:t,...n},r){let{visible:o,closeDrawer:l,isDragging:a,snapPoints:u,activeSnapPoint:s,setActiveSnapPoint:c,dismissible:d,handleOnly:f,onPress:p,onDrag:m}=useDrawerContext(),h=i.useRef(null),g=i.useRef(!1);function handleStartCycle(){if(g.current){handleCancelInteraction();return}window.setTimeout(()=>{handleCycleSnapPoints()},120)}function handleCycleSnapPoints(){if(a||e||g.current){handleCancelInteraction();return}if(handleCancelInteraction(),(!u||0===u.length)&&d){l();return}let t=s===u[u.length-1];if(t&&d){l();return}let n=u.findIndex(e=>e===s);if(-1===n)return;let r=u[n+1];c(r)}function handleStartInteraction(){h.current=window.setTimeout(()=>{g.current=!0},250)}function handleCancelInteraction(){window.clearTimeout(h.current),g.current=!1}return i.createElement("div",{onClick:handleStartCycle,onDoubleClick:()=>{g.current=!0,l()},onPointerCancel:handleCancelInteraction,onPointerDown:e=>{f&&p(e),handleStartInteraction()},onPointerMove:e=>{f&&m(e)},ref:r,"vaul-drawer-visible":o?"true":"false","vaul-handle":"","aria-hidden":"true",...n},i.createElement("span",{"vaul-handle-hitarea":"","aria-hidden":"true"},t))});h.displayName="Drawer.Handle";let g=i.forwardRef(function({children:e,...t},n){let{overlayRef:r,snapPoints:l,onRelease:a,shouldFade:u,isOpen:s,visible:c}=useDrawerContext(),d=useComposedRefs(n,r),f=l&&l.length>0;return i.createElement(o.aV,{onMouseUp:a,ref:d,"vaul-drawer-visible":c?"true":"false","vaul-overlay":"","vaul-snap-points":s&&f?"true":"false","vaul-snap-points-overlay":s&&u?"true":"false",...t})});g.displayName="Drawer.Overlay";let v=i.forwardRef(function({onOpenAutoFocus:e,onPointerDownOutside:t,onAnimationEnd:n,style:r,...l},a){let{drawerRef:u,onPress:s,onRelease:c,onDrag:d,dismissible:f,keyboardIsOpen:p,snapPointsOffset:m,visible:h,closeDrawer:g,modal:v,openProp:w,onOpenChange:b,setVisible:y,handleOnly:E,direction:R}=useDrawerContext(),C=useComposedRefs(a,u),x=i.useRef(null),S=i.useRef(!1),isDeltaInDirection=(e,t,n=0)=>{if(S.current)return!0;let r=Math.abs(e.y),o=Math.abs(e.x),i=o>r,l=["bottom","right"].includes(t)?1:-1;if("left"===t||"right"===t){let t=e.x*l<0;if(!t&&o>=0&&o<=n)return i}else{let t=e.y*l<0;if(!t&&r>=0&&r<=n)return!i}return S.current=!0,!0};return i.useEffect(()=>{y(!0)},[]),i.createElement(o.VY,{"vaul-drawer":"","vaul-drawer-direction":R,"vaul-drawer-visible":h?"true":"false",...l,ref:C,style:m&&m.length>0?{"--snap-point-height":`${m[0]}px`,...r}:r,onOpenAutoFocus:t=>{if(e)e(t);else{var n;t.preventDefault(),null==(n=u.current)||n.focus()}},onPointerDown:e=>{E||(null==l.onPointerDown||l.onPointerDown.call(l,e),x.current={x:e.clientX,y:e.clientY},s(e))},onPointerDownOutside:e=>{if(null==t||t(e),!v||e.defaultPrevented){e.preventDefault();return}p.current&&(p.current=!1),e.preventDefault(),null==b||b(!1),f&&void 0===w&&g()},onFocusOutside:e=>{if(!v){e.preventDefault();return}},onEscapeKeyDown:e=>{if(!v){e.preventDefault();return}},onPointerMove:e=>{if(E||(null==l.onPointerMove||l.onPointerMove.call(l,e),!x.current))return;let t=e.clientY-x.current.y,n=e.clientX-x.current.x,r="touch"===e.pointerType?10:2,o=isDeltaInDirection({x:n,y:t},R,r);o?d(e):(Math.abs(n)>r||Math.abs(t)>r)&&(x.current=null)},onPointerUp:e=>{null==l.onPointerUp||l.onPointerUp.call(l,e),x.current=null,S.current=!1,c(e)}})});function NestedRoot({onDrag:e,onOpenChange:t,...n}){let{onNestedDrag:r,onNestedOpenChange:o,onNestedRelease:l}=useDrawerContext();if(!r)throw Error("Drawer.NestedRoot must be placed in another drawer");return i.createElement(Root,{nested:!0,onClose:()=>{o(!1)},onDrag:(t,n)=>{r(t,n),null==e||e(t,n)},onOpenChange:e=>{e&&o(e),null==t||t(e)},onRelease:l,...n})}v.displayName="Drawer.Content";let w={Root,NestedRoot,Content:v,Handle:h,Overlay:g,Trigger:o.xz,Portal:o.h_,Close:o.x8,Title:o.Dx,Description:o.dk}}}]);