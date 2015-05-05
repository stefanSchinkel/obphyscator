##ophyscator


A rather simple email obfusctor for website that _encrypts_ (encryption as in obfuscation) an `<mailto>` link in JavaScript. I like to imagine this prevents spam (and so far it actually did  - much to my surprise).

###Usage:


```sh
$>ophyscator mail@example.com "Click Here"
```

The result is an HTML snippet like the one below

```
<ins>
<span style="display:inline;" id="ophyscator"></span>
<script type="text/javaScript">
var a = new Array('i','c','a','l','m','a','m','m','o','i','.','@','l');
var b = new Array('f','j','l',' ','s',' ',' ');
var str = "<a href='mailto:"+a[7]+a[5]+a[0]+a[3]+a[11]+a[6]+a[2]+a[9]+a[12]+a[10]+a[1]+a[8]+a[4]+"'>"+b[0]+b[5]+b[1]+b[3]+b[4]+b[6]+b[2]+"</a>";
document.getElementById('ophyscator').innerHTML = str;
</script>
<noscript>
<p>Sorry, you need to have JavaScript enabled to get the mail address</p>
</noscript>
</ins>
```
that replaces the `<a href="mailto:mail@example.com> Click Here</a>` part of your HTML file.
