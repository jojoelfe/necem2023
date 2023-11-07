---
theme: ./theme
background: /ribomitotubulerender.png
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: slide-left
title: >-
  Workflows for <emph>In-Situ</emph> Structural Biology Using DeCo-LACE and
  cisTEM
mdc: true
layout: cover
---

# *In-situ* and *in-vitro* structure determination using 2DTM in *cis*TEM

Johannes Elferich, Grigorieff Lab


---

# 2D Template Matching

::middle::




<div class="mx-auto">

<p class="text-center font-large">

$\max [($
<img src="/2dtm_template.png" class="inline h-48" />
$\cdot R_{\phi,\theta,\psi})\ast$
<img src="/2dtm_image.png" class="inline h-48 rounded-md shadow-lg mx-2" />
$]$

</p>
<p class="text-center">

$=$
<img src="/2dtm_mip.png" class="mx-auto h-48 rounded-md shadow-lg" />
</p>
</div>

::bottom::
<p class="cite text-right mr-20"><a class="cite" href="https://doi.org/10.7554/eLife.25648" >Rickgauer, J.P., et al. eLife 6:e25648 (2017)
</a></p>
---

# 2DTM in-situ

::middle::

<div class="mx-auto">
<img src="/vis_01.png" class="rounded-md shadow-lg h-112 mx-auto absolute"  />

<img src="/vis_02.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>
<img src="/vis_03.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>

<img src="/vis_04.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>
<img src="/vis_04.png" class="rounded-md shadow-lg h-112 mx-auto" v-after/>

</div>

---

# Reconstruction from 2DTM detections

::middle::

<img src="/cistem_reconstruct3d.png" class="rounded-md shadow-lg h-80 mx-auto" />
<img src="/overall_locres_clipped.png" class="h-80 mx-auto" />


---

# What else could 2DTM used for

- Single particle
  - Maybe fewer images needed
  - Direct selection of "good" particles
  - Start out with good euler angles
  - Sample does not to have to be pure
  - Deterministic
- Lysate vs purified sample
  - Minimize "time to grid"
  - Keep more interaction partners around
  - Purify organelles instead of proteins

---

# Today - Demo using ryanodine receptor

::middle::

<img src="/ryrtitle.png" class="rounded-md shadow-lg h-20 mx-auto" />
<img src="/ryr.jpg" class="h-80 mx-auto" />


---
layout: iframe

# the web page source
url: http://localhost:3000/webgl-ctf/image_abb
---

---

# What about thick samples

::left::

<img src="/indctfs.png" class="h-40 mx-auto" />


::right::

<img src="/integral.png" class="h-40 mx-auto" />


