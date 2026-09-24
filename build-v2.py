# gera v2.html a partir do index.html: herói -> entregáveis -> planos (dor + entregáveis com ícone)
src = open('../maleta-lp/index.html', encoding='utf-8').read()
h = src

def cut(h, start, end):
    a = h.index(start); b = h.index(end, a)
    return h[:a] + h[b:]

h = h.replace('A MALETA DO ADVOGADO · E3 DIGITAL · v2', 'A MALETA DO ADVOGADO · E3 DIGITAL · v2 curta: herói, entregáveis, planos')

# ---------- CSS extra (antes do bloco mobile) ----------
css = '''
/* planos v2: dor e os entregáveis que a resolvem, ícone no lugar do check */
.plan .dores{display:flex;flex-direction:column;gap:20px;flex:1}
.plan .dor{display:flex;flex-direction:column;gap:9px}
.plan .dor b{font-family:var(--ffd);font-size:1.02rem;font-weight:600;letter-spacing:-.015em;line-height:1.3;color:#fff}
.plan .sol{display:flex;flex-direction:column;gap:4px}
.plan .sol span{display:flex;align-items:center;gap:9px;font-size:.86rem;line-height:1.3;color:var(--t-2);padding:2px 0}
.plan .sol img{width:32px;height:32px;flex:none}
.plan--hot .sol span{color:rgba(255,255,255,.9)}
.plan .dor+.dor{padding-top:18px;border-top:1px solid var(--hair-2)}
.plan--hot .dor+.dor{border-top-color:rgba(255,255,255,.12)}
'''
h = h.replace('/* ---------- mobile ---------- */', css + '\n/* ---------- mobile ---------- */', 1)

# ---------- palco 1: só o herói, maleta girando ----------
a = h.index('<section class="stage" id="stage1"'); b = h.index('<!-- ================= RIMA')
stage = '''<section class="stage" id="stage1" style="height:200vh">
  <div class="pin">
    <div id="obj"><canvas id="c1" width="1024" height="576" data-n="65"></canvas></div>

    <div class="blk blk--l" data-w="0,1">
      <h1 class="h-mega ttl">Tudo o que o seu escritório precisa para <span class="hl">faturar mais,</span> <span class="hl">dentro de uma maleta.</span></h1>
      <p class="lede">CRM, scripts de atendimento, follow-ups, curso comercial, templates de conteúdo, apresentações, playbooks, ferramentas de gestão e muito mais. Tudo pronto para você adaptar e aplicar no seu escritório.</p>
    </div>

    <div class="hint" id="hint"><span>Role</span><i></i></div>
  </div>
</section>

'''
h = h[:a] + stage + h[b:]

# ---------- tira rima, quem montou, depoimentos ----------
h = cut(h, '<!-- ================= RIMA', '<!-- ================= PALCO 2: DENTRO')
# ---------- tira comparar, editável, para quem é, custo afundado ----------
h = cut(h, '<!-- ================= DO ZERO x COM A MALETA', '<!-- ================= PLANOS')
# ---------- tira o modal de vídeo ----------
h = cut(h, '<div class="vmodal"', '<script>')

# lede do "dentro" vira a ponte do herói
h = h.replace('Cada compartimento resolve uma trava do escritório: o que postar, como atender e como medir. Role e a maleta abre.',
              'CRM, scripts, playbooks, planilhas, posts e o Curso Comercial E3. Cada compartimento resolve uma trava do escritório: o que postar, como atender e como medir. Role e a maleta abre.')

# ---------- planos ----------
def sol(items):
    return '<div class="sol">' + ''.join(f'<span><img src="img/p-{k}.png" alt="">{t}</span>' for k, t in items) + '</div>'
def dor(txt, items):
    return f'<div class="dor"><b>{txt}</b>{sol(items)}</div>'

