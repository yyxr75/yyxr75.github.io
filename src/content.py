"""All site content. Edit here, then run `python3 src/build.py`."""

NAME = "Yanlong Yang"
EMAIL = "yanlong.yang@my.jcu.edu.au"
SCHOLAR = "https://scholar.google.com/citations?user=aMDjXZEAAAAJ"
GITHUB = "https://github.com/yyxr75"
ORCID = "https://orcid.org/0009-0000-8870-5993"
CV_PDF = "/files/CV_YanlongYang.pdf"

TAGLINE = "I build deep-learning perception for autonomous driving, generative models for inverse problems, and the systems that put them to work in the field — from radar signal chains and data pipelines to a crocodile-detection system for the Queensland Government."

BIO = [
    'I am a PhD candidate in Engineering at <a href="https://www.jcu.edu.au/">James Cook University</a>, Cairns, advised by <a href="https://research.jcu.edu.au/portfolio/tao.huang1/">Dr Tao Huang</a> in the <a href="https://www.taoicclab.com/">Intelligent Computing &amp; Communications Lab</a> (expected completion Oct 2027).',
    'I work across the whole stack of AI for perception. At Vanjee Technology in Beijing I spent four years as an algorithm engineer on autonomous and vehicle–road cooperative driving: 3D object detection and radar–LiDAR fusion, the MIMO radar signal chain underneath them, and a data closed-loop system I led to keep models improving after deployment — with nine granted patents along the way.',
    'In my PhD I develop generative models for inverse problems — diffusion priors that super-resolve sparse radar without paired data, and self-diffusion methods that recover images through unknown blur with no pre-training (first author, CVPR 2026) — and I am extending them toward world models for driving. I also build applied systems end to end: computer vision deployed for crocodile monitoring with the Queensland Government, and a public data platform for Australian skilled migration.',
    'My background in opto-electronics and hardware — optics, THz spectroscopy, PCB design and multi-sensor rigs — means I am comfortable from the sensor and the signal all the way up to the model and the product.',
]

# Home "What I do" pillars: (title, one-liner, skills, [project slugs])
PILLARS = [
    ("Autonomous-driving perception", "Deep learning for 3D detection, radar–LiDAR fusion and tracking, from research models to production pipelines.",
     ["PyTorch", "3D detection", "BEV fusion", "point clouds", "world models"], ["ralibev", "data-closed-loop", "world-models"]),
    ("Generative models &amp; inverse problems", "Diffusion priors and self-diffusion for recovering clean images and point clouds from degraded, incomplete data.",
     ["diffusion models", "self-supervised learning", "blind deconvolution", "super-resolution"], ["deblursdi", "radarinv", "self-diffusion"]),
    ("Applied AI &amp; systems", "Taking models into the field and building the systems around them — data loops, deployment, and full products.",
     ["deployment", "data pipelines", "team lead", "web &amp; cloud"], ["crocodile-detection", "data-closed-loop", "ausimmitool"]),
    ("Signals &amp; hardware", "Radar signal processing, multi-sensor synchronisation and embedded hardware — the layer the models stand on.",
     ["MIMO radar", "FFT / CFAR / AoA", "ROS", "PCB design", "embedded MCUs"], ["mimo-radar", "thermal-reconstruction", "smart-car"]),
]

INTERESTS = [
    "Deep learning for autonomous-driving perception",
    "Diffusion and generative models for inverse problems",
    "Multi-sensor fusion: radar, LiDAR, camera",
    "3D detection, tracking and point-cloud enhancement",
    "World models",
    "Radar signal processing",
]

STATS = [
    ("CVPR 2026", "first-author paper"),
    ("7", "publications"),
    ("9", "granted patents"),
    ("4 yrs", "industry R&amp;D"),
]

NEWS = [
    ("Aug 2026", 'Launched <a href="/projects/ausimmitool/">ausimmitool.com</a>, a public data site for Australian skilled migration.'),
    ("Jun 2026", '<a href="/projects/deblursdi/">DeblurSDI</a> presented at <strong>CVPR 2026</strong>.'),
    ("2026", "Reviewing for AAAI 2026 and ICLR 2026."),
    ("2025", "Became Cairns Campus Officer, JCU Student Association; represented JCU at the Australian University Student Voice Conference, Gold Coast."),
    ("Oct 2025", '<a href="/projects/self-diffusion/">Self-Diffusion for Solving Inverse Problems</a> released on arXiv.'),
    ("May 2025", '<a href="/projects/radarinv/">RadarINV</a> released on arXiv; <a href="/projects/ralibev/">RaLiBEV</a> published in <em>IEEE TCSVT</em>.'),
]

