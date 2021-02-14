let xs = $(".lang-ja .part pre[id^='pre-sample']");
let ret = ""
for (let i = 0; i < xs.length; i += 2){
  id = (i / 2) + 1;
  q = xs[i].innerText;
  a = xs[i + 1].innerText;
  ret += `T${id} = """\n${q}"""\n`
  ret += `TEST_T${id} = """\n>>> as_input(T${id})\n>>> main()\n${a}"""\n`
}
xs[0].innerText = ret;