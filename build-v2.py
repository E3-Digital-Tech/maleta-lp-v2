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
      <h1 class="h-mega ttl">Tudo o que o seu escritório precisa para <span class="hl">vender,</span> <span class="hl">dentro de uma maleta.</span></h1>
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
h = h.replace('Sem mensalidade e sem software para assinar. Você escolhe o tamanho, paga uma vez e recebe tudo no e-mail em seguida.',
              'Pagamento único, sem mensalidade e sem software para assinar. Leia o que cada plano resolve, escolha o seu e receba tudo no e-mail em seguida.')

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

# apertar o vazio: entregáveis colam no herói, planos colam nos entregáveis
h = h.replace('<section class="sec" id="dentro">', '<section class="sec" id="dentro" style="padding-top:clamp(24px,4vw,56px)">')
h = h.replace('<section class="sec" id="planos">', '<section class="sec" id="planos" style="padding-top:0">')
open('index.html', 'w', encoding='utf-8').write(h)
print('ok', len(h.splitlines()), 'linhas')