start = ''.join([
    dor('Lead que pergunta o preço e some.', [('crm','Modelo de CRM'),('scripts','Scripts de atendimento e follow-up')]),
    dor('Semana que passa sem post.', [('posts','Pack de posts editáveis')]),
    dor('Proposta montada na hora, cada vez de um jeito.', [('apresentacao','Apresentação comercial editável')]),
    dor('Comissão calculada de cabeça.', [('comissao','Planilha de comissionamento')]),
])
pro = ''.join([
    dor('Reunião que termina em “vou pensar”.', [('curso','Curso Comercial E3'),('reuniao','Playbook de reunião comercial'),('objecoes','Banco de objeções com respostas'),('checklist','Checklist de fechamento')]),
    dor('Follow-up que fica para amanhã.', [('followup','Playbook de follow-up'),('scripts','Scripts completos de WhatsApp')]),
    dor('Mês que fecha sem meta e sem número.', [('metas','Calculadora de metas comerciais'),('dashboard','Dashboard de indicadores')]),
    dor('Conteúdo que para na segunda semana.', [('calendario','Calendário de conteúdo de 90 dias'),('reels','Pack de roteiros para Reels'),('prompts','Biblioteca com mais de 100 prompts de IA')]),
    dor('Proposta que leva dias para sair.', [('propostas','Modelos de proposta comercial')]),
])
black = ''.join([
    dor('Anúncio que gasta e não traz cliente.', [('anuncios','Modelos de anúncios'),('headlines','Banco de headlines e chamadas'),('cta','Biblioteca de chamadas para ação')]),
    dor('Calendário que acaba em três meses.', [('calendario','Calendário editorial de 180 dias'),('prompts','Prompts avançados de IA para conteúdo')]),
    dor('Cada pessoa da equipe atende de um jeito.', [('playbook','Playbook comercial completo'),('scripts','Mais de 50 scripts comerciais'),('reuniao','Roteiro completo de reunião'),('objecoes','Playbook de tratamento de objeções'),('fechamento','Manual de fechamento')]),
    dor('Sem saber quanto custa cada cliente novo.', [('cac','Planilha de CAC e ROI'),('leads','Planilha de acompanhamento de leads'),('indicadores','Indicadores essenciais do escritório')]),
])

def swap_plan(h, plan, inc, body):
    a = h.index(f'data-plan="{plan}"'); i = h.index('<div class="inc">', a); j = h.index('</ul>', i) + len('</ul>')
    return h[:i] + f'<div class="inc">{inc}</div>\n        <div class="dores">{body}</div>' + h[j:]
h = swap_plan(h, 'start', 'A Start resolve:', start)
h = swap_plan(h, 'black', 'Tudo da Pro, e ainda resolve:', black)
h = swap_plan(h, 'pro', 'Tudo da Start, e ainda resolve:', pro)
h = h.replace('<div class="eyebrow rv">Escolha o tamanho</div>', '<div class="eyebrow rv">Escolha pelo que trava o seu escritório</div>')
h = h.replace('<h2 class="h-lg ttl rv" data-d="1">Três tamanhos de maleta. <span class="hl">Pagamento único.</span></h2>',
              '<h2 class="h-lg ttl rv" data-d="1">Cada tamanho resolve <span class="hl">um conjunto de travas.</span></h2>')
h = h.replace('<p class="lede rv" data-d="2">Sem mensalidade e sem software para assinar. Você escolhe o tamanho, paga uma vez e recebe tudo no e-mail em seguida.</p>',
              '<p class="plans-key rv" data-d="2"><span class="hot">Pagamento único, sem mensalidade e sem software para assinar.</span> Leia o que cada plano resolve, escolha o seu e receba tudo no e-mail em seguida.</p>')
h = h.replace('.plans-head .lede{margin:18px auto 0;text-align:center}',
              '''.plans-head .lede{margin:18px auto 0;text-align:center}
.plans-key{margin:22px auto 0;max-width:34ch;font-family:var(--ffd);font-weight:600;font-size:clamp(1.25rem,2vw,1.7rem);line-height:1.3;letter-spacing:-.02em;color:var(--t-2)}
.plans-key .hot{display:block;margin-bottom:6px}''')