# ---------------------------------------------------------------- publications
# me = index of the author to bold. kind: conference | journal | preprint
PUBS = [
    dict(id="deblursdi", year=2026, kind="conference", star=True,
         title="Self-Diffusion Driven Blind Imaging",
         authors=["Y. Yang", "G. Luo"], me=0,
         venue="IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)", venue_short="CVPR 2026",
         detail="pp. 26711–26720",
         blurb="Zero-shot, self-supervised blind imaging: an iterative reverse self-diffusion process that starts from pure noise and jointly refines the sharp image and the unknown blur kernel — no pre-training.",
         links=[("Paper", "https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Self-Diffusion_Driven_Blind_Imaging_CVPR_2026_paper.html"),
                ("arXiv", "https://arxiv.org/abs/2510.27439"), ("Project", "/projects/deblursdi/")],
         fig="deblursdi"),
    dict(id="self-diffusion", year=2025, kind="preprint",
         title="Self-Diffusion for Solving Inverse Problems",
         authors=["G. Luo", "S. Huang", "Y. Yang"], me=2,
         venue="arXiv:2510.21417", venue_short="arXiv 2025",
         blurb="Alternates noising and denoising with an untrained convolutional self-denoiser, adapting to arbitrary forward operators without pretrained priors.",
         links=[("arXiv", "https://arxiv.org/abs/2510.21417"), ("Project", "/projects/self-diffusion/")],
         fig="self-diffusion"),
    dict(id="radarinv", year=2025, kind="preprint", star=True,
         title="Unsupervised Radar Point-Cloud Enhancement via Arbitrary LiDAR-Guided Diffusion Prior",
         authors=["Y. Yang", "J. Liu", "G. Luo", "H. Li", "E. Ahn", "M. Rahimi Azghadi", "T. Huang"], me=0,
         venue="arXiv:2505.09887", venue_short="arXiv 2025",
         blurb="Enhances sparse, noisy radar point clouds toward LiDAR-like density with a diffusion prior learned from arbitrary, unpaired LiDAR data.",
         links=[("arXiv", "https://arxiv.org/abs/2505.09887"), ("Code", "https://github.com/yyxr75/RadarINV"), ("Project", "/projects/radarinv/")],
         fig="radarinv"),
    dict(id="ralibev", year=2025, kind="journal", star=True,
         title="RaLiBEV: Radar and LiDAR BEV Fusion Learning for Anchor-Box-Free Object Detection Systems",
         authors=["Y. Yang*", "J. Liu*", "T. Huang", "Q.-L. Han", "G. Ma", "B. Zhu"], me=0,
         venue="IEEE Transactions on Circuits and Systems for Video Technology", venue_short="IEEE TCSVT 2025",
         detail="35(5):4130–4143 · *equal contribution",
         blurb="Fuses radar range–azimuth heatmaps with LiDAR in bird's-eye view for all-weather detection: +13.1% (clear) and +19.0% (fog) at IoU 0.8.",
         links=[("IEEE", "https://ieeexplore.ieee.org/document/10812016/"), ("arXiv", "https://arxiv.org/abs/2211.06108"),
                ("Code", "https://github.com/yyxr75/RaLiBEV"), ("Project", "/projects/ralibev/")],
         fig="ralibev"),
    dict(id="ssp", year=2023, kind="conference",
         title="SSP: Small Object Detection from Sparse Point Clouds of Roadside LiDAR for Vehicle-to-Infrastructure Cooperating Systems",
         authors=["H. Liang", "Y. Yang", "J. Li", "Y. Deng"], me=1,
         venue="ITS World Congress", venue_short="ITS WC 2023",
         blurb="Detecting pedestrians, cyclists and other small objects in the sparse point clouds of roadside LiDAR for V2I perception.",
         links=[("Project", "/projects/data-closed-loop/")], fig="ssp"),
    dict(id="thermal", year=2022, kind="journal",
         title="Fusion Reconstruction Method for 3D Temperature Fields on the Human Body Surface",
         authors=["Y. Yang", "C. Xu"], me=0,
         venue="Infrared Technology", venue_short="Infrared Technology 2022",
         blurb="Fuses depth and thermal imaging to reconstruct textured 3D temperature fields of the human body surface.",
         links=[("Project", "/projects/thermal-reconstruction/")], fig="thermal-reconstruction"),
    dict(id="metamaterial", year=2020, kind="journal",
         title="Observation of Phase Transitions of Ba0.6Sr0.4TiO3–Silicon Hybrid Metamaterial by THz Spectra",
         authors=["L. Wu", "Y. Fu", "N. Xu", "Q. Sheng", "X. Zhang", "Y. Yang", "et al."], me=5,
         venue="ACS Applied Electronic Materials", venue_short="ACS AEM 2020",
         blurb="THz-spectroscopy study of temperature-driven phase transitions in a BST–silicon hybrid metamaterial (undergraduate honours research).",
         links=[], fig="metamaterial"),
]

