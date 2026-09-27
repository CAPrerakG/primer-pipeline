(function(){
  var D=window.PRIMER_DATA||{};
  var NS="http://www.w3.org/2000/svg";
  function el(t,a,txt){var e=document.createElementNS(NS,t);for(var k in a)e.setAttribute(k,a[k]);if(txt!=null)e.textContent=txt;return e;}
  function nice(lo,hi){var p=(hi-lo)*0.14;if(lo<0)lo-=p;hi+=p*0.5;var span=hi-lo,step=span>80?20:span>40?10:span>16?5:span>8?2:1;lo=Math.floor(lo/step)*step;hi=Math.ceil(hi/step)*step;var t=[];for(var v=lo;v<=hi+1e-9;v+=step)t.push(Math.round(v*10)/10);return{min:lo,max:hi,ticks:t};}
  function chart(svg,data,opt){
    var vb=svg.getAttribute("viewBox").split(" "),W=+vb[2],H=+vb[3],L=46,R=10,T=20,B=opt.sub?52:34;
    var vals=data.map(function(d){return d.v;}),sc=nice(Math.min(0,Math.min.apply(null,vals)),Math.max(0,Math.max.apply(null,vals)));
    var n=data.length,cw=(W-L-R)/n,y=function(v){return T+(sc.max-v)/(sc.max-sc.min)*(H-T-B);};
    if(opt.band){svg.appendChild(el("rect",{x:L+cw*opt.band[0],y:T,width:cw*(opt.band[1]-opt.band[0]+1),height:H-T-B,"class":"c-band"}));}
    sc.ticks.forEach(function(t){svg.appendChild(el("line",{x1:L,x2:W-R,y1:y(t),y2:y(t),"class":t===0?"c-zero":"c-axis"}));svg.appendChild(el("text",{x:L-8,y:y(t)+4,"text-anchor":"end","class":"c-txt"},(t>0?"+":"")+t));});
    data.forEach(function(d,i){var v=d.v,x=L+cw*i+cw*0.18,w=cw*0.64,y0=y(0),yv=y(v);
      svg.appendChild(el("rect",{x:x,y:Math.min(y0,yv),width:w,height:Math.max(1,Math.abs(yv-y0)),"class":v>=0?"c-pos":"c-neg",rx:2}));
      svg.appendChild(el("text",{x:x+w/2,y:v>=0?yv-5:yv+14,"text-anchor":"middle","class":"c-val"},(v>0?"+":"")+v.toFixed(1)));
      svg.appendChild(el("text",{x:x+w/2,y:H-B+18,"text-anchor":"middle","class":"c-txt"},d.label));
      if(d.sub)svg.appendChild(el("text",{x:x+w/2,y:H-B+34,"text-anchor":"middle","class":"c-txt"},d.sub));});
  }
  document.querySelectorAll("svg[data-chart]").forEach(function(svg){
    var k=svg.getAttribute("data-chart");
    if(k==="month"&&D.monthly){var ML="JFMAMJJASOND";chart(svg,D.monthly.map(function(m,i){return{v:m.rel,label:ML[i],sub:m.hit+"/"+m.n};}),{sub:true,band:D.band||null});}
    if(k==="year"&&D.cy){chart(svg,D.cy.map(function(c){return{v:c.rel,label:"'"+String(c.y).slice(2)};}),{});}
    if(k==="win"&&D.wy){var w=D.wy[svg.getAttribute("data-win")];if(w)chart(svg,w.map(function(c){return{v:c.v,label:"'"+String(c.y).slice(2)};}),{});}
    if(k==="mon"&&D.my){var mm=D.my[svg.getAttribute("data-m")];if(mm)chart(svg,Object.keys(mm).sort().map(function(y){return{v:mm[y],label:"'"+y.slice(2)};}),{});}
  });
  function sg(v){return(v>0?"+":"")+v;}
  document.querySelectorAll("tbody[data-table]").forEach(function(tb){
    var k=tb.getAttribute("data-table");
    if(k==="cy"&&D.cy){D.cy.forEach(function(c){var tr=document.createElement("tr");var ys=String(c.y);
      var hx=D.hx?'<td class="num">'+((D.hx.v&&D.hx.v[ys]!=null)?D.hx.v[ys]:'–')+'</td>':'';
      var nt=D.notes?'<td class="note-cell">'+(D.notes[ys]||'')+'</td>':'';
      tr.innerHTML='<td class="num">'+c.y+(c.partial?'*':'')+'</td>'+hx+nt+'<td class="num '+(c.b>=0?'pos':'negc')+'">'+sg(c.b.toFixed(1))+'%</td><td class="num">'+sg(c.n.toFixed(1))+'%</td><td class="num '+(c.rel>=0?'pos':'negc')+'">'+sg(c.rel.toFixed(1))+'</td>';tb.appendChild(tr);});}
    if(k==="dd"&&D.dd){D.dd.forEach(function(d){var tr=document.createElement("tr");tr.innerHTML='<td>'+d.co+'</td><td>'+d.peak+'</td><td class="num '+(d.fp>=0?'pos':'negc')+'">'+sg(d.fp)+'%</td><td class="num '+(d.y1>=0?'pos':'negc')+'">'+sg(d.y1)+'%</td>';tb.appendChild(tr);});}
  });
  var q=document.getElementById("gq");
  if(q){var cnt=document.getElementById("gcount"),none=document.getElementById("gnone");
    var pairs=[].slice.call(document.querySelectorAll(".gl dt")).map(function(dt){return[dt,dt.nextElementSibling];});
    var run=function(){var s=q.value.trim().toLowerCase(),shown=0;
      pairs.forEach(function(p){var hit=!s||(p[0].textContent+" "+p[1].textContent).toLowerCase().indexOf(s)>-1;p[0].hidden=!hit;p[1].hidden=!hit;if(hit)shown++;});
      document.querySelectorAll(".gl dl").forEach(function(dl){var any=[].some.call(dl.querySelectorAll("dt"),function(d){return!d.hidden;});dl.hidden=!any;if(dl.previousElementSibling&&dl.previousElementSibling.tagName==="H3")dl.previousElementSibling.hidden=!any;});
      if(cnt)cnt.textContent=s?shown+" of "+pairs.length+" terms":pairs.length+" terms";if(none)none.hidden=shown>0;};
    q.addEventListener("input",run);run();}
})();