# ---------- JS ----------
a = h.index('const KF=['); b = h.index('];', a) + 2
h = h[:a] + '''const KF=[
  {p:0, x:22, y:2, s:1.08, r:-2},
  {p:1, x:22, y:2, s:1.08, r:-2}
];''' + h[b:]
old = '''  let f;
  if(p<.2)f=0;
  else f=(p-.2)/.8;
  giro.set(f);'''
assert old in h
h = h.replace(old, '  giro.set(p);')
h = h.replace("const x=m?0:k.x,y=m?0:k.y,s=m?(p<.2?1.02:.9):k.s;", "const x=m?0:k.x,y=m?0:k.y,s=m?1.02:k.s;")
h = cut(h, '/* ---------- depoimentos ---------- */', '/* ---------- faq ---------- */')
h = h.replace("$$('h1,section h2,.edit h3,.who h3,.two h3')", "$$('h1,section h2,.two h3')")


# ---------- "o que tem dentro": copy nova (sessão 2) ----------
MK=[('posts','Pack de posts editáveis','Conteúdos prontos para adaptar à realidade do seu escritório.'),
    ('reels','Roteiros de Reels','Estruturas para transformar conhecimento jurídico em vídeos.'),
    ('headlines','Banco de headlines e chamadas','Ideias para chamar atenção e fazer o público parar para consumir seu conteúdo.'),
    ('anuncios','Modelos de anúncios','Estruturas para apresentar sua oferta e gerar novas oportunidades.'),
    ('calendario','Calendário editorial de 180 dias','Um direcionamento para você saber o que publicar e não depender da inspiração.'),
    ('cta','Biblioteca de chamadas para ação','Chamadas para transformar atenção em próximo passo.'),
    ('prompts','Prompts avançados de IA','Use IA para acelerar a criação sem precisar começar cada conteúdo do zero.')]
CO=[('curso','Curso Comercial E3','Aprenda a conduzir o processo comercial do diagnóstico ao fechamento.'),
    ('playbook','Playbook Comercial','Tenha uma estrutura clara para organizar o processo de vendas.'),
    ('followup','Playbook de Follow-up','Saiba o que fazer quando o lead não responde, pede tempo ou desaparece.'),
    ('objecoes','Playbook de Objeções','Respostas e direcionamentos para as principais objeções comerciais.'),
    ('scripts','+50 Scripts Comerciais','Mensagens prontas para diferentes momentos da jornada do lead.'),
    ('propostas','Modelos de Propostas','Apresente sua solução de forma mais profissional e estruturada.'),
    ('apresentacao','Modelos de Apresentação','Tenha uma estrutura visual para conduzir sua reunião e apresentar sua solução.'),
    ('reuniao','Roteiro de Reunião','Saiba o que perguntar, quando perguntar e como conduzir a conversa.'),
    ('fechamento','Manual de Fechamento','Transforme uma conversa comercial em um próximo passo claro.')]
GE=[('crm','CRM','Saiba onde cada oportunidade está e qual deve ser o próximo passo.'),
    ('dashboard','Dashboard Comercial','Tenha uma visão geral da performance do seu processo comercial.'),
    ('metas','Calculadora de Metas','Descubra quantos leads, reuniões e contratos são necessários para atingir sua meta.'),
    ('comissao','Planilha de Comissionamento','Organize metas, vendas e comissões do time.'),
    ('cac','Planilha de CAC e ROI','Entenda quanto você investe para gerar uma oportunidade e quanto ela retorna.'),
    ('leads','Planilha de Acompanhamento de Leads','Controle o volume e a evolução das oportunidades.'),
    ('indicadores','Indicadores Essenciais','Acompanhe os números que realmente importam para o crescimento comercial.')]
def items(lst):
    return '<div class="items">' + ''.join(f'<div class="it"><img src="img/p-{k}.png" alt=""><div><b>{n}</b><span>{d}</span></div></div>' for k,n,d in lst) + '</div>'
