# Quantum imaging

Imaging a faintly absorbing sample with few photons, such as a cell that light damages, is limited by the random arrival of photons. Light from parametric down-conversion comes in pairs. Counting the partner photons measures that randomness, which can then be subtracted.

Consider one pixel and an object with transmission $t=1-\alpha$. With coherent light, the transmitted count $N_t$ is Poisson distributed with mean $t\bar N$. The estimate $\hat t=N_t/\bar N$ then has variance $t/\bar N$, the shot-noise limit. In twin beams, signal and idler pixel pairs contain equal photon numbers. The idler count $N_i$ therefore tells how many photons entered the sample in the matching signal pixel.

Each photon then survives the object independently with probability $t$. The signal count $N_s$ is binomially distributed given $N_i$, and the ratio $\hat t=N_s/N_i$ has a smaller variance:

```math
\operatorname{Var}\hat t_{\rm coh}=\frac{t}{\bar N},\qquad
\operatorname{Var}\hat t_{\rm twin}=\frac{t(1-t)}{\bar N},\qquad
\frac{\operatorname{Var}\hat t_{\rm twin}}{\operatorname{Var}\hat t_{\rm coh}}=\alpha.
```

Fluctuations in the number of pairs cancel, because they appear equally in both beams. Only the randomness of absorption itself remains. For a sample absorbing $\alpha=1\%$, the variance falls a hundredfold. The same precision is then reached with a hundredth of the photons, an important saving for light-sensitive samples.

Real detectors miss photons. If each beam is detected with efficiency $\eta$, a missed idler is mistaken for an absent photon. The statistic used in experiments is the noise reduction factor. For a transparent region of the sample it becomes

```math
\frac{\operatorname{Var}(N_s-N_i)}{\langle N_s+N_i\rangle}=1-\eta\qquad(t=1),
```

compared with 1 for two independent beams at the shot-noise level. The advantage thus requires high efficiency. Each pixel must also collect both members of most pairs, so pixels must be larger than the coherence area of the down-converted light. That area sets the spatial resolution.

Brida, Genovese and Ruo Berchera demonstrated sub-shot-noise imaging in 2010. They recorded twin beams from parametric down-conversion on a CCD camera, placed a weakly absorbing object in one beam, and subtracted the matching pixels of the other. The object appeared with a larger signal-to-noise ratio than with classical illumination at the same photon number.

Ghost imaging also uses pair correlations. A detector without spatial resolution collects light behind the object, while a camera in the other beam forms the image in coincidence counts. Ghost images can also be formed with classical thermal light at lower visibility, so a ghost image alone is not a signature of quantum correlations. The photon-number difference above is quantum, because classical fields cannot push the noise reduction factor below 1. Quantum metrology treats the same comparison of precision per photon in general form.

## References For The Physical Derivation

- [G. Brida, M. Genovese and I. Ruo Berchera, Experimental realization of sub-shot-noise quantum imaging; twin-beam absorption imaging.](https://arxiv.org/abs/1004.1274)
- [M. Genovese, Real applications of quantum imaging; sub-shot-noise and ghost imaging.](https://arxiv.org/abs/1601.06066)
