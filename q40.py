#matching brackets.py


samplelist = [
"< >< ><[(t(w))t]x[z]>((w)){[[z]u]/}<f><y>(v){fu(})",
"((+)[h] )[<(e)y> <a>{x[d({*}y)]}(a)[*][a<b>]](y( ))<h>{}",
"<<[y]-> [b](y)>(<v({-}-){ }[w]><(<f>(<v> )d)g{<^</> x}>x){}",
"<( ) ><b>{{(<t<t{ })*}{z}/}<({/}y)<^><[ ](+)((-<%>{t})>w>u)/>><g>",
"<z>[y][*[>](*)<[-]%<d>>]<<h<</>[b](t{f})h><w>{v}<a>h<a>>",
"(d{*}<y>)((y){<*>w}e)[{b}*{[u]d}[{u}g]( )]{ }{[a]*(t)<c>}()",
"</{{d}u}{[w]c}[[g  ]]<a([w]y)>{v}<b>( )c]<a>>[[x]](<+><w>%)",
"<(v<u>)<h( [h])>< >[g]((x a)(h<f><v>[+<<w> >{ }]{t})[[/]+]><y>",
"{{ }}(a<u(b)((x))(t)[t]v{( <f}>%)[e<%>]>{%}[+][^](b[t])<t>)",
"(*<(/){<w>(+)*{^} b><v>){b}(d(^))((f)[c])",
"[t](*)([v](/){<w>{^}a/){ <u>}<t>+}){-}[x]{(}",
"(t)[[[b][x]<u>v[[u]g)<<b>z>](/<^>[a]] <h>]({^})",
"<y{v}>{}[y]<{[-(a)]b}[d]h>[e][f](%)(c)<u>",
"(<{z}b>[(w)*][[z]d<z>([hfa)<%(+)><{<]>d(v)}b>](*))",
"(([[u]f]v)<z><v>[z]((^)d<z>)(%{ (e)/}<t>a[y]}))",
"<-{%}>{t}<[+[[ ] ]](u{z}(+)(d))y<d(^)>><d>[[{y}+]]",
"{c}[ ]{y[%[ ]]}((/)[%][e]{+}[d]v){}[ ][y(f)]{{d}[z]h(+)}<y>",
"<[x]>{[ ]< {c{^{t}}}>((c)  )g<c{(z)<g>[b]/}>)[w]{ }%}"]

openlist = ['(','[','{','<']
closedlist = [')',']','}','>']

def check(astring):
   mylist=[]
   error = 0
   for i in astring:
       if i in openlist:
           mylist.append(i)
       elif i in closedlist:
           if (len(mylist) > 0):
              var = mylist.pop()
              pos = closedlist.index(i)
              if var != openlist[pos]:
                   error += 1
   if len(mylist) != 0:
       error += 1


   if error == 0 :
       print (1)
       print(" ")
   else:
       print(0)
       print(" ")


for s in samplelist:
    check(s)
