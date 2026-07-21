---
title: "RaLiBEV — Radar and LiDAR BEV Fusion"
excerpt: "Anchor-box-free radar and LiDAR birds-eye-view fusion for all-weather 3D object detection. Published in IEEE TCSVT, 2025."
collection: projects
permalink: /projects/ralibev
---

**RaLiBEV** fuses radar range-azimuth heatmaps with LiDAR point clouds in a bird's-eye-view representation, using an interactive transformer-based fusion module and a consistency-aware label assignment strategy for anchor-box-free detection.

Radar penetrates rain and fog where LiDAR degrades, so fusing the two yields robust detection in adverse weather — outperforming prior methods by 13.1% (clear) and 19.0% (foggy) at IoU 0.8.

Published in *IEEE Transactions on Circuits and Systems for Video Technology*, 35(5):4130–4143, 2025.

[Code](https://github.com/yyxr75/RaLiBEV) &middot; [arXiv:2211.06108](https://arxiv.org/abs/2211.06108) &middot; [IEEE Xplore](https://ieeexplore.ieee.org/document/10812016/)