def comp(num, nome, n, quote, corpo, h4, lst, res):
    return f"""        <div class="comp rv">
          <div class="top"><h3><small>{num}</small>{nome}</h3><div class="n">{n} peças</div></div>
          <p class="quote">“{quote}”</p>
          {corpo}
          <h4>{h4}</h4>
          {items(lst)}
          <p class="res"><small>Resultado</small>{res}</p>
        </div>
"""
comps = comp('01','Marketing',7,'Eu sei que preciso produzir conteúdo, mas não sei o que postar.',
    '<div class="story"><p>A falta de conteúdo não é necessariamente falta de conhecimento. É falta de estrutura para transformar conhecimento em conteúdo com consistência.</p><p>Você não precisa passar horas pensando no próximo post.</p></div>',
    '7 peças para nunca mais começar o conteúdo do zero.', MK,
    'Mais consistência para gerar atenção, autoridade e demanda.')
comps += comp('02','Comercial',9,'Os leads chegam. O problema é o que acontece depois.',
    '<div class="story"><p>O lead pergunta o preço. Você responde. Ele diz que vai pensar. E desaparece.</p><p>Ou participa da reunião, recebe a proposta e nunca mais responde.</p><p>É aqui que muitos escritórios deixam dinheiro na mesa. A Maleta transforma o comercial em um processo, em vez de depender de improviso, talento individual ou “feeling”.</p></div>',
    '9 peças para transformar oportunidades em contratos.', CO,
    'Mais processo. Mais previsibilidade. Mais oportunidades aproveitadas.')
comps += comp('03','Gestão',7,'Eu vendo, mas não sei exatamente o que está funcionando.',
    '<ul class="qs"><li>Quantos leads entraram?</li><li>Quantos foram atendidos?</li><li>Quantos viraram reunião?</li><li>Quantas propostas foram enviadas?</li><li>Quantos contratos foram fechados?</li><li>Quanto custou cada oportunidade?</li></ul><div class="story"><p>Se você não acompanha esses números, você está administrando o comercial no escuro.</p><p>A Maleta coloca os principais indicadores do escritório em um só lugar.</p></div>',
    '7 peças para transformar números em decisões.', GE,
    'Você deixa de olhar apenas para o faturamento e passa a entender o que está gerando o faturamento.')

a = h.index('<!-- ================= PALCO 2: DENTRO'); b = h.index('<!-- ================= PLANOS')
stick = h[h.index('<div class="stick">', a):h.index('<div class="comps">', a)]
dentro = f"""<!-- ================= PALCO 2: DENTRO ================= -->
<section class="sec" id="dentro">
  <div class="wrap">
    <div class="head">
      <div class="rv"><div class="eyebrow">O que tem dentro</div><h2 class="h-lg ttl"><span class="hl">23 ferramentas</span> para tirar o seu escritório do improviso.</h2></div>
      <p class="lede rv" data-d="1">Seu escritório não precisa de mais uma coleção de aulas para assistir. Precisa das ferramentas certas para resolver as travas que aparecem todos os dias.</p>
    </div>
    <div class="intro">
      <div class="travas rv"><span>O que postar.</span><span>Como atender.</span><span>Como conduzir uma reunião.</span><span>Como fazer follow-up.</span><span>Como lidar com objeções.</span><span>Como acompanhar os números.</span><span>Como saber onde o dinheiro está sendo perdido.</span></div>
      <div class="por rv" data-d="1"><p>Por isso, a Maleta foi dividida em 3 compartimentos:</p><b>Marketing → Comercial → Gestão</b><p>Cada um resolve uma parte diferente do problema. Role e abra a Maleta.</p></div>
    </div>
    <div class="inside" id="stage2">
      {stick.rstrip()}
      <div class="comps">
{comps}      </div>
    </div>
    <div class="fecho rv">
      <div class="tres"><div><b>Marketing</b>para gerar demanda e ter uma presença no digital.</div><div><b>Comercial</b>para transformar demanda em contratos.</div><div><b>Gestão</b>para saber o que está funcionando.</div></div>
      <h3 class="ttl">Uma estrutura completa para tirar o escritório do improviso.</h3>
      <div class="abra">Abra a Maleta.</div>
    </div>
  </div>
</section>

"""
h = h[:a] + dentro + h[b:]

