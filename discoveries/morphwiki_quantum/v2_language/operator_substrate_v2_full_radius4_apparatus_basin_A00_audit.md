# V2 Apparatus Basin Audit: `A00`

- Readiness: `usable`
- Target cluster: `4`
- Target total rows: `6151464` (0.4235)
- Alignment rows seen: `2420388`
- Decision: `weak_abelian_surface_enrichment_without_closure_support`

## Target Signature

- `A:Ω_readout_closure_spectral-Ξ_diffuse-R_mixed-Γ_lo`

## Aligned Support

- Target aligned rows: `1340624`
- Control aligned rows: `1079764`
- Target math-like rate: `1.0000`
- Target prose-like rate: `0.0000`

## Marker Enrichment

- `abelian_commutative`: target `0.0142`, control `0.0094`, enrichment `1.518`
- `prose_noise`: target `0.0004`, control `0.0003`, enrichment `1.411`
- `commutator_bracket`: target `0.2314`, control `0.2294`, enrichment `1.009`
- `linear_superposition`: target `0.1012`, control `0.1312`, enrichment `0.771`
- `differential_transport`: target `0.0240`, control `0.0391`, enrichment `0.615`
- `closure_constraint`: target `0.0004`, control `0.0012`, enrichment `0.299`
- `spectral_diagonal`: target `0.0180`, control `0.1315`, enrichment `0.137`
- `readout_observable`: target `0.0034`, control `0.0410`, enrichment `0.082`

## Interpretation

The target basin has weak enrichment for explicit Abelian/commutative surface markers, but closure, spectral and readout surface markers are not enriched. It should not be called a closure-preserving or spectral/readout Abelian cluster from this audit alone.

## Examples

### `commutator_bracket`

- `0712.3304` score `0.833333`: `x_{u, \\alpha} = (1/2) n_{u, \\alpha}/n`
  - matched `equation_preview` via `\{[^\}]+,[^\}]+\}`: `x_{u, \alpha} = (1/2) n_{u, \alpha}/n`
- `2102.05093` score `0.611111`: `M_{1,i}=\\frac{12B_{i}L_{i}^{4}}{\\pi^{4}}`
  - matched `equation_preview` via `\{[^\}]+,[^\}]+\}`: `m_{1,i}=\frac{12b_{i}l_{i}^{4}}{\pi^{4}}`
- `1611.00588` score `0.666667`: `r_1 = \\overline{r}_1 -1`
  - matched `subject_preview` via `\{[^\}]+,[^\}]+\}`: `= sum_{h=1}^q overline{ theta}_h b_h + sum_{h=1}^q ( sum_{j=1}^s 2 pi l_j beta_{j,h}) b_h = sum_{h=1}^q ( overline{ theta}_h +2 pi overline{r}_h)b_h`
- `astro-ph9810122` score `1.0`: `t_{1} < t_{p}`
  - matched `object_preview` via `\{[^\}]+,[^\}]+\}`: `\nc_{p} > c_{1,2}+ alpha sqrt{c_{p}+c_{1,2}}\n`
