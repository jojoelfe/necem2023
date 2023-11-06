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

# *In-situ* cryo-EM

::middle::

<div class="mx-20">
<h3 class="text-center">Expectation</h3>

<img src="/goodsell.jpg" class="mx-auto h-48 rounded-md shadow-lg" />

<h3 class="text-center">Reality</h3>

<img src="/trueem.png" class="mx-auto h-48 rounded-md shadow-lg"/>

</div>


<div>
<h3 class="text-center">2D Template Matching</h3>

<p class="text-center">

$\max [($
<img src="/2dtm_template.png" class="inline h-36" />
$\cdot R_{\phi,\theta,\psi})\ast$
<img src="/2dtm_image.png" class="inline h-36 rounded-md shadow-lg mx-2" />
$]$

</p>
<p class="text-center">

$=$
<img src="/2dtm_mip.png" class="mx-auto h-36 rounded-md shadow-lg" />
</p>
</div>

::bottom::
<p class="cite text-right mr-20"><a class="cite" href="https://doi.org/10.7554/eLife.25648" >Rickgauer, J.P., et al. eLife 6:e25648 (2017)
</a></p>
---

# 2DTM for in-situ

::middle::

<div class="mx-auto">
<img src="/vis_01.png" class="rounded-md shadow-lg h-112 mx-auto absolute"  />

<img src="/vis_02.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>
<img src="/vis_03.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>

<img src="/vis_04.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>
<img src="/vis_04.png" class="rounded-md shadow-lg h-112 mx-auto" v-after/>

</div>
---

# What else could 2DTM used for

- Single particle
  - Maybe fewer images needed
  - Direct selection of "good" particles
  - Start out with good euler angles
  - Sample does not to have to be pure
- Lysate vs purified sample
  - Minimize "time to grid"
  - Keep more interaction partners around
  - Purify organelles instead of proteins

---

# Today - Demo using ryanodine receptor

---
layout: iframe

# the web page source
url: http://localhost:3000/webgl-ctf/image_abb
---



---

# cisTEM Preprocessing - CTFfind

::left::

<img src="/ctffind4.png" class="rounded-md shadow-lg" />

::right::

<img src="/ctffind5.png" class="rounded-md shadow-lg" v-click/>

::bottom::

 <a href="https://github.com/GrigorieffLab/cisTEM/tree/je_ctffind_added_to_combined"><logos-github-icon /> GrigorieffLab/cisTEM/tree/ctffind5</a>
<a class="cite mx-4" href=" https://doi.org/10.1016/j.ultramic.2020.113023" >
 Tichelaar W., et al. Ultramicroscopy. 216:113023 (2020)
</a>

---

# Running 2D Template Matching

::middle::

<img src="/mt_start.png" class="rounded-md shadow-lg h-112 mx-auto" />


---

# Running 2D Template Matching

::middle::

<img src="/mt_result.png" class="rounded-md shadow-lg h-112 mx-auto" />

---


# cisTEM 2DTM - Automation with pycistem


::left::
<WindowConsole class="rounded-lg shadow-lg object-cover z-10 ">

```python
from pycistem.programs import unblur

par = unblur.UnblurParameters(
    input_filename="movie.tif",
    output_filename="corrected.mrc"
    gain_filename="gain.dm4",
    pixel_size=0.53,
    output_binning_factor= 3.774,
    exposure_per_frame=0.8)

result = unblur.run(par)  
```

</WindowConsole>

::right::
<WindowConsole class="rounded-lg shadow-lg object-cover z-10 text-sm" v-click>

```bash
> lace_proc import-session /data/elferich/CryoTEM/20230505 \\
  --pixel-size 0.53 --exp-per-frame 0.8

> lace_proc run-unblur --num-cores 400 --cmd-prefix "srun"

> lace_proc run-ctffind --num-cores 400 --cmd-prefix "srun"

> lace_proc run-matchtemplate --template "7cpu_60S.mrc"
```

</WindowConsole>

::bottom::

 <a href="https://github.com/jojoelfe/pycistem"><logos-github-icon /> jojoelfe/pycistem</a>


---



# Molecular localization - Visualize using Blender

::middle::

<div class="mx-auto">
<img src="/vis_01.png" class="rounded-md shadow-lg h-112 mx-auto absolute"  />

<img src="/vis_02.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>
<img src="/vis_03.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>

<img src="/vis_04.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click/>
<img src="/vis_04.png" class="rounded-md shadow-lg h-112 mx-auto" v-after/>

</div>
::bottom::

<a href="https://github.com/BradyAJohnston/MolecularNodes/"><logos-github-icon /> BradyAJohnston/MolecularNodes</a>
<a href="https://github.com/jojoelfe/MolecularNodes/" class="mx-2  "><logos-github-icon /> jojoelfe/MolecularNodes</a>
---


# Brequinar as a treatment for AML

::left::
<div class="flex-wrap flex">
<img src="/breq_mechanism.png" class="mx-auto h-48 rounded-md shadow-lg">
<img src="/cell_cover.jpg" class="mx-auto h-48 rounded-md shadow-lg" />
<img src="/g1655.png" class="mx-auto h-32 mt-4 rounded-md shadow-lg" />
</div>
::right::
<div>
<div class="text-xs" v-click>

