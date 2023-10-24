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

# Workflows for *In-Situ* Structural Biology <br /> Using DeCo-LACE and *cis*TEM

Johannes Elferich, Grigorieff Lab


---
layout: twocols
---

# *In-situ* cryo-EM

::left::

<h3 class="text-center">Expectation</h3>

<img src="/goodsell.jpg" class="mx-auto h-48 rounded-md shadow-lg" />

<h3 class="text-center">Reality</h3>

<img src="/trueem.png" class="mx-auto h-48 rounded-md shadow-lg"/>
 
::right::

<h3 class="text-center mt--10">Tomography</h3>

<img src="/cryoet.png" class="mx-auto h-32 rounded-md shadow-lg" />

<p class="cite text-right"><a class="cite" href="https://doi.org/10.1038/s41586-022-05255-2" >Xue, L., et al. Nature 610, 205–211 (2022)</a></p>

<h3 class="text-center">2D Template Matching</h3>

<p class="text-center">

$\max [($
<img src="/2dtm_template.png" class="inline h-24" />
$\cdot R_{\phi,\theta,\psi})\ast$
<img src="/2dtm_image.png" class="inline h-24 rounded-md shadow-lg mx-2" />
$]$

</p>

<img src="/2dtm_mip.png" class="mx-auto h-24 rounded-md shadow-lg" />
<p class="cite text-right"><a class="cite" href="https://doi.org/10.7554/eLife.25648" >Rickgauer, J.P., et al. eLife 6:e25648 (2017)
</a></p>
<!-- /nrs/elferich/bern_backup/ER_HoxB8_96h/Assets/Images/Scaled/CF4-g1_00165_-20.0_165 -->
<!-- - Solve structures in thei native environment
- Quantify differences in conformational landscapes
- Quantify differences in complex formation
- Main problem is finding target
- Tomography vs 2DTM
- Data acquisition speed is crucial
-->

---

# Defocus Corrected Large-Area Cryo-EM (DeCo-LACE)

::middle::

<img src="/init.png" class="inline h-90 rounded-md shadow-lg mx-2" />
<img src="/approach.png" class="inline h-90 rounded-md shadow-lg mx-2" />
<img src="/deco_result.jpg" class="inline h-90 rounded-md shadow-lg mx-2" />

<!-- - Lamellae preparation is slow (Do not waste area)
- Hard to know where rare events are from overview (CLEM)
- Approach: Image everything as fast as possible
-->

::bottom::

<p class="cite"><a class="cite" href=" https://doi.org/10.7554/eLife.80980" >Elferich, J., et al. eLife 11:e80980 (2022)
</a></p>

---
clicks: 2
---

# Data acquisition using DeCo-LACE

::left::

<img src="/lamella.png" class="rounded-md shadow-lg absolute" v-click="[0, 1]" />

<img src="/lamella_setup.png" class="rounded-md shadow-lg absolute" v-click="[1, 2]"/>

<img src="/lamella_exposures.png" class="rounded-md shadow-lg" v-click="[2, 3]"/>

::right::

<img src="/Figure_1.svg" />

::bottom::

 <a href="https://github.com/jojoelfe/decolace"><logos-github-icon /> jojoelfe/decolace</a>

---
---

# cisTEM Preprocessing - CTFfind

::left::

<img src="/ctffind4.png" class="rounded-md shadow-lg" />

::right::

<img src="/ctffind5.png" class="rounded-md shadow-lg"/>

::bottom::

 <a href="https://github.com/GrigorieffLab/cisTEM/tree/je_ctffind_added_to_combined"><logos-github-icon /> GrigorieffLab/cisTEM/tree/ctffind5</a>


---

# Running 2D Template Matching

::middle::

<img src="/mt_start.png" class="rounded-md shadow-lg h-112 mx-auto" />


---

# Running 2D Template Matching

::middle::