css2 = """
/* o que tem dentro, v2: intro com as travas, compartimentos com fala, peças descritas e resultado */
.intro{display:grid;grid-template-columns:1.1fr .9fr;gap:28px 64px;align-items:start;margin:-8px 0 clamp(36px,5vw,56px)}
.travas{display:grid;grid-template-columns:1fr 1fr;gap:10px 28px;border-top:1px solid var(--hair-2);padding-top:22px}
.travas span{font-size:.97rem;color:var(--t-2);padding-left:18px;position:relative;line-height:1.4}
.travas span::before{content:"";position:absolute;left:0;top:.7em;width:8px;height:1px;background:var(--o)}
.intro .por{display:flex;flex-direction:column;gap:12px;border-top:1px solid var(--hair-2);padding-top:22px}
.intro .por p{font-size:1rem;line-height:1.55;color:var(--t-2)}
.intro .por b{font-family:var(--ffd);font-weight:700;font-size:clamp(1.3rem,2vw,1.7rem);letter-spacing:-.025em;color:#fff}
.comp .top h3 small{display:block;font-size:.64rem;font-weight:600;letter-spacing:.3em;margin-bottom:8px;background:var(--og);-webkit-background-clip:text;background-clip:text;color:transparent;width:max-content}
.comp .quote{font-family:var(--ffd);font-weight:600;font-size:1.3rem;letter-spacing:-.02em;line-height:1.25;color:#fff;max-width:32ch}
.comp .story{display:flex;flex-direction:column;gap:8px}
.comp .story p{font-size:.97rem;line-height:1.5;color:var(--t-2);max-width:56ch}
.comp .qs{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:6px 20px}
.comp .qs li{font-size:.92rem;color:var(--t-3);padding-left:16px;position:relative;line-height:1.4}
.comp .qs li::before{content:"";position:absolute;left:0;top:.7em;width:8px;height:1px;background:var(--o)}
.comp h4{font-family:var(--ffd);font-weight:600;font-size:1.08rem;letter-spacing:-.015em;color:#fff;margin-top:6px}
.comp .items{align-items:start}
.comp .it{align-items:flex-start;padding:12px 14px 12px 10px;gap:12px}
.comp .it img{width:40px;height:40px}
.comp .it div{display:flex;flex-direction:column;gap:3px}
.comp .it b{font-size:.9rem;font-weight:600;color:#fff;line-height:1.3}
.comp .it span{font-size:.8rem;line-height:1.4;color:var(--t-3)}
.comp .res{display:flex;flex-direction:column;gap:6px;padding:4px 0 4px 18px;border-left:2px solid var(--o);font-size:1rem;line-height:1.5;color:#fff;font-weight:500;max-width:52ch}
.comp .res small{font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--t-3);font-weight:600}
.fecho{margin-top:clamp(24px,3vw,40px);text-align:center;display:flex;flex-direction:column;align-items:center;gap:28px}
.fecho .tres{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;width:100%;border-top:1px solid var(--hair-2);border-bottom:1px solid var(--hair-2);padding:28px 0}
.fecho .tres div{font-size:.97rem;line-height:1.5;color:var(--t-2);padding:0 16px}
.fecho .tres b{display:block;font-family:var(--ffd);font-size:1.25rem;font-weight:700;color:#fff;margin-bottom:6px;letter-spacing:-.02em}
.fecho h3{font-size:clamp(1.8rem,3.6vw,3rem);letter-spacing:-.035em;max-width:20ch;margin-top:10px}
.fecho .abra{font-family:var(--ffd);font-weight:700;font-size:clamp(2rem,5vw,4rem);letter-spacing:-.04em;line-height:1;background:var(--og);-webkit-background-clip:text;background-clip:text;color:transparent}
@media (max-width:900px){
  .intro,.travas,.comp .qs,.fecho .tres{grid-template-columns:1fr}
  .fecho .tres div{padding:0}
}
"""
h = h.replace('/* ---------- mobile ---------- */', css2 + '\n/* ---------- mobile ---------- */', 1)