- `2501.10030` score `0.571429`: `\ \n\t\t{H_1^{mos}(\\{{x_{i}^{[0,{T_i-L}]}\\}_{i=1}^p})}\\\\\n\t\t{H_L^{mos}(\\{{u_{i}^{[0,{T_i-1}]}\\}_{i=1}^p})}\n\t\`
  - matched `equation_preview` via `\[[^\]]+,[^\]]+\]`: `\ \n\t\t{h_1^{mos}(\{{x_{i}^{[0,{t_i-l}]}\}_{i=1}^p})}\\\n\t\t{h_l^{mos}(\{{u_{i}^{[0,{t_i-1}]}\}_{i=1}^p})}\n\t\`

### `linear_superposition`

- `1611.00588` score `0.666667`: `r_1 = \\overline{r}_1 -1`
  - matched `subject_preview` via `\bsum_`: `a = sum_{h=1}^q overline{ theta}_h b_h + sum_{h=1}^q ( sum_{j=1}^s 2 pi l_j beta_{j,h})`
- `1802.04838` score `0.9`: `\\|a_{m.}\\|_1 = \\|a_{m.}\\|_{1+} + \\|a_{m.}\\|_{1-}`
  - matched `object_preview` via `\bsum_`: `|a |_{p,q}=( sum_m |a_{m.} |_q^p)^{ frac{1}{p}}`
- `2005.13988` score `1.0`: `Z_{x,y}=Z_{y}+z_{x,y}`
  - matched `object_preview` via `\bsum_`: `split n=10000= sum_{x}n_{x} total size to these 50 multinomial`
- `1511.06461` score `0.615385`: `\\sum_{n=1}^{\\infty}t_{n} = \\infty`
  - matched `equation_preview` via `\bsum_`: `\sum_{n=1}^{\infty}t_{n} = \infty`
- `1610.02766` score `0.5625`: `\\sum_{i=0}^{r-1} X_i (x) = \\eta^{B_{2^r} (x)} (x)`
  - matched `equation_preview` via `\bsum_`: `\sum_{i=0}^{r-1} x_i (x) = \eta^{b_{2^r} (x)} (x)`

### `spectral_diagonal`

- `2012.01436` score `0.6875`: `\n U(T) = (U_0)^{\\Omega T/2 \\pi}.\n\`
  - matched `object_preview` via `\btr\b`: `text{sff} = overline{| text{tr}[u(t)]|^2}`
- `dg-ga9710035` score `0.615385`: `\\Omega ^p_{B/A}= \\Lambda ^p_B \\Omega _{B/A}`
  - matched `equation_preview` via `\\lambda\b`: `\omega ^p_{b/a}= \lambda ^p_b \omega _{b/a}`
- `2002.00050` score `0.666667`: `x_1=\\frac{1}{1+(u+u^q)^{q-1}}`
  - matched `subject_preview` via `\btr\b`: `tr left( frac{1}{v_1^{ frac{1}{q-1}}} right)=tr left( frac{1}{v_2^{ frac{1}{q-1}}}`
- `1201.1022` score `1.0`: `Q=Q_s=x^3+axyz+bxz^2+cyz^2+dz^3`
  - matched `object_preview` via `\bdet\b`: `r=r(k,l,m):= det(d^2(q_e))=3k^2mp+9km^2q-3kl^2-m^3p^2`
- `1403.0807` score `0.631579`: `\n\\Cc_k\\colon v^\\ell=u(u+1)^{\\ell-k-1}\\,.\n`
  - matched `subject_preview` via `\btr\b`: `\n tr v_{ ell\'}( cc_k)( frob_p)=0\n`

### `differential_transport`

- `math0601526` score `1.0`: `f_{vv}(x)=0`
  - matched `subject_preview` via `\bpartial_`: `partial_v^2( a\nh)(x_0,t_0)=0`
- `2412.05458` score `0.692308`: `q_\\mu^{\\pm} = q_\\mu^1 \\pm i q_\\mu^2`
  - matched `object_preview` via `\bpartial_`: `q_{ mu nu}^3 = partial_ mu q_ nu^3`
- `1407.0259` score `0.857143`: `F_{Bu}=\\partial_B A_u-\\partial_u A_B = O(1)`
  - matched `equation_preview` via `\bpartial_`: `f_{bu}=\partial_b a_u-\partial_u a_b = o(1)`
- `0911.4608` score `0.703704`: `\nE_{BR}(\\vec{q},k)=\\frac{1}{4M}\\, q^{2}+\\frac{u_{1}(k)}{Z_{\\phi}(k)}\n+\\frac{R_{B}(q,k)}{Z_{\\phi}(k)}\`
  - matched `subject_preview` via `\bpartial_`: `partial_{k}u_{2}|_{b}= frac{u_{2}^{2}(k)}{2z_{ phi}^{3}(k)}`
- `1206.3856` score `0.684211`: `\\forall e\',\\quad\\partial_{e\'} i^{u,v}_r(e\')=\\frac{i^{u,v}_r(e\')}{r(e\')}j(e\')=\\frac{i^{u,v}_r(e\')}{r(e\')}(i^{e\'}_r(e\')-1)\\`
  - matched `equation_preview` via `\bpartial_`: `\forall e\',\quad\partial_{e\'} i^{u,v}_r(e\')=\frac{i^{u,v}_r(e\')}{r(e\')}j(e\')=\frac{i^{u,v}_r(e\')}{r`

### `abelian_commutative`

- `1609.08601` score `0.625`: `[\\xi_1,\\xi_3]=\\xi_2`
  - matched `subject_preview` via `\[ *[^\]]+ *, *[^\]]+ *\] *= *0`: `[ xi_2, xi_3]= 0`
- `1710.04084` score `1.0`: `y_{1,1}=1`
  - matched `subject_preview` via `\{ *[^\}]+ *, *[^\}]+ *\} *= *0`: `y_{1,1}=1 , y_{1,2}=0 , y_{2,1}`
- `2105.09516` score `0.583333`: `P_{O, 4}=0.13`
  - matched `equation_preview` via `\{ *[^\}]+ *, *[^\}]+ *\} *= *0`: `p_{o, 4}=0.13`
- `0810.3148` score `0.55`: `\n Y_3=X_{-\\lambda_1}+X_{-\\lambda_2}-X_{-\\lambda_3}+ X_{-\\lambda_4}`
  - matched `subject_preview` via `\[ *[^\]]+ *, *[^\]]+ *\] *= *0`: `[x_2,ad(a_1)^2(x_2)]=[x_2,[a_1,x_1]]=-[x_2,[x_1,a_1]]=\n-[x_1,[x_2,a_1]]=[x_1,x_1]=0`
- `0803.0244` score `0.5625`: `b^K=\\sum_{k=0}^K \\sum_{l=0}^{m_k-1} b_{k,l}B^{k,l}`
  - matched `object_preview` via `\{ *[^\}]+ *, *[^\}]+ *\} *= *0`: `0, tilde b_{k,l}=0 hbox{otherwise}`

### `prose_noise`

- `1001.2554` score `1.0`: `we consider \\\\ Q_c=(1-(x_1-c)^{q-1})P`
  - matched `equation_preview` via `\bwe\b`: `we consider \\ q_c=(1-(x_1-c)^{q-1})p`
- `0812.0443` score `1.0`: `{anneal-1}\n\\{\\check{X}_n(z),\\ z\\in \\Z^d\\}\\stackrel{Q-\\text{law}}{=}\n\\{X_n(z),\\ z\\in \\Z^d\\}\\quad\\text{where}\\quad\nX_n(z)=q_n^2(z)-l_n(z).\n\`
  - matched `equation_preview` via `\bwhere\b`: `_n(z),\ z\in \z^d\}\stackrel{q-\text{law}}{=}\n\{x_n(z),\ z\in \z^d\}\quad\text{where}\quad\nx_n(z)=q_n^2(z)-l_n(z).\n\`
- `astro-ph0308143` score `1.0`: `4.3 ). Remarkably, the difference in the \nnormalization between observation and theory is quite similar to that found \nin the study of B335, a core that is likely associated with the same parent\nmolecular cloud as...`
  - matched `equation_preview` via `\bthe\b.*\bis\b`: `4.3 ). remarkably, the difference in the \nnormalization between observation and theory is quite similar to that found \nin the study of b335, a core that is likely associated with the same parent\nmolecular cloud as...`
- `1803.04995` score `0.685714`: `\nI_1&=&I_1^{out}-I_1^{in}=\\frac{e^2}{h}[(T_1(3 - 2 f + f^2 (-2 + R_1) R_1)/a^2)V_1\ \\\\&-&T_1V''_{1}-(T_1(1-f)/a^2+R_1 T_1 (1 - f) f/a^2)(V'_1+V'_{6})]\ \\\\ \\qquad\\text{with }& & I_4=-I_1, \\text{where a=1-R_1f...`
  - matched `equation_preview` via `\bwhere\b`: `+r_1 t_1 (1 - f) f/a^2)(v'_1+v'_{6})]\ \\ \qquad\text{with }& & i_4=-i_1, \text{where a=1-r_1f...`
- `1102.0366` score `1.0`: `the relations\n\\bes\nh_{x_i}f=[h_{x_i},f]+fh_{x_i}, h_{y_i}f=[h_{y_i},f]+fh_{y_i},\n\\ees\nand multinomial coefficients, we get\n\\bes\n\\frac{1}{\\g!}h^{\\g}f=\\sum_{\\a+\\b=\\g}\n\\frac{1}{\\a!\\b!} H^{\\a}(f) h^{\...`
  - matched `equation_preview` via `\bwe\b`: `]+fh_{x_i}, h_{y_i}f=[h_{y_i},f]+fh_{y_i},\n\ees\nand multinomial coefficients, we get\n\bes\n\frac{1}{\g!}h^{\g}f=\sum_{\a+\b=\g}\n\frac{1}{\a!\b!} h^{\a}(f) h^{`

### `readout_observable`

- `1711.11389` score `0.55`: `=\\langle \\alpha,\\beta|[(\\alpha\\beta^{n-k+1}\\alpha\\beta^{-n+k})^{n+k}(\\alpha\\beta)^{-2k+1}\\beta^{-n+k-1}]^{m+1}=\\alpha\\beta^{n-k+1}\\alpha\\beta^{-n+k}\\rangle.\`
  - matched `equation_preview` via `\\langle`: `=\langle \alpha,\beta|[(\alpha\beta^{n-k+1}\alpha\beta^{-n+k})^{n+k}(\alpha\beta)^{-2k+1`
- `2306.08654` score `0.571429`: `\\langle q, x\\rangle:=\\frac{1}{2}(\\bar q x + \\bar x q) = \\frac{1}{2}(q \\bar x + x \\bar q)`
  - matched `equation_preview` via `\\langle`: `\langle q, x\rangle:=\frac{1}{2}(\bar q x + \bar x q) = \frac{1}{2}(q \bar x + x \bar q`
- `1003.5379` score `0.6`: `\\langle\\mathcal{J}(x_2)x_1,x_1\\rangle=A(x_1,x_2,x_2,x_1)=\\alpha`
  - matched `equation_preview` via `\\langle`: `\langle\mathcal{j}(x_2)x_1,x_1\rangle=a(x_1,x_2,x_2,x_1)=\alpha`
- `quant-ph0607134` score `0.607143`: `\n X_{n,m}(E_1,E_2,\\omega,t):=\n \\lim\\limits_{\\xi\\to 0}X_{n,m,\\xi}(E_1,E_2,\\omega,t), \\qquad X=B,B^+,N\n`
  - matched `object_preview` via `\blangle\b`: `n,n\'} dl_{m,m\'} dl(t\'-t) \n times dl(e_1-e_3) dl(e_2-e_4) dl(e_1-e_2- omega) langle g_{n},p_{e_1}g_{n} r`
- `1302.3882` score `0.583333`: `\\langle \\overline{a_2},\\overline{b_2},\\overline{c_2}\\mid \\overline{a_2}\\hspace{1pt}^{2^n}=\\overline{b_2}\\hspace{1pt}^{2^k}=\\overline{c_2}\\hspace{1pt}^2=1,\n\\overline{a_2}\\hspace{1pt}^{\\overline{b_2}}=\\o...`
  - matched `equation_preview` via `\\langle`: `\langle \overline{a_2},\overline{b_2},\overline{c_2}\mid \overline{a_2}\hspace{1pt}^{2^`

### `closure_constraint`

- `cond-mat0406441` score `0.5625`: `u'_{\\v i\\v j}=W_{\\v\ni}u_{\\v i \\v j}W^\\dag_{\\v j}`
  - matched `object_preview` via `\binvariant\b`: `si^ dag_{2 v i}|0 > are invariant under su(2) gauge`
- `1009.5768` score `0.555556`: `\n\\frac{Q^2}{2}&=&(-q_0 p^1 + q_2 q_3)\\ ,\\\\\n\\frac{P^2}{2}&=&(q_1 p^0+ q_2 q_3)\\ ,\\\\\nQ\\cdot P&=& q_0 p^0 - q_1 p^1 + q_1 p^1 + q_2 p^2\\ .\n\`
  - matched `object_preview` via `\binvariant\b`: `4d duality invariant is given by i_4= 4 p^0 q_1 q_2 q_3`
- `2305.19647` score `0.6`: `A= A-\\overline{(X-A)}^{\\mathcal{I}^{*}}`
  - matched `object_preview` via `\bclosed\b`: `assertions are equivalent:\n\n(i) a is mathcal{i}^{*} - closed.\n\n(ii) a= bigcap lbrace f:f text{ is } mathcal{i}^{*}- tex`
- `1108.2005` score `0.5625`: `d\\eta_{k_1,k_2}=\\pi^*\\gro_{k_1,k_2}`
  - matched `object_preview` via `\bprojection\b`: `s^2 is natural projection defines a contact structure cald_{k_1,k_2}= ker eta_{k_1,k_2} on m^5_{k_1,k_2}`
- `cond-mat0406028` score `0.818182`: `\\mbox{[open]}/\\mbox{[closed]}=a^N`
  - matched `equation_preview` via `\bclosed\b`: `\mbox{[open]}/\mbox{[closed]}=a^n`

## Scope

Enrichment audit for a derived V2 apparatus basin using source-card/V2-row alignments. It tests whether the target basin is enriched for marker families; it does not prove physical equivalence or that all rows in the basin are Abelian mechanisms.