<img src="/mt_result.png" class="rounded-md shadow-lg h-112 mx-auto" />

---
layout: twocols
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
<WindowConsole class="rounded-lg shadow-lg object-cover z-10 text-sm">

```bash
> lace_proc import-session /data/elferich/CryoTEM/20230505 --pixel-size 0.53 --exp-per-frame 0.8

> lace_proc run-unblur --num-cores 40 --cmd-prefix "srun"

> lace_proc run-ctffind --num-cores 40 --cmd-prefix "srun"

> lace_proc run-matchtemplate --template "7cpu_60S.mrc"
```

</WindowConsole>

::bottom::

 <a href="https://github.com/jojoelfe/pycistem"><logos-github-icon /> jojoelfe/pycistem</a>

---

# Data collected 

|         | Control           | 24h brequinar  | 48h brequinar | **Total** |
| ------------- |-------------:| -----:| ---:| ---:|
| # Lamellae      | 35 | 15 | 31| 81 | 
| # Micrograph      | 15,612  | 6,423 | 14,008 | 36,043 |
| # 60S Matches | 210,780      | 71,469 | 108,108 | 390,357 |
| 60S Matches / micrograph | 13.5 | 11.1 | 7.7 | 10.8 |

---

# Creating Template Matches Package

::middle::

<img src="/mt_package.png" class="rounded-md shadow-lg h-112 mx-auto" />

---
clicks:2
---

# Molecular localization - Visualize using Blender

::middle::

<div class="mx-auto">
<img src="/blender_start.png" class="rounded-md shadow-lg h-112 mx-auto absolute" v-click="[0, 1]" />
<SlidevVideo autoPlay="resume" autoPause="click" autoReset="click" muted  class="rounded-md shadow-lg h-112" v-click="[1, 3]">
  <source src="/blender_workflow.webm" type="video/webm">
  Download the <a href="/flower.webm">WEBM</a>
</SlidevVideo>
</div>



::bottom::

<a href="https://github.com/BradyAJohnston/MolecularNodes/"><logos-github-icon /> BradyAJohnston/MolecularNodes</a>
<a href="https://github.com/jojoelfe/MolecularNodes/"><logos-github-icon /> jojoelfe/MolecularNodes</a>
---

# Molecular localization - Visualize using Blender

<img src="/ribomitotubulerender.png" class="rounded-md shadow-lg h-112 mx-auto" />

---

# cisTEM - Convert to a single-particle project

---

# cisTEM - Reconstruction and Template Bias

---
layout: twocols
---

# cisTEM - Classification

::left::

<img src="/overall_crop.png" />

::right::

<img src="/classes.gif" />

---

# Does the drug affect the elongation cycle?

<img src="/class_perc.png" class="h-96"/>

---
layout: twocols
---

# SERBP1 is bound to EF2 inactive class

::left::

<img src="/serbp1_helix.png" />

::right::

<img src="/serbp1_zoom.png" />

---
layout: twocols
---

# Degradation in autophagosomes?

::left::

<div class="grid grid-cols-2 gap-4">

<img src="/render001.png" class="rounded-md shadow-lg" />
<img src="/render005.png" class="rounded-md shadow-lg" />
<img src="/render004.png" class="rounded-md shadow-lg" />
<img src="/render003.png" class="rounded-md shadow-lg" />
</div>

---

# Future directions

- Analyze ribosome states in primary CD34+ precursors


---

# Acknowledgements

::left::

<p class="pi">Niko Grigorieff</p>
<p>Bronwyn Lucas</p>
<p>Ben Himes</p>
<p>Lingli</p>
<p>Steve Diggs</p>
<p>Kexin</p>
<p class="pi">Tim Grant</p>
<p class="pi">David Sykes</p>
<p>Jelena Milosevic</p>
<p class="pi">UMass Medical School Cryo-EM core:</p>
<p>Chen Xu</p>
<p>Kangkang Song</p>


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