# ---------- planos: cabeça nova ----------
h = h.replace('<div class="eyebrow rv">Escolha pelo que trava o seu escritório</div>', '<div class="eyebrow rv">Escolha a Maleta pelo que está travando o seu escritório</div>')
h = h.replace('<h2 class="h-lg ttl rv" data-d="1">Cada tamanho resolve <span class="hl">um conjunto de travas.</span></h2>',
              '<h2 class="h-lg ttl rv" data-d="1">Cada plano resolve <span class="hl">um nível diferente de gargalo.</span></h2>')
h = h.replace('<p class="plans-key rv" data-d="2"><span class="hot">Pagamento único, sem mensalidade e sem software para assinar.</span> Leia o que cada plano resolve, escolha o seu e receba tudo no e-mail em seguida.</p>',
              '<p class="plans-key rv" data-d="2"><span class="hot">Acesso vitalício. Pagamento único. Sem mensalidade. Sem software para assinar.</span> Escolha o nível de estrutura que seu escritório precisa e receba acesso imediato à sua Maleta.</p>')

# ---------- garantia + amostra ----------
a = h.index('<div class="two">'); b = h.index('<!-- ================= FAQ')
h = h[:a] + """<div class="two">
      <div class="it rv">
        <div class="eyebrow">Você não precisa acreditar na nossa promessa</div>
        <h3>Abra a Maleta. Teste. Use. <span class="hl">E decida.</span></h3>
        <div class="big">7 dias</div>
        <div class="gl">de garantia</div>
        <p>Você terá 7 dias para abrir os materiais, conhecer a estrutura e começar a aplicar no seu escritório.</p>
        <p>Se depois de testar você entender que a Maleta não faz sentido para o seu momento, basta solicitar o reembolso dentro do prazo. Você recebe 100% do seu investimento de volta.</p>
        <div class="sem"><span>Sem justificativa.</span><span>Sem burocracia.</span><span>Sem ficar preso.</span></div>
        <p class="risco">O risco fica com a gente.</p>
        <a class="btn btn--hot" href="#planos">Quero abrir a Maleta</a>
      </div>
      <div class="it rv" data-d="1">
        <div class="eyebrow">Antes de comprar, teste uma parte</div>
        <h3>Quer saber como é o conteúdo <span class="hl">antes de entrar?</span></h3>
        <p>Vamos te entregar um dos scripts que você encontra dentro da Maleta. <b class="hot">Grátis.</b></p>
        <p>Um script de follow-up desenvolvido para uma das situações que mais fazem escritórios perderem oportunidades: o lead demonstrou interesse, mas parou de responder.</p>
        <p>Deixe seu e-mail. Receba o material gratuitamente. Leia. Aplique. E veja na prática o nível de profundidade da Maleta.</p>
        <form class="form" id="amostra" novalidate>
          <input type="email" name="email" placeholder="seu@email.com" required autocomplete="email">
          <button class="btn btn--hot" type="submit">Quero receber o script</button>
          <span class="ok">Enviado. Confere a caixa de entrada em um minuto.</span>
        </form>
        <p class="depois">Gostou desse? Então imagine ter acesso à estrutura completa. <a href="#planos">Ver os planos</a></p>
      </div>
    </div>
  </div>
</section>

""" + h[b:]

# ---------- fechamento com o contador ----------
a = h.index('<section class="sec final" id="fim">'); b = h.index('<footer>')
h = h[:a] + """<section class="sec final" id="fim">
  <div class="wrap">
    <div class="eyebrow rv">Pare de começar mais uma semana do zero</div>
    <h2 class="h-lg ttl rv" data-d="1">Comece a próxima semana com o marketing e o comercial do seu escritório <span class="hl">estruturados.</span></h2>
    <div class="bigtimer ttl rv" data-d="2" data-timer><b>07</b><s>:</s><b>41</b><s>:</s><b>23</b></div>
    <p class="lede rv" data-d="3">O acesso à Maleta continua. A condição de lançamento, não. Quando o contador chegar a zero, os valores de lançamento serão encerrados.</p>
    <p class="ou rv" data-d="3">Você pode continuar improvisando na próxima semana. Ou pode começar a próxima semana com a <span class="hot">Maleta do Advogado.</span></p>
    <div class="ctas rv" data-d="3">
      <a class="btn btn--hot" href="#planos">Quero abrir a Maleta</a>
    </div>
  </div>
</section>

""" + h[b:]

