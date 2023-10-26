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
<!-- /nrs/elferich/bern_backup/ER_HoxB8_96h/Assets/Images/Scaled/CF4-g1_00165_-20.0_165 -->
<!-- - Solve structures in thei native environment
- Quantify differences in conformational landscapes
- Quantify differences in complex formation
- Main problem is finding target
- Tomography vs 2DTM
- Data acquisition speed is crucial
-->
---

# Brequinar as a treatment for AML

::left::

<img src="/cell_cover.jpg" class="mx-auto h-96 rounded-md shadow-lg" />


::right::


<img src="/g866.png" class="mx-auto h-32 rounded-md shadow-lg" />
<img src="/g1655.png" class="mx-auto h-32 rounded-md shadow-lg" />

::bottom::
 <p class="cite"><a class="cite" href="https://doi.org/10.1016/j.cell.2016.08.057">Sykes D.B., et al. Cell 167(1) (2016)
</a></p>
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

# Data collected 

::middle::

<div class="px-10">

|   |   |
|---|---|
| **Cells** | THP1 |
| **Vitrification** | Plunge-freeze |
| **Thinning** | TF Acquilos 2 to 150nm |
| **TEM acquisition** | TF Krios 300keV |
| **Pixel size** | 0.53 $\AA$ |
| **Exposure** | 30 $\frac{e}{\AA^2}$ |

</div>

<div class="mx-5">

|         | Control           | 24h brequinar  | 48h brequinar | **Total** |
| ------------- |-------------:| -----:| ---:| ---:|
| # Lamellae      | 35 | 15 | 31| 81 | 
| # Micrographs      | 15,612  | 6,423 | 14,008 | 36,043 |

</div>
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

::middle::

<div class="px-10">

|   |   |
|---|---|
| **Cells** | THP1 |
| **Vitrification** | Plunge-freeze |
| **Thinning** | TF Acquilos 2 to 150nm |
| **TEM acquisition** | TF Krios 300keV |
| **Pixel size** | 0.53 $\AA$ |
| **Exposure** | 30 $\frac{e}{\AA^2}$ |
| **2DTM pixel size** | 2 $\AA$ |
| **2DTM angular sampling** | $2^\circ$ IP, $3^\circ$ OP |

</div>

<div class="mx-5">

|         | Control           | 24h brequinar  | 48h brequinar | **Total** |
| ------------- |-------------:| -----:| ---:| ---:|
| # Lamellae      | 35 | 15 | 31| 81 | 
| # Micrographs      | 15,612  | 6,423 | 14,008 | 36,043 |
| # 60S Matches | 210,780      | 71,469 | 108,108 | 390,357 |
| 60S Matches / micrograph | 13.5 | 11.1 | 7.7 | 10.8 |

</div>


---

# Creating Template Matches Package

::middle::

<img src="/mt_package.png" class="rounded-md shadow-lg h-112 mx-auto" />

---
clicks:1
---

# Molecular localization - Visualize using Blender

::middle::


<SlidevVideo autoPlay="resume" autoPause="click" autoReset="click" muted  class="rounded-md shadow-lg h-112 mx-auto" >
  <source src="/blender_workflow2.mp4" type="video/mp4">
</SlidevVideo>




::bottom::

<a href="https://github.com/BradyAJohnston/MolecularNodes/"><logos-github-icon /> BradyAJohnston/MolecularNodes</a>
<a href="https://github.com/jojoelfe/MolecularNodes/"><logos-github-icon /> jojoelfe/MolecularNodes</a>
---

# Molecular localization - Visualize using Blender

<img src="/ribomitotubulerender.png" class="rounded-md shadow-lg h-112 mx-auto" />

---

# cisTEM - Convert to a single-particle project

::middle::

<img src="/cistem_refinement.png" class="rounded-md shadow-lg h-112 mx-auto" />
---

# cisTEM - Reconstructed Matches

::middle::

<img src="/cistem_reconstruct3d.png" class="rounded-md shadow-lg h-92 mx-auto" />
<img src="/overall_locres_clipped.png" class="h-92 mx-auto" />

---

# cisTEM - Template Bias?

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

# cisTEM - Classification

::left::

<img src="/overall_crop.png" />

::right::

<img src="/classes.gif" />

---
clicks: 2
---

# Does the drug affect the elongation cycle?

::middle::

<div class="mx-auto">
<img src="/class1.png" class="absolute h-114" v-click="[0, 1]" />

<img src="/class2.png" class="absolute h-114" v-click="[1, 2]"/>

<img src="/class3.png" class="h-114" v-click="[2, 3]"/>
</div>

---
clicks:1
---

# SERBP1 is bound to EF2 inactive class

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

# Degradation in autophagosomes?

::left::

<h3> Brequinar treatment </h3>

<div class="grid grid-cols-2 gap-4">

<img src="/render001.png" class="rounded-md shadow-lg" />
<img src="/render005.png" class="rounded-md shadow-lg" />
<img src="/render004.png" class="rounded-md shadow-lg" />
<img src="/render003.png" class="rounded-md shadow-lg" />
</div>

::right::

<h3> Control </h3>

<div class="grid grid-cols-2 gap-4">

<img src="/crender001.png" class="rounded-md shadow-lg" />
<img src="/crender002.png" class="rounded-md shadow-lg" />
<img src="/crender003.png" class="rounded-md shadow-lg" />
<img src="/crender004.png" class="rounded-md shadow-lg" />
</div>


---

# Summary future directions

- Brequinar treatment changes ribosome levels, but does not appear to change the fraction of actively translating ribosomes
- THP1 cells contain a surprisingly high fraction of translationally inactive ribosomes
- Brequinar treatment appears to induce formation of ribosome-containing phagocytic structures

<div class="mt-5" />

# Future Directions

- We are planning to compare these results to CD34+ cells isolated from human umbilical blood
- We are working on developing approaches to test for statistically significant changes in spatial orientation of ribosomal states


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