|   |   |    |   |
|---|---|---|---|
| **Cells** | THP1 | **Vitrification** | Plunge-freeze |
| **Thinning** | cryo-FIB 150nm |  **TEM acquisition** | Krios 300keV |
| **Pixel size** | 1.06 Å | **Exposure** | 30 $\frac{e}{Å^2}$ |
| **2DTM pixel size** | 2 Å | **2DTM angular sampling** | 2° IP, 3° OP |

</div>
<div class="text-xs mt-20" v-click>

|         | Control           | 24h brequinar  | 48h brequinar | **Total** |
| ------------- |-------------:| -----:| ---:| ---:|
| # Lamellae      | 35 | 15 | 31| 81 | 
| # Micrographs      | 15,612  | 6,423 | 14,008 | 36,043 |
| # 60S Matches | 210,780      | 71,469 | 108,108 | 390,357 |
| 60S Matches / Micrograph | 13.5 | 11.1 | 7.7 | 10.8 |

</div>
</div>
::bottom::

 <p class="cite">
 <a class="cite" href="https://doi.org/10.1111/eci.13366">
 Coelho, A.R., et al. EJCI (2020)
 </a>
 <a class="cite" href="https://doi.org/10.1016/j.cell.2016.08.057">Sykes D.B., et al. Cell 167(1) (2016)
</a></p>
---

# Reconstruction from 2DTM detections

::middle::

<img src="/cistem_reconstruct3d.png" class="rounded-md shadow-lg h-80 mx-auto" />
<img src="/overall_locres_clipped.png" class="h-80 mx-auto" />

---

# Maps from 2DTM detections differ from template

::left::

<SlidevVideo autoPlay="resume"  loop muted  class="rounded-md shadow-lg h-96 mx-auto ">
  <source src="/error1.mp4" type="video/mp4">
</SlidevVideo>

::right::

<SlidevVideo autoPlay="resume" loop muted  class="rounded-md shadow-lg h-96 mx-auto" >
  <source src="/error2.mp4" type="video/mp4">
</SlidevVideo>

---
layout: twocols
---

# Classification of 2DTM detections

::left::

<img src="/overall_crop.png" />

::right::

<img src="/classes.gif" v-click />

---
clicks: 2
---

# Does brequinar affect the elongation cycle?

::middle::

<div class="mx-auto">
<img src="/class1.png" class="absolute h-114" v-click="[0, 1]" />

<img src="/class2.png" class="absolute h-114" v-click="[1, 2]"/>

<img src="/class3.png" class="h-114" v-click="[2, 3]"/>
</div>

---
clicks:1
---

# Translationally inactive class consistent with SERBP1 binding

::middle::

<img src="/brown.jpg" class="rounded-md shadow-lg h-96 mx-auto" />

<div>
<SlidevVideo  muted  class="rounded-md shadow-lg h-96 mx-auto absolute" v-click-hide>
  <source src="/serbp1.mp4" type="video/mp4">
</SlidevVideo>

<SlidevVideo autoPlay="resume" autoPause="click" autoReset="click" muted  class="rounded-md shadow-lg h-96 mx-auto" v-click-after >
  <source src="/serbp1.mp4" type="video/mp4">
</SlidevVideo>
</div>
::bottom::

<p class="cite"><a class="cite" href="https://doi.org/10.7554/eLife.40486" >Brown, A., et al. eLife 7:e40486 (2018)</a></p>


---
layout: twocols
---

# Ribosome degradation by autophagocytosis?

::left::

<h3> Brequinar treatment </h3>


<img src="/br_render.png" class="rounded-md shadow-lg h-96" />

::right::

<h3> Control </h3>


<img src="/C_render.png" class="rounded-md shadow-lg h-96" />



---

# Summary 

- Brequinar treatment changes ribosome levels, but does not appear to change the fraction of actively translating ribosomes
- THP1 cells contain a surprisingly high fraction of translationally inactive ribosomes
- Brequinar treatment appears to induce formation of ribosome-containing phagosome-like structures

<div class="mt-5" />

# Future Directions

- Image CD34+ cells isolated from human umbilical cord blood as a healthy control
- Develop approaches to test for statistical significance of changes in spatial organisation of ribosomal states


---

# Acknowledgements

::left::

<div>
<p class="pi">Niko Grigorieff</p>
<p>Bronwyn Lucas</p>
<p>Ben Himes</p>
<p>Lingli Kong</p>
<p>Steve Diggs</p>
<p>Kexin Zhang</p>
<p>Ximena Zottig</p>
<p class="pi">Tim Grant</p>
<p class="pi">David Sykes</p>
<p>Jelena Milosevic</p>
<p class="pi">UMass Medical School Cryo-EM core:</p>
<p>Chen Xu</p>
<p>Kangkang Song</p>
</div>
::right::

<div>
<img src="/qr-code.png" />
<a href="https://jojoelfe.github.io/necem2023" class="text-center"><logos-github-icon /> jojoelfe.github.io/necem2023</a>
</div>

<style>
  .slidev-layout p {
    @apply leading-5 my-0 !important;
  }
  p.sig {
    @apply font-bold
  }
  p.pi{
    @apply font-bold underline mt-1rem
  }
</style>