css3 = """
/* garantia + amostra, v2 */
.two .it .eyebrow{margin-bottom:2px;width:auto;min-width:0;max-width:100%}
.two .gl{font-size:.7rem;font-weight:600;letter-spacing:.28em;text-transform:uppercase;color:var(--t-3);margin-top:-6px}
.two .sem{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:4px}
.two .sem span{font-size:.95rem;font-weight:600;color:#fff;padding-left:16px;position:relative}
.two .sem span::before{content:"";position:absolute;left:0;top:.7em;width:8px;height:1px;background:var(--o)}
.two .risco{font-family:var(--ffd);font-weight:600;font-size:1.2rem;letter-spacing:-.02em;color:#fff}
.two .it .btn{align-self:flex-start;margin-top:6px}
.two .depois{font-size:.9rem;color:var(--t-3)}
.two .depois a{color:#fff;font-weight:600;border-bottom:1px solid var(--o);padding-bottom:1px;margin-left:6px}
/* fechamento, v2 */
.final h2{max-width:22ch;margin:16px auto 0}
.final .bigtimer{margin-top:30px}
.final .ou{margin:22px auto 0;max-width:40ch;font-family:var(--ffd);font-weight:600;font-size:clamp(1.2rem,2vw,1.6rem);line-height:1.3;letter-spacing:-.02em;color:#fff}
"""
h = h.replace('/* ---------- mobile ---------- */', css3 + '\n/* ---------- mobile ---------- */', 1)

# títulos: âncoras param abaixo do header; no celular a maleta que abre deixa de ser fixa e não cobre mais os títulos
h = h.replace('.sec{position:relative;padding:clamp(80px,10vw,140px) 0}', '.sec{position:relative;padding:clamp(80px,10vw,140px) 0;scroll-margin-top:calc(var(--top) - 10px)}')
h = h.replace('  .stick{position:sticky;top:var(--top);height:40vh;height:40svh;background:linear-gradient(180deg,#000 72%,transparent);z-index:3}',
              '  .stick{position:static;height:auto;padding:6px 0 10px}')
h = h.replace("""  const start=vh*.85,end=-(stage2.offsetHeight-vh*.6);
  abre.set(Math.min(1,clamp((start-r.top)/(start-end),0,1)*1.25));""",
              """  if(mob()){const c=$('.stick').getBoundingClientRect();abre.set(clamp((vh*.95-c.top)/(vh*.75),0,1));return}
  const start=vh*.85,end=-(stage2.offsetHeight-vh*.6);
  abre.set(Math.min(1,clamp((start-r.top)/(start-end),0,1)*1.25));""")

# palavras animadas: folga em cima e embaixo na caixa de overflow, senão o topo das letras corta (Inter Tight é mais alta que a linha .96)
old_w = '.w{display:inline-block;overflow:hidden;vertical-align:bottom;padding:0 .02em .1em;margin:0 -.02em -.1em}'
assert old_w in h
h = h.replace(old_w, '.w{display:inline-block;overflow:hidden;vertical-align:bottom;padding:.16em .03em .14em;margin:-.16em -.03em -.14em}')
h = h.replace('.w i{display:inline-block;font-style:normal;transform:translateY(112%);', '.w i{display:inline-block;font-style:normal;transform:translateY(125%);')

# apertar o vazio: entregáveis colam no herói, planos colam nos entregáveis
h = h.replace('<section class="sec" id="dentro">', '<section class="sec" id="dentro" style="padding-top:clamp(24px,4vw,56px)">')
h = h.replace('<section class="sec" id="planos">', '<section class="sec" id="planos" style="padding-top:0">')
open('index.html', 'w', encoding='utf-8').write(h)
print('ok', len(h.splitlines()), 'linhas')
