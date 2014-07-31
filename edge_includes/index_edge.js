/**
 * Adobe Edge: symbol definitions
 */
(function($, Edge, compId){
//images folder
var im='images/';

var fonts = {};
   fonts['lusitana, serif']='<script src=\"http://use.edgefonts.net/lusitana:n7,n4:all.js\"></script>';
   fonts['source-sans-pro, sans-serif']='<script src=\"http://use.edgefonts.net/source-sans-pro:n4,n9,n7,i7,i4,n3,i3,n6,i6,i9,n2,i2:all.js\"></script>';


var resources = [
];
var symbols = {
"stage": {
   version: "2.0.1",
   minimumCompatibleVersion: "2.0.0",
   build: "2.0.1.268",
   baseState: "Base State",
   initialState: "Base State",
   gpuAccelerate: false,
   resizeInstances: false,
   content: {
         dom: [
         {
            id:'loading',
            type:'image',
            rect:['619px','320px','128px','128px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"loading.GIF",'0px','0px']
         },
         {
            id:'giphy',
            type:'image',
            rect:['-28px','-24px','1493px','828px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"giphy.gif",'0px','0px']
         },
         {
            id:'Text',
            display:'none',
            type:'text',
            rect:['39px','28px','501px','82px','auto','auto'],
            opacity:1,
            text:"power@world:~$ MONEY",
            font:['Lucida Console, Monaco, monospace',24,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'Text2',
            display:'none',
            type:'text',
            rect:['31px','136px','1456px','184px','auto','auto'],
            text:"power@world:~$ GREED",
            align:"left",
            font:['\'Lucida Console\', Monaco, monospace',109,"rgba(255,255,255,1)","normal","none","normal"]
         },
         {
            id:'Text3',
            display:'none',
            type:'text',
            rect:['1px','242px','1772px','184px','auto','auto'],
            text:"power@world:~$ POWER",
            align:"left",
            font:['\'Lucida Console\', Monaco, monospace',109,"rgba(255,255,255,1)","normal","none","normal"]
         },
         {
            id:'Text4',
            display:'none',
            type:'text',
            rect:['183px','66px','988px','214px','auto','auto'],
            text:"THEY ALL HAVE YOUR DATA",
            font:['Lucida Console, Monaco, monospace',63,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'Text5',
            display:'none',
            type:'text',
            rect:['89px','200px','1188px','340px','auto','auto'],
            text:"UNSECURED",
            align:"left",
            font:['\'Lucida Console\', Monaco, monospace',226,"rgba(0,0,0,1)","normal","none","normal"]
         },
         {
            id:'Text7',
            display:'none',
            type:'text',
            rect:['581px','402px','440px','104px','auto','auto'],
            text:"With",
            align:"left",
            font:['\'Lucida Console\', Monaco, monospace',63,"rgba(0,0,0,1)","normal","none","normal"]
         },
         {
            id:'Text8',
            display:'none',
            type:'text',
            rect:['25px','496px','1284px','246px','auto','auto'],
            text:"GREED ",
            align:"center",
            font:['\'Lucida Console\', Monaco, monospace',220,"rgba(0,0,0,1)","normal","none","normal"]
         },
         {
            id:'Text9',
            display:'none',
            type:'text',
            rect:['59px','58px','1246px','286px','auto','auto'],
            text:"So keep your data secure",
            align:"center",
            font:['\'Lucida Console\', Monaco, monospace',220,"rgba(0,0,0,1)","normal","none","normal"]
         },
         {
            id:'Text10',
            display:'none',
            type:'text',
            rect:['117px','88px','1208px','266px','auto','auto'],
            text:"With our encyption",
            align:"left",
            font:['source-sans-pro, sans-serif',148,"rgba(0,0,0,1.00)","100","none","normal"]
         },
         {
            id:'Ellipse',
            display:'none',
            type:'ellipse',
            rect:['47px','384px','1258px','346px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(0,0,0,1.00)"],
            stroke:[0,"rgba(0,0,0,1)","none"]
         },
         {
            id:'Text11',
            display:'none',
            type:'text',
            rect:['223px','404px','996px','102px','auto','auto'],
            text:"You're Safe",
            align:"left",
            font:['source-sans-pro, sans-serif',202,"rgba(255,255,255,1)","100","none","normal"]
         },
         {
            id:'padlock_silhouette-2555px',
            display:'none',
            type:'image',
            rect:['670px','418px','26px','37px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"padlock_silhouette-2555px.png",'0px','0px']
         }],
         symbolInstances: [

         ]
      },
   states: {
      "Base State": {
         "${_padlock_silhouette-2555px}": [
            ["style", "top", '392px'],
            ["style", "height", '63px'],
            ["style", "display", 'none'],
            ["style", "left", '266px'],
            ["style", "width", '44px']
         ],
         "${_Ellipse}": [
            ["color", "background-color", 'rgba(0,0,0,1.00)'],
            ["style", "display", 'none']
         ],
         "${_Text7}": [
            ["style", "top", '402px'],
            ["style", "left", '581px'],
            ["style", "display", 'none']
         ],
         "${_Text11}": [
            ["style", "top", '404px'],
            ["style", "font-family", 'source-sans-pro, sans-serif'],
            ["style", "display", 'none'],
            ["style", "font-weight", '100'],
            ["style", "left", '223px'],
            ["style", "font-size", '202px']
         ],
         "${_Text3}": [
            ["style", "top", '242px'],
            ["style", "left", '0px'],
            ["style", "display", 'none']
         ],
         "${_Text4}": [
            ["style", "top", '66px'],
            ["style", "display", 'none'],
            ["style", "font-family", 'Lucida Console, Monaco, monospace'],
            ["style", "left", '183px'],
            ["style", "font-size", '63px']
         ],
         "${_Text2}": [
            ["style", "top", '136px'],
            ["style", "left", '9px'],
            ["style", "display", 'none']
         ],
         "${_Text10}": [
            ["style", "top", '88px'],
            ["style", "display", 'none'],
            ["style", "font-weight", '100'],
            ["color", "color", 'rgba(0,0,0,1.00)'],
            ["style", "font-family", 'source-sans-pro, sans-serif'],
            ["style", "left", '117px'],
            ["style", "font-size", '148px']
         ],
         "${_Text8}": [
            ["style", "display", 'none'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '220px']
         ],
         "${_Text}": [
            ["style", "font-size", '109px'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "font-family", 'Lucida Console, Monaco, monospace'],
            ["style", "display", 'none'],
            ["style", "height", '160px'],
            ["style", "opacity", '1'],
            ["style", "left", '1px'],
            ["style", "width", '1353px']
         ],
         "${_Text5}": [
            ["style", "top", '200px'],
            ["style", "display", 'none'],
            ["style", "left", '89px'],
            ["style", "font-size", '226px']
         ],
         "${_Stage}": [
            ["color", "background-color", 'rgba(255,255,255,1)'],
            ["style", "width", '1366px'],
            ["style", "height", '768px'],
            ["style", "overflow", 'hidden']
         ],
         "${_Text9}": [
            ["style", "display", 'none']
         ],
         "${_giphy}": [
            ["style", "top", '-24px'],
            ["style", "display", 'block'],
            ["style", "overflow", 'visible'],
            ["style", "height", '828px'],
            ["style", "opacity", '0'],
            ["style", "left", '-28px'],
            ["style", "width", '1493px']
         ],
         "${_loading}": [
            ["style", "top", '320px'],
            ["style", "opacity", '1'],
            ["style", "left", '619px']
         ]
      }
   },
   timelines: {
      "Default Timeline": {
         fromState: "Base State",
         toState: "",
         duration: 18000,
         autoPlay: true,
         timeline: [
            { id: "eid20", tween: [ "style", "${_Text}", "width", '1353px', { fromValue: '1353px'}], position: 3880, duration: 0 },
            { id: "eid117", tween: [ "style", "${_giphy}", "display", 'none', { fromValue: 'block'}], position: 5893, duration: 0 },
            { id: "eid40", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid38", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'none'}], position: 4250, duration: 0 },
            { id: "eid58", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4328, duration: 0 },
            { id: "eid59", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 4345, duration: 0 },
            { id: "eid60", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4378, duration: 0 },
            { id: "eid61", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 4388, duration: 0 },
            { id: "eid62", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4403, duration: 0 },
            { id: "eid63", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'block'}], position: 4432, duration: 0 },
            { id: "eid64", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 4449, duration: 0 },
            { id: "eid65", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4482, duration: 0 },
            { id: "eid66", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 4492, duration: 0 },
            { id: "eid67", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4507, duration: 0 },
            { id: "eid68", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'block'}], position: 4536, duration: 0 },
            { id: "eid69", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 4553, duration: 0 },
            { id: "eid70", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4586, duration: 0 },
            { id: "eid71", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 4596, duration: 0 },
            { id: "eid39", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 4633, duration: 0 },
            { id: "eid115", tween: [ "style", "${_Text2}", "display", 'none', { fromValue: 'block'}], position: 5893, duration: 0 },
            { id: "eid136", tween: [ "style", "${_Text3}", "left", '0px', { fromValue: '0px'}], position: 10250, duration: 0 },
            { id: "eid137", tween: [ "style", "${_padlock_silhouette-2555px}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid138", tween: [ "style", "${_padlock_silhouette-2555px}", "display", 'block', { fromValue: 'none'}], position: 15000, duration: 0 },
            { id: "eid11", tween: [ "style", "${_giphy}", "opacity", '0', { fromValue: '0'}], position: 2644, duration: 0 },
            { id: "eid10", tween: [ "style", "${_giphy}", "opacity", '0.01', { fromValue: '0'}], position: 2750, duration: 0 },
            { id: "eid12", tween: [ "style", "${_giphy}", "opacity", '1', { fromValue: '0.01'}], position: 3000, duration: 0 },
            { id: "eid13", tween: [ "style", "${_giphy}", "opacity", '1', { fromValue: '1'}], position: 3055, duration: 0 },
            { id: "eid125", tween: [ "style", "${_Text8}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid122", tween: [ "style", "${_Text8}", "display", 'block', { fromValue: 'none'}], position: 6500, duration: 0 },
            { id: "eid123", tween: [ "style", "${_Text8}", "display", 'block', { fromValue: 'block'}], position: 6750, duration: 0 },
            { id: "eid126", tween: [ "style", "${_Text8}", "display", 'none', { fromValue: 'block'}], position: 8250, duration: 0 },
            { id: "eid134", tween: [ "style", "${_Text9}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid133", tween: [ "style", "${_Text9}", "display", 'none', { fromValue: 'none'}], position: 8126, duration: 0 },
            { id: "eid132", tween: [ "style", "${_Text9}", "display", 'block', { fromValue: 'none'}], position: 8250, duration: 0 },
            { id: "eid135", tween: [ "style", "${_Text9}", "display", 'none', { fromValue: 'block'}], position: 10109, duration: 0 },
            { id: "eid152", tween: [ "style", "${_Ellipse}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid155", tween: [ "style", "${_Ellipse}", "display", 'block', { fromValue: 'none'}], position: 10109, duration: 0 },
            { id: "eid151", tween: [ "style", "${_Text11}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid154", tween: [ "style", "${_Text11}", "display", 'block', { fromValue: 'none'}], position: 10109, duration: 0 },
            { id: "eid41", tween: [ "style", "${_Text2}", "left", '9px', { fromValue: '9px'}], position: 4712, duration: 0 },
            { id: "eid118", tween: [ "style", "${_Text4}", "display", 'block', { fromValue: 'none'}], position: 6000, duration: 0 },
            { id: "eid129", tween: [ "style", "${_Text4}", "display", 'none', { fromValue: 'block'}], position: 8250, duration: 0 },
            { id: "eid142", tween: [ "style", "${_padlock_silhouette-2555px}", "height", '1249px', { fromValue: '63px'}], position: 15000, duration: 2750 },
            { id: "eid148", tween: [ "style", "${_padlock_silhouette-2555px}", "height", '2401px', { fromValue: '1249px'}], position: 17750, duration: 250 },
            { id: "eid119", tween: [ "style", "${_Text5}", "display", 'block', { fromValue: 'none'}], position: 6000, duration: 0 },
            { id: "eid128", tween: [ "style", "${_Text5}", "display", 'none', { fromValue: 'block'}], position: 8250, duration: 0 },
            { id: "eid150", tween: [ "style", "${_Text10}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid153", tween: [ "style", "${_Text10}", "display", 'block', { fromValue: 'none'}], position: 10109, duration: 0 },
            { id: "eid143", tween: [ "style", "${_padlock_silhouette-2555px}", "top", '-388px', { fromValue: '392px'}], position: 15000, duration: 2750 },
            { id: "eid147", tween: [ "style", "${_padlock_silhouette-2555px}", "top", '-1274px', { fromValue: '-388px'}], position: 17750, duration: 250 },
            { id: "eid124", tween: [ "style", "${_Text7}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid120", tween: [ "style", "${_Text7}", "display", 'none', { fromValue: 'none'}], position: 6000, duration: 0 },
            { id: "eid121", tween: [ "style", "${_Text7}", "display", 'block', { fromValue: 'none'}], position: 6250, duration: 0 },
            { id: "eid127", tween: [ "style", "${_Text7}", "display", 'none', { fromValue: 'block'}], position: 8250, duration: 0 },
            { id: "eid22", tween: [ "color", "${_Text}", "color", 'rgba(255,255,255,1.00)', { animationColorSpace: 'RGB', valueTemplate: undefined, fromValue: 'rgba(255,255,255,1.00)'}], position: 3880, duration: 0 },
            { id: "eid42", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid72", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5298, duration: 0 },
            { id: "eid73", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5315, duration: 0 },
            { id: "eid74", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5348, duration: 0 },
            { id: "eid75", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5358, duration: 0 },
            { id: "eid76", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5373, duration: 0 },
            { id: "eid77", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'block'}], position: 5402, duration: 0 },
            { id: "eid78", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5419, duration: 0 },
            { id: "eid79", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5452, duration: 0 },
            { id: "eid80", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5462, duration: 0 },
            { id: "eid81", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5477, duration: 0 },
            { id: "eid82", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'block'}], position: 5506, duration: 0 },
            { id: "eid83", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5523, duration: 0 },
            { id: "eid84", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5556, duration: 0 },
            { id: "eid86", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'block'}], position: 5566, duration: 0 },
            { id: "eid87", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5583, duration: 0 },
            { id: "eid88", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5616, duration: 0 },
            { id: "eid89", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5626, duration: 0 },
            { id: "eid90", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5641, duration: 0 },
            { id: "eid91", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'block'}], position: 5670, duration: 0 },
            { id: "eid92", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5687, duration: 0 },
            { id: "eid93", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5720, duration: 0 },
            { id: "eid94", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5730, duration: 0 },
            { id: "eid95", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5745, duration: 0 },
            { id: "eid96", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'block'}], position: 5774, duration: 0 },
            { id: "eid97", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5791, duration: 0 },
            { id: "eid98", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5824, duration: 0 },
            { id: "eid43", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 5834, duration: 0 },
            { id: "eid114", tween: [ "style", "${_Text3}", "display", 'none', { fromValue: 'block'}], position: 5893, duration: 0 },
            { id: "eid130", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 8250, duration: 0 },
            { id: "eid21", tween: [ "style", "${_Text}", "font-size", '109px', { fromValue: '109px'}], position: 3880, duration: 0 },
            { id: "eid144", tween: [ "style", "${_padlock_silhouette-2555px}", "width", '872px', { fromValue: '44px'}], position: 15000, duration: 2750 },
            { id: "eid149", tween: [ "style", "${_padlock_silhouette-2555px}", "width", '1676px', { fromValue: '872px'}], position: 17750, duration: 250 },
            { id: "eid9", tween: [ "style", "${_loading}", "opacity", '1', { fromValue: '1'}], position: 0, duration: 0 },
            { id: "eid3", tween: [ "style", "${_loading}", "opacity", '0', { fromValue: '1'}], position: 2250, duration: 750 },
            { id: "eid146", tween: [ "style", "${_padlock_silhouette-2555px}", "left", '-138px', { fromValue: '266px'}], position: 17750, duration: 250 },
            { id: "eid7", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid23", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3579, duration: 0 },
            { id: "eid24", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 3596, duration: 0 },
            { id: "eid25", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3629, duration: 0 },
            { id: "eid26", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 3639, duration: 0 },
            { id: "eid27", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3654, duration: 0 },
            { id: "eid28", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'block'}], position: 3683, duration: 0 },
            { id: "eid29", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 3700, duration: 0 },
            { id: "eid30", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3733, duration: 0 },
            { id: "eid31", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 3743, duration: 0 },
            { id: "eid32", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3758, duration: 0 },
            { id: "eid33", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'block'}], position: 3787, duration: 0 },
            { id: "eid34", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 3804, duration: 0 },
            { id: "eid35", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3837, duration: 0 },
            { id: "eid36", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 3847, duration: 0 },
            { id: "eid37", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'none'}], position: 3862, duration: 0 },
            { id: "eid8", tween: [ "style", "${_Text}", "display", 'block', { fromValue: 'block'}], position: 3880, duration: 0 },
            { id: "eid116", tween: [ "style", "${_Text}", "display", 'none', { fromValue: 'block'}], position: 5893, duration: 0 },
            { id: "eid19", tween: [ "style", "${_Text}", "left", '1px', { fromValue: '1px'}], position: 3880, duration: 0 },
            { id: "eid16", tween: [ "style", "${_Text}", "height", '160px', { fromValue: '160px'}], position: 3880, duration: 0 }         ]
      }
   }
}
};


Edge.registerCompositionDefn(compId, symbols, fonts, resources);

/**
 * Adobe Edge DOM Ready Event Handler
 */
$(window).ready(function() {
     Edge.launchComposition(compId);
});
})(jQuery, AdobeEdge, "EDGE-9632012");