# --------------------------------------------------------------------- patents
PATENTS = [
    ("Method for Multiple-Target Detection and Related Product", "CN116863325B", 2022, ["Y. Yang", "J. Li", "Y. Deng"]),
    ("Assisted Parking Method, Device, Computer Equipment and Storage Medium", "CN114299146B", 2021, ["M. Liu", "Y. Yang", "Y. Deng", "Y. Fang"]),
    ("Point-Cloud Data Enhancement Method, Device, Computer Equipment, System and Storage Medium", "CN116359908B", 2021, ["Y. Yang", "J. Li", "F. Meng", "Y. Deng", "L. Wu"]),
    ("Automatic Parking Method, Roadside Equipment, Vehicle and System", "CN113997932B", 2021, ["K. Cao", "Y. Yang", "Y. Fang", "Y. Deng"]),
    ("Noise-Point Processing Method, Device, Equipment and Storage Medium", "CN116047477B", 2021, ["D. Liu", "J. Li", "Y. Yang"]),
    ("Method and Device for Generating Data, Electronic Equipment and Storage Medium", "CN116027288B", 2021, ["Y. Yang", "Y. Deng", "J. Li", "L. Wu"]),
    ("Multi-Sensor Signal Fusion Method, Device, Electronic Equipment and Storage Medium", "CN116027318B", 2021, ["Y. Deng", "Y. Yang", "J. Li", "L. Wu"]),
    ("Assisted-Driving Method for Vehicles in Parking Lots, Intelligent Terminal and Roadside Equipment", "CN115731738B", 2021, ["Y. Yang", "J. Li", "K. Cao"]),
    ("Target-Object Identification Method, Device, Electronic Equipment and Storage Medium", "CN113687358B", 2021, ["L. Wu", "Y. Yang"]),
]
PATENTS_NOTE = "Granted Chinese invention patents, assignee Vanjee Technology (filing year shown). Plus 13 pending applications (2021–2023) on millimetre-wave radar signal processing, multi-sensor target detection and tracking, and point-cloud generation."

