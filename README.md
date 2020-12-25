# Understanding Urban Structures and Crowd Dynamics Leveraging Large-Scale Vehicle Mobility Data

A comprehensive understanding of city structures and ur- ban dynamics can greatly improve the efficiency and quality of urban planning and management, while the traditional approaches of which, such as manual surveys, usually incur substantial labor and time. In this paper, we propose a data- driven framework to sense urban structures and dynamics from large-scale vehicle mobility data. First, we divide the city into fine-grained grids, and cluster the grids with similar mobility features into structured urban areas with a proposed distance-constrained clustering algorithm (DCCA). Second, we detect irregular mobility traffic patterns in each area leveraging an ARIMA-based anomaly detection algo- rithm (ADAM), and correlate them to the urban social and emergency events. Finally, we build a visualization system to demonstrate the urban structures and crowd dynamics. We evaluate our framework using real-world datasets collected from Xiamen City, China, and the results show that the proposed framework can sense urban structures and crowd comprehensively and effectively.

/proc: data processing codes

/viz: the visualization platform

If you find this repository, e.g., the code and the datasets, useful in your research, please cite the following paper:

    @article{jiang2020understanding,
      title={Understanding urban structures and crowd dynamics leveraging large-scale vehicle mobility data},
      author={Jiang, Zhihan and Liu, Yan and Fan, Xiaoliang and Wang, Cheng and Li, Jonathan and Chen, Longbiao},
      journal={Frontiers of Computer Science},
      volume={14},
      number={5},
      pages={1--12},
      year={2020},
      publisher={Springer}
    }