# -------------------------------------------------------------------- projects
# cat: research | industry | public ; feat = shown on home
PROJECTS = [
    dict(slug="ausimmitool", cat="public", feat=True, period="Aug 2026 – Present", start=2026, end=9999,
         title="Australian Skilled-Migration Toolbox", sub="ausimmitool.com · solo, end-to-end",
         short="A public Chinese-language data site covering ~490 occupations, rebuilt automatically every month.",
         body=["Skilled-migration data in Australia is published monthly in a government dashboard that is hard to query. I built a public site that turns it into something people can use: per-occupation dashboards, a treemap heatmap of the whole EOI pool, and a watchlist that follows the occupations a visitor cares about.",
               "The pipeline scrapes the SkillSelect dashboard (a Qlik engine over WebSocket), detects each monthly release and rebuilds the site through GitHub Actions. A Cloudflare Worker serves an LLM-based CV-to-occupation matcher and email login for synced watchlists."],
         points=["Automated monthly data collection, cleaning and site rebuild", "Interactive treemap heatmap and occupation dashboards", "LLM CV-to-occupation matching behind a Cloudflare Worker API", "Written for a non-technical audience"],
         links=[("Visit ausimmitool.com", "https://ausimmitool.com")], shots=[("1", "Watchlist view: an occupation's EOI pool, six-month trend, score distribution and auto-generated takeaways.", "Live site, ausimmitool.com")],
         fig="ausimmitool"),
    dict(slug="world-models", cat="research", period="2025 – Present", start=2025, end=9999,
         title="World Models for Autonomous-Driving Perception", sub="PhD research · ongoing",
         short="Extending diffusion-based generative priors toward models that predict how the driving scene evolves.",
         body=["Perception systems see the present; a world model also predicts what comes next. This ongoing PhD work extends the generative priors from my radar and imaging research toward predictive world models of the driving environment, with occupancy as the shared representation.",
               "I maintain a curated survey of occupancy world models on GitHub."],
         points=["Generative priors for future-occupancy prediction", "Curated survey: Awesome-Occupancy-World-Model"],
         links=[("Awesome-Occupancy-World-Model", "https://github.com/yyxr75/Awesome-Occupancy-World-Model")], fig="world-models"),
    dict(slug="crocodile-detection", cat="research", feat=True, period="2024 – Present", start=2024, end=9999,
         title="AI Crocodile-Detection System", sub="JCU × Queensland Government (DETSI)",
         short="Computer vision that tells crocodiles apart from other floating objects, for real-time public-safety monitoring.",
         body=["Crocodiles are a real public-safety risk in North Queensland waterways. In a James Cook University collaboration with the Queensland Government (DETSI), I contributed computer-vision models that distinguish crocodiles from logs, debris and other floating objects.",
               "The models were trained on thousands of hours of real-world footage and deployed on a mobile, trailer-mounted camera platform for real-time monitoring."],
         points=["Trained on thousands of hours of field footage", "Deployed on a trailer-mounted camera platform", "Real-time public-safety monitoring in North Queensland"],
         links=[], fig="crocodile-detection"),
    dict(slug="deblursdi", cat="research", period="2025 – 2026", start=2025, end=2026,
         title="DeblurSDI — Self-Diffusion Driven Blind Imaging", sub="First author · CVPR 2026",
         short="Zero-shot blind image restoration that recovers both the sharp image and the unknown blur, with no pre-training.",
         body=["Blind inverse problems must estimate the latent image and the unknown degradation at the same time. Existing methods suffer from unstable convergence, limited priors and sensitivity to hyperparameters.",
               "DeblurSDI treats recovery as an iterative reverse self-diffusion process that starts from pure noise and progressively refines both the sharp image and the blur kernel. It is zero-shot and self-supervised — no pre-training and no external data — and outperforms other methods by a clear margin on combined optical aberrations and motion blur."],
         points=["Joint estimation of image and blur kernel", "No pre-training, no external data", "Published at CVPR 2026"],
         links=[("CVPR paper", "https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Self-Diffusion_Driven_Blind_Imaging_CVPR_2026_paper.html"), ("arXiv", "https://arxiv.org/abs/2510.27439")],
         pub="deblursdi", shots=[("1", "Blind deblurring on FFHQ faces. DeblurSDI recovers both the sharp image and the blur kernel (inset) with no pre-training.", "CVPR 2026 paper")],
         fig="deblursdi"),
    dict(slug="self-diffusion", cat="research", period="2025", start=2025, end=2025,
         title="Self-Diffusion for Solving Inverse Problems", sub="Co-author · arXiv 2025",
         short="A self-diffusion framework that adapts to arbitrary forward operators using an untrained self-denoiser.",
         body=["Self-diffusion alternates noising and denoising with an untrained convolutional self-denoiser. Because nothing is pretrained, the same procedure adapts to arbitrary forward operators — a general recipe for inverse problems where clean training data is scarce."],
         points=["Untrained convolutional self-denoiser", "Works with arbitrary forward operators", "Foundation for DeblurSDI"],
         links=[("arXiv", "https://arxiv.org/abs/2510.21417")], pub="self-diffusion", shots=[("1", "One untrained model, many inverse problems: inpainting, motion deblurring, 4× super-resolution, and accelerated 2D and 3D MRI.", "arXiv 2025 paper")],
         fig="self-diffusion"),
    dict(slug="radarinv", cat="research", period="2023 – 2025", start=2023, end=2025,
         title="RadarINV — Unsupervised Radar Point-Cloud Enhancement", sub="First author · arXiv 2025",
         short="Super-resolving sparse radar toward LiDAR-like density with a diffusion prior learned from unpaired LiDAR.",
         body=["A small automotive radar array cannot resolve nearby targets in angle, so its point clouds are sparse and noisy. RadarINV enhances them toward LiDAR-like density using a diffusion prior learned from arbitrary, unpaired LiDAR data — removing the need for paired radar/LiDAR supervision.",
               "The project began at Vanjee as radar super-resolution from raw radar signals and continued into my PhD."],
         points=["Unsupervised: no paired radar/LiDAR data", "Diffusion prior from arbitrary LiDAR datasets", "Array super-resolution as an inverse problem"],
         links=[("arXiv", "https://arxiv.org/abs/2505.09887"), ("Code", "https://github.com/yyxr75/RadarINV")], pub="radarinv", shots=[("1", "Framework: a diffusion prior trained on LiDAR BEV images, then posterior sampling guided by the radar forward model (range FFT → Doppler → beamforming).", "RadarINV paper")],
         fig="radarinv"),
    dict(slug="ralibev", cat="research", period="2022 – 2025", start=2022, end=2025,
         title="RaLiBEV — Radar &amp; LiDAR BEV Fusion", sub="Co-first author · IEEE TCSVT 2025",
         short="Anchor-box-free radar–LiDAR fusion in bird's-eye view for object detection in fog and rain.",
         body=["Radar penetrates rain and fog where LiDAR degrades. RaLiBEV fuses radar range–azimuth heatmaps with LiDAR point clouds in a bird's-eye-view representation, using an interactive transformer-based fusion module and a consistency-aware label assignment strategy for anchor-box-free detection.",
               "It outperforms prior methods by 13.1% in clear weather and 19.0% in fog at IoU 0.8."],
         points=["Interactive transformer fusion of radar and LiDAR", "Consistency-aware label assignment, anchor-box-free", "+19.0% in fog at IoU 0.8"],
         links=[("IEEE Xplore", "https://ieeexplore.ieee.org/document/10812016/"), ("arXiv", "https://arxiv.org/abs/2211.06108"), ("Code", "https://github.com/yyxr75/RaLiBEV")],
         pub="ralibev", shots=[("1", "Architecture: LiDAR and radar range–azimuth features meet in an interactive transformer-based BEV fusion module, then an anchor-free head predicts oriented boxes.", "IEEE TCSVT paper")],
         fig="ralibev"),
    dict(slug="data-closed-loop", cat="industry", period="2022 – 2024", start=2022, end=2024,
         title="Data Closed-Loop for Vehicle–Road Cooperative Perception", sub="Vanjee Technology · team lead",
         short="A pipeline that feeds field data back into training to improve perception for V2I cooperative driving.",
         body=["Perception models for vehicle–road cooperative (V2I) driving meet conditions in the field that no training set anticipated. I led a three-person team building a data closed-loop system: collect real-world roadside sensor data, clean it and mine the hard cases, retrain, and redeploy.",
               "Version 1.0 was rolled out to customers. Related roadside-LiDAR research appeared as SSP at the ITS World Congress 2023."],
         points=["Led a team of three engineers", "Collect → clean &amp; mine → retrain → redeploy", "v1.0 shipped to customers"],
         links=[], pub="ssp", fig="data-closed-loop"),
    dict(slug="mimo-radar", cat="industry", feat=True, period="2020 – 2022", start=2020, end=2022,
         title="MIMO Radar Signal-Processing Chain", sub="Vanjee Technology",
         short="The full processing chain of an in-house millimetre-wave radar toolkit, from raw array signals to detections.",
         body=["Starting from the TI reference design, I built the signal-processing chain of an in-house MIMO radar toolkit: range and Doppler FFTs, detection in noise and clutter, and angle-of-arrival estimation from phase differences across the antenna array.",
               "The hardware and software were deployed on an engineering sample unit and laid the groundwork for the radar–LiDAR fusion work that became RaLiBEV."],
         points=["Range and Doppler FFTs, CFAR detection", "Angle-of-arrival estimation across the array", "Deployed on an engineering sample unit"],
         links=[], fig="mimo-radar"),
    dict(slug="thermal-reconstruction", cat="research", period="2018 – 2020", start=2018, end=2020,
         title="3D Human Thermal-Surface Reconstruction", sub="Master's research · Beijing Institute of Technology",
         short="Fusing depth and thermal cameras to build 3D human body models textured with temperature.",
         body=["A ROS-based capture system time-synchronises an Intel RealSense D435i depth camera with a lab-built FLIR thermal camera. Point-cloud registration and global optimisation reconstruct a full 3D body model, and thermal imagery is UV-mapped onto the mesh to output a textured 3D thermal body for analysing surface heat distribution.",
               "I designed the hardware, software and mechanical structure."],
         points=["ROS-based multi-camera time synchronisation", "Point-cloud registration and global optimisation", "UV-mapped thermal texture on a 3D mesh"],
         links=[], pub="thermal", fig="thermal-reconstruction"),
    dict(slug="smart-car", cat="research", period="2015 – 2017", start=2015, end=2017,
         title="Autonomous Smart-Car — NXP Cup", sub="Tianjin University · hardware lead",
         short="Circuit boards and vision software for a self-driving model car; National Second Prize.",
         body=["For the China National University Smart-Car Competition (NXP Cup), I designed the car's circuit boards in Altium Designer around a Freescale K60 MCU — power supply, motor driver and CCD camera acquisition — and co-developed the software: Otsu-threshold binarisation for road-edge detection and closed-loop steering and speed control.",
               "The team won the National Second Prize, ranked 24th of 200+ teams."],
         points=["PCB design around a Freescale K60 MCU", "Otsu-based road-edge detection", "National Second Prize (24th of 200+)"],
         links=[], fig="smart-car"),
]

# ------------------------------------------------------------------ about/CV
EDUCATION = [
    ("PhD, Engineering — Computer Vision &amp; Machine Learning", "James Cook University, Cairns", "Apr 2024 – Oct 2027 (expected)", "Advisor: Dr Tao Huang. Generative priors for sensing and inverse problems."),
    ("MEng by Research, Optical Engineering", "Beijing Institute of Technology", "2017 – 2020", "Thesis: 3D human thermal-surface reconstruction (86.8 / 100)."),
    ("BEng, Opto-Electronics Engineering", "Tianjin University", "2013 – 2017", "Honours thesis: THz spectroscopy of BST–silicon metamaterials (86 / 100)."),
]
EXPERIENCE = [
    ("Doctoral Researcher", "James Cook University, Cairns", "Apr 2024 – Present", "Generative priors for radar super-resolution and blind imaging; world models for perception; computer vision for the JCU × Queensland Government crocodile-detection system."),
    ("Algorithm Engineer", "Vanjee Technology, Beijing", "2020 – 2024", "Radar signal processing and radar–LiDAR perception for autonomous and vehicle–road cooperative driving. Led a three-person data closed-loop team; nine granted invention patents."),
    ("Graduate Researcher", "Beijing Institute of Technology", "2018 – 2020", "Hardware, software and mechanical design for 3D human thermal-surface reconstruction."),
]
HONOURS = [
    ("Postgraduate Research Stipend Scholarship (HDR)", "James Cook University", "2024 – Present"),
    ("Second-Class Academic Scholarship, awarded each year", "Beijing Institute of Technology", "2017 – 2020"),
    ("National Second Prize, NXP Cup — ranked 24th of 200+ teams", "China National University Smart-Car Competition", "2017"),
    ("Golden Boot &amp; team champion", "Vanjee Technology football tournament", "2020 – 2024"),
]
SERVICE = [
    ("Cairns Campus Officer", "JCU Student Association", "2025 – 2026"),
    ("Postgraduate Officer", "JCU Student Association", "2024 – 2025"),
    ("Reviewer", "AAAI Conference on Artificial Intelligence (2025, 2026)", "2025 – 2026"),
    ("Reviewer", "International Conference on Learning Representations (2025, 2026)", "2025 – 2026"),
]
SKILLS = [
    ("Programming", "Python (primary), C/C++, MATLAB, JavaScript · Linux, Git, Jupyter"),
    ("Deep learning", "PyTorch · 3D object detection &amp; tracking · BEV / multi-sensor fusion · diffusion &amp; generative models · self-supervised learning · GPU training"),
    ("Perception &amp; 3D", "point clouds (PCL), radar heatmaps, camera vision, 3D reconstruction, OpenGL"),
    ("Systems", "data closed-loop pipelines, model deployment on field hardware, ROS, Qt, GitHub Actions CI, Cloudflare Workers, web front-end"),
    ("Signals &amp; hardware", "MIMO radar signal processing (FFT, CFAR, angle of arrival), multi-sensor time sync, PCB design (Altium), embedded MCUs"),
    ("Languages", "Chinese (native), English"),
]

# Old Jekyll URLs that must keep working.
REDIRECTS = {
    "publications/": "/research/",
    "about/": "/about/",  # real page, listed for completeness
    "resume/": "/cv/",
    "publication/2026-deblursdi/": "/research/#deblursdi",
    "publication/2025-self-diffusion-inverse/": "/research/#self-diffusion",
    "publication/2025-radarinv/": "/research/#radarinv",
    "publication/2025-ralibev/": "/research/#ralibev",
    "publication/2023-ssp/": "/research/#ssp",
    "publication/2022-thermal-reconstruction/": "/research/#thermal",
    "publication/2020-metamaterial-thz/": "/research/#metamaterial",
}